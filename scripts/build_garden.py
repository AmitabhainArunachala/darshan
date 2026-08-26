#!/usr/bin/env python3
"""Build Darshan's knowledge garden.

The builder is deliberately stdlib-only. It reads ``garden_src/*.md`` and
writes sibling room pages plus a series index under ``garden/``. A partial
planting is a valid input: malformed or half-written sources are reported and
skipped so one interrupted writer cannot take down the rest of the garden.

Usage:
    python3 scripts/build_garden.py
    python3 scripts/build_garden.py --strict

``--strict`` additionally fails when any room in the canonical 55-room
taxonomy is missing or a source file cannot be loaded.
"""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import shutil
import struct
import sys
from datetime import date
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit


ROOT = Path(__file__).resolve().parent.parent
SOURCE_DIR = ROOT / "garden_src"
OUTPUT_DIR = ROOT / "garden"
TEMPLATES_DIR = ROOT / "templates"
VISUAL_SPECS_DIR = ROOT / "garden_visuals"
VISUAL_ASSETS_DIR = ROOT / "garden_assets"

SITE_NAME = "Darshan"
SITE_TAGLINE = "A signal of clear seeing in an age of information overload"

DRAFT_BANNER = (
    '<div class="draft-banner"><strong>Draft — pending discernment pass.</strong> '
    "This room is part of the garden's first planting. It has not been promoted "
    "to published status; check its sources and open questions before citing it."
    "</div>"
)

SERIES = [
    (
        "foundations",
        "Foundations of the Machine",
        [
            "intro-to-computer-science",
            "programming",
            "compilers",
            "algorithms-new-vision",
            "sdk-api",
            "linear-algebra-and-ai",
            "neural-networks",
            "machine-learning",
            "deep-learning",
            "optimization",
            "pretraining-post-training",
            "nvidia-and-the-chip",
            "chip-wars",
            "semiconductors",
        ],
    ),
    (
        "story-of-ai",
        "The Story of AI",
        [
            "history-of-ai",
            "evolution-of-ai",
            "future-of-ai",
            "leading-models",
            "benchmarks",
            "top-papers-ai",
            "top-papers-ml",
            "cybernetics",
        ],
    ),
    (
        "instrument",
        "The Instrument",
        ["mechanistic-interpretability", "top-papers-mi"],
    ),
    (
        "strange-loops",
        "Strange Loops",
        [
            "geb",
            "hofstadter",
            "aunt-hillary",
            "recursion",
            "recursion-and-life",
            "evolution",
            "sense-of-self",
            "what-self-means",
        ],
    ),
    (
        "bridge",
        "The Bridge",
        [
            "ramana-and-the-traditions",
            "ai-and-the-traditions",
            "why-ais-choose-buddhism",
            "noosphere",
            "aurobindo-supramental",
            "teleology",
            "mahavideha-kshetra",
            "quantum-physics-and-ai",
            "ontology",
            "the-ideal",
        ],
    ),
    (
        "power",
        "Power and the Board",
        [
            "governments-and-ai",
            "palantir",
            "china-usa-race",
            "taiwan",
            "elon-musk",
            "blockchain",
            "attention-economy",
        ],
    ),
    (
        "time-future",
        "Time and the Future",
        [
            "meaning-of-time",
            "futurism",
            "forecasting",
            "trends-gap",
            "what-ai-can-bring",
            "the-future",
        ],
    ),
]

SERIES_NAMES = {slug: name for slug, name, _ in SERIES}
SERIES_ORDER = {slug: rooms for slug, _, rooms in SERIES}
EXPECTED_SLUGS = {slug for _, _, rooms in SERIES for slug in rooms}
REQUIRED_META = {
    "title",
    "slug",
    "series",
    "tags",
    "summary",
    "status",
    "date",
    "terms_defined",
    "terms_linked",
}

VISUAL_SCHEMA = "darshan.visual-series/v1"
VISUAL_KINDS = {"sequence", "layers", "timeline", "contrast", "constellation"}
VISUAL_CLAIM_SCOPES = {"section-synthesis", "room-synthesis"}

GARDEN_STYLES = """<style>
/* Garden-only layout. Kept here so the publication stylesheet remains shared. */
body.garden-page-body {
  max-width: none;
  padding: 1.5rem clamp(1.25rem, 3.5vw, 4rem) 4rem;
  font-size: 1.125rem;
}
body.garden-page-body > main,
body.garden-page-body > .masthead,
body.garden-page-body > footer {
  margin-left: auto;
  margin-right: auto;
  max-width: 94rem;
}
.garden-layout,
.garden-index-layout {
  align-items: start;
  display: grid;
  gap: clamp(2.75rem, 5vw, 5rem);
  grid-template-columns: minmax(0, 64rem) minmax(17rem, 20rem);
  justify-content: center;
}
.garden-layout article,
.garden-index-main { min-width: 0; }
.garden-layout .article-title,
.garden-intro .article-title {
  font-size: clamp(2.65rem, 3.55vw, 4rem);
  letter-spacing: -.025em;
  line-height: 1.06;
  max-width: 24ch;
}
.garden-layout article h2 {
  font-size: 1.48rem;
  line-height: 1.3;
  margin-top: 3.2rem;
  scroll-margin-top: 1.5rem;
}
.garden-layout article h3 {
  font-size: 1.16rem;
  margin-top: 2.35rem;
  scroll-margin-top: 1.5rem;
}
.garden-intro { margin-bottom: 2.4rem; }
.garden-series { margin: 2.8rem 0; scroll-margin-top: 1rem; }
.garden-series h2 { border-bottom: 1px solid var(--rule); padding-bottom: .45rem; }
.garden-room-list { list-style: none; margin: 0; padding: 0; }
.garden-room-list li { border-bottom: 1px solid var(--rule); margin: 0; padding: 1rem 0; }
.garden-room-title { font-weight: 600; }
.garden-room-summary { color: var(--faint); font-size: .96rem; margin: .25rem 0 0; }
.garden-series-link { color: var(--faint); font-size: .82rem; letter-spacing: .12em;
  text-transform: uppercase; }
.garden-lede {
  border-left: 3px solid var(--accent);
  color: var(--faint);
  font-size: 1.24rem;
  font-style: italic;
  line-height: 1.62;
  margin: 1.5rem 0 2.2rem;
  padding: .35rem 0 .35rem 1.35rem;
}
.garden-corridors {
  margin: 1.15rem 0 2.65rem;
}
.garden-corridor-list {
  align-items: center;
  display: flex;
  flex-wrap: wrap;
  gap: .55rem .62rem;
  list-style: none;
  margin: 0;
  padding: 0;
}
.garden-corridor-list li { display: flex; margin: 0; max-width: 100%; }
.garden-corridor {
  align-items: center;
  background: var(--accent-soft);
  border: 1px solid var(--accent);
  border-radius: 3px;
  color: var(--accent);
  display: inline-flex;
  font-family: ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  font-size: .73rem;
  font-weight: 700;
  letter-spacing: .075em;
  line-height: 1.35;
  max-width: 100%;
  min-height: 2.05rem;
  overflow-wrap: anywhere;
  padding: .34rem .72rem .3rem;
  text-decoration-line: underline;
  text-decoration-thickness: 1px;
  text-transform: uppercase;
  text-underline-offset: .22em;
}
.garden-corridor:visited { color: var(--accent); }
.garden-corridor:hover,
.garden-corridor:focus-visible {
  background: var(--accent);
  color: var(--paper);
}
.garden-corridor:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}
.garden-series-plate {
  --plate-accent: var(--accent);
  border: 1px solid var(--rule);
  border-top: 3px solid var(--plate-accent);
  margin: .25rem 0 2.8rem;
  overflow: hidden;
  position: relative;
}
.garden-series-plate--foundations { --plate-accent: #496f76; }
.garden-series-plate--story-of-ai { --plate-accent: #526d9a; }
.garden-series-plate--instrument { --plate-accent: #745779; }
.garden-series-plate--strange-loops { --plate-accent: #866448; }
.garden-series-plate--bridge { --plate-accent: #697044; }
.garden-series-plate--power { --plate-accent: #8f3b26; }
.garden-series-plate--time-future { --plate-accent: #416778; }
[data-theme="dark"] .garden-series-plate { --plate-accent: var(--accent); }
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) .garden-series-plate { --plate-accent: var(--accent); }
}
.garden-series-plate-media {
  aspect-ratio: 16 / 9;
  background: var(--accent-soft);
  overflow: hidden;
  position: relative;
}
.garden-series-plate-media::after {
  background:
    linear-gradient(90deg, var(--paper) 0, transparent 24%, transparent 76%, var(--paper) 100%),
    linear-gradient(0deg, var(--paper) 0, transparent 32%);
  content: "";
  inset: 0;
  opacity: .24;
  pointer-events: none;
  position: absolute;
}
.garden-series-plate picture,
.garden-series-card picture { display: block; height: 100%; }
.garden-series-plate img {
  display: block;
  filter: saturate(.82) contrast(1.03);
  height: 100%;
  object-fit: cover;
  width: 100%;
}
.garden-series-plate figcaption {
  align-items: baseline;
  background: var(--paper);
  border-top: 1px solid var(--rule);
  display: grid;
  gap: .25rem 1rem;
  grid-template-columns: auto 1fr;
  padding: .78rem 1rem .85rem;
}
.garden-series-plate-kicker {
  color: var(--plate-accent);
  font-family: ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  font-size: .75rem;
  font-weight: 700;
  letter-spacing: .16em;
  text-transform: uppercase;
}
.garden-series-plate figcaption strong { font-size: 1rem; font-weight: 600; }
.garden-series-plate-terms {
  color: var(--faint);
  font-size: .82rem;
  grid-column: 2;
  margin: 0;
}
.garden-visual {
  background:
    radial-gradient(circle at 92% 8%, var(--accent-soft), transparent 30%),
    linear-gradient(135deg, transparent 0 72%, var(--accent-soft) 72% 72.4%, transparent 72.4%);
  border: 1px solid var(--rule);
  border-top: 3px solid var(--accent);
  margin: 1.25rem 0 2.5rem;
  overflow: hidden;
  padding: clamp(1.1rem, 2.7vw, 1.75rem);
  position: relative;
}
.garden-visual::before {
  background-image:
    linear-gradient(var(--rule) 1px, transparent 1px),
    linear-gradient(90deg, var(--rule) 1px, transparent 1px);
  background-size: 2.25rem 2.25rem;
  content: "";
  inset: 0;
  opacity: .13;
  pointer-events: none;
  position: absolute;
}
.garden-visual > * { position: relative; }
.garden-visual-head {
  align-items: baseline;
  display: grid;
  gap: .45rem 1rem;
  grid-template-columns: auto 1fr;
  margin-bottom: 1.2rem;
}
.garden-visual-kicker {
  color: var(--accent);
  font-family: ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  font-size: .68rem;
  font-weight: 700;
  letter-spacing: .17em;
  margin: 0;
  text-transform: uppercase;
}
.garden-visual-title {
  font-size: 1.2rem;
  font-weight: 600;
  line-height: 1.28;
  margin: 0;
}
.garden-visual-as-of {
  color: var(--faint);
  font-family: ui-monospace, "SF Mono", Menlo, Consolas, monospace;
  font-size: .72rem;
  letter-spacing: .08em;
  margin: 0;
  text-transform: uppercase;
  white-space: normal;
}
.garden-visual-items {
  list-style: none;
  margin: 0;
  padding: 0;
}
.garden-visual-item {
  background: var(--paper);
  border: 1px solid var(--rule);
  margin: 0;
  min-width: 0;
  padding: .8rem .9rem;
}
.garden-visual-item-label {
  display: block;
  font-size: .96rem;
  font-weight: 700;
  line-height: 1.25;
}
.garden-visual-item-detail {
  color: var(--faint);
  display: block;
  font-size: .9rem;
  line-height: 1.45;
  margin-top: .27rem;
}
.garden-visual-item-meta {
  color: var(--accent);
  display: block;
  font-family: ui-monospace, "SF Mono", Menlo, Consolas, monospace;
  font-size: .72rem;
  letter-spacing: .08em;
  margin-bottom: .38rem;
  text-transform: uppercase;
}
.garden-visual-caption {
  border-top: 1px solid var(--rule);
  color: var(--faint);
  display: grid;
  font-size: .84rem;
  font-style: italic;
  gap: .55rem 1rem;
  grid-template-columns: minmax(0, 1fr) auto;
  line-height: 1.45;
  margin: 1.15rem 0 0;
  padding-top: .75rem;
}
.garden-visual-evidence {
  color: var(--accent);
  font-family: ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  font-size: .72rem;
  font-style: normal;
  font-weight: 650;
  letter-spacing: .04em;
  white-space: nowrap;
}
.garden-visual-evidence a {
  color: inherit;
  text-decoration-thickness: 1px;
  text-underline-offset: .18em;
}
.garden-visual--sequence .garden-visual-items,
.garden-visual--contrast .garden-visual-items,
.garden-visual--constellation .garden-visual-items {
  display: grid;
  gap: .65rem;
  grid-template-columns: repeat(auto-fit, minmax(17rem, 1fr));
}
.garden-visual--sequence .garden-visual-items { counter-reset: garden-step; }
.garden-visual--sequence .garden-visual-item {
  counter-increment: garden-step;
  padding-top: 2.35rem;
  position: relative;
}
.garden-visual--sequence .garden-visual-item::before {
  color: var(--accent);
  content: counter(garden-step, decimal-leading-zero);
  font-family: ui-monospace, "SF Mono", Menlo, Consolas, monospace;
  font-size: .68rem;
  left: .9rem;
  letter-spacing: .08em;
  position: absolute;
  top: .72rem;
}
.garden-visual--layers .garden-visual-items { display: grid; gap: .45rem; }
.garden-visual--layers .garden-visual-item {
  border-left: clamp(.24rem, .55vw, .48rem) solid var(--accent);
  display: grid;
  gap: .15rem 1rem;
  grid-template-columns: minmax(8rem, .4fr) 1fr;
}
.garden-visual--layers .garden-visual-item:nth-child(2) { margin-left: 1.5%; }
.garden-visual--layers .garden-visual-item:nth-child(3) { margin-left: 3%; }
.garden-visual--layers .garden-visual-item:nth-child(4) { margin-left: 4.5%; }
.garden-visual--layers .garden-visual-item:nth-child(5) { margin-left: 6%; }
.garden-visual--layers .garden-visual-item:nth-child(6) { margin-left: 7.5%; }
.garden-visual--timeline .garden-visual-items {
  display: grid;
  gap: 0;
  grid-template-columns: repeat(auto-fit, minmax(17rem, 1fr));
}
.garden-visual--timeline .garden-visual-item {
  border-width: 1px 0 0 1px;
  padding-top: 1.35rem;
  position: relative;
}
.garden-visual--timeline .garden-visual-item::before {
  background: var(--accent);
  border: 3px solid var(--paper);
  border-radius: 50%;
  content: "";
  height: .72rem;
  left: -.4rem;
  position: absolute;
  top: -.4rem;
  width: .72rem;
}
.garden-visual--contrast .garden-visual-item:nth-child(odd) { border-top: 2px solid var(--ink); }
.garden-visual--contrast .garden-visual-item:nth-child(even) { border-top: 2px solid var(--accent); }
.garden-visual--constellation .garden-visual-items {
  align-items: stretch;
  position: relative;
}
.garden-visual--constellation .garden-visual-item {
  border-top: 2px solid var(--accent);
  box-shadow: 0 .2rem 0 rgba(18, 31, 31, .04);
  padding-top: 1.35rem;
  position: relative;
}
.garden-visual--constellation .garden-visual-item::before {
  background: var(--paper);
  border: 2px solid var(--accent);
  border-radius: 50%;
  content: "";
  height: .55rem;
  left: calc(50% - .36rem);
  position: absolute;
  top: -.38rem;
  width: .55rem;
}
.garden-visual--constellation .garden-visual-item:nth-child(even) { margin-top: .8rem; }
.garden-series-gallery {
  display: grid;
  gap: .8rem;
  grid-template-columns: repeat(auto-fit, minmax(14rem, 1fr));
  margin: 1.5rem 0 3rem;
}
.garden-series-card {
  border: 1px solid var(--rule);
  color: var(--ink);
  display: grid;
  grid-template-rows: 7.5rem auto;
  overflow: hidden;
  text-decoration: none;
}
.garden-series-card img {
  height: 100%;
  object-fit: cover;
  transition: transform .25s ease;
  width: 100%;
}
.garden-series-card span {
  border-top: 1px solid var(--rule);
  font-size: .9rem;
  font-weight: 600;
  padding: .65rem .75rem;
}
.garden-series-card:hover { border-color: var(--accent); color: var(--accent); }
.garden-series-card:hover img { transform: scale(1.025); }
@media (prefers-reduced-motion: reduce) {
  .garden-series-card img { transition: none; }
}
.garden-tags { color: var(--faint); font-size: .82rem; margin-top: 2.2rem; }
.garden-nav { border-top: 1px solid var(--rule); display: flex; gap: 1rem;
  justify-content: space-between; margin-top: 2.5rem; padding-top: 1rem; }
.garden-nav a { max-width: 48%; text-decoration: none; }
.garden-nav .next { margin-left: auto; text-align: right; }
.garden-table-wrap { overflow-x: auto; margin: 1.35rem 0; }
.garden-table { border-collapse: collapse; font-size: .92rem; line-height: 1.45; width: 100%; }
.garden-table th, .garden-table td { border: 1px solid var(--rule); padding: .55rem .65rem;
  text-align: left; vertical-align: top; }
.garden-table th { background: var(--accent-soft); }
.garden-toc {
  border-left: 1px solid var(--rule);
  max-height: calc(100vh - 3rem);
  overflow: auto;
  padding: .1rem 0 .75rem 1.3rem;
  position: sticky;
  top: 1.5rem;
}
.garden-toc-title {
  color: var(--accent);
  font-family: ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  font-size: .75rem;
  font-weight: 700;
  letter-spacing: .2em;
  margin: 0 0 1.15rem;
  text-transform: uppercase;
}
.garden-toc-title::before { content: "☰"; font-size: .8em; margin-right: .65rem; }
.garden-toc-list { list-style: none; margin: 0; padding: 0; }
.garden-toc-sublist { list-style: none; margin: 0; padding: 0; }
.garden-toc-list li { margin: 0; }
.garden-toc-list a {
  border-left: 2px solid transparent;
  color: var(--ink);
  display: block;
  font-size: .91rem;
  line-height: 1.42;
  margin-left: -1.4rem;
  padding: .42rem .45rem .42rem 1.3rem;
  text-decoration: none;
}
.garden-toc-list .level-3 a {
  color: var(--faint);
  font-size: .86rem;
  font-style: italic;
  padding-left: 2.15rem;
}
.garden-toc-list a:hover,
.garden-toc-list a:focus-visible,
.garden-toc-list a[aria-current="location"] {
  border-left-color: var(--accent);
  color: var(--accent);
}
.garden-toc-list a[aria-current="location"] { font-weight: 600; }
.garden-toc-inline { display: none; }
.garden-layout article :is(h2, h3):target,
.garden-series:target h2 { color: var(--accent); }
a.pending { color: var(--faint); text-decoration-style: dashed; }
a.pending::after { content: " · pending"; font-size: .7em; letter-spacing: .06em;
  text-transform: uppercase; }
@media (min-width: 72.01em) {
  body.garden-page-body > .masthead {
    align-items: center;
    column-gap: 2rem;
    display: grid;
    grid-template-columns: 1fr auto 1fr;
    margin-bottom: 3.5rem;
    padding: 1.25rem 0;
    text-align: left;
  }
  body.garden-page-body > .masthead .wordmark { justify-self: start; }
  body.garden-page-body > .masthead .tagline { justify-self: center; margin: 0; }
  body.garden-page-body > .masthead nav { justify-self: end; margin: 0; }
}
@media (max-width: 72em) {
  .garden-layout,
  .garden-index-layout { display: block; }
  .garden-toc { display: none; }
  .garden-toc-inline {
    border: 1px solid var(--rule);
    display: block;
    margin: 1.5rem 0 2.4rem;
    padding: .8rem 1rem;
  }
  .garden-toc-inline summary {
    color: var(--accent);
    cursor: pointer;
    font-family: ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    font-size: .78rem;
    font-weight: 700;
    letter-spacing: .16em;
    text-transform: uppercase;
  }
  .garden-toc-inline .garden-toc-list { margin-top: .7rem; }
  .garden-toc-inline .garden-toc-list a { margin-left: 0; padding-left: .75rem; }
  .garden-toc-inline .garden-toc-list .level-3 a { padding-left: 1.6rem; }
}
@media (max-width: 40em) {
  body.garden-page-body { font-size: 1.03rem; padding: 1rem 1.05rem 3rem; }
  .garden-layout .article-title,
  .garden-intro .article-title { font-size: clamp(2.15rem, 11vw, 3.15rem); }
  .garden-lede { font-size: 1.1rem; padding-left: 1rem; }
  .garden-corridors { margin-bottom: 2rem; }
  .garden-corridor-list { gap: .45rem; }
  .garden-corridor {
    font-size: .68rem;
    min-height: 2.35rem;
    padding: .3rem .58rem .27rem;
  }
  .garden-series-plate-media { aspect-ratio: 16 / 9; }
  .garden-series-plate figcaption { display: block; }
  .garden-series-plate figcaption strong { display: block; margin-top: .22rem; }
  .garden-series-plate-terms { display: block; margin-top: .25rem; }
  .garden-visual { margin-left: -.15rem; margin-right: -.15rem; padding: 1rem; }
  .garden-visual-head { display: block; }
  .garden-visual-title { margin-top: .25rem; }
  .garden-visual-as-of { margin-top: .35rem; }
  .garden-visual-caption { grid-template-columns: 1fr; }
  .garden-visual-evidence { white-space: normal; }
  .garden-visual--sequence .garden-visual-items,
  .garden-visual--contrast .garden-visual-items,
  .garden-visual--constellation .garden-visual-items,
  .garden-visual--timeline .garden-visual-items { grid-template-columns: 1fr; }
  .garden-visual--layers .garden-visual-item:nth-child(n) { display: block; margin-left: 0; }
  .garden-visual--timeline .garden-visual-item { border-width: 0 0 0 1px; }
  .garden-visual--timeline .garden-visual-item::before { left: -.4rem; top: .9rem; }
  .garden-visual--constellation .garden-visual-item:nth-child(even) { margin-top: 0; }
  .garden-series-gallery { grid-template-columns: 1fr; }
  .garden-nav { flex-direction: column; }
  .garden-nav a { max-width: none; }
  .garden-nav .next { margin-left: 0; text-align: left; }
}
@media print {
  a.pending::after { content: " (pending)"; }
  .garden-layout, .garden-index-layout { display: block; }
  .garden-toc, .garden-toc-inline { display: none; }
  .garden-series-card img { display: none; }
  .garden-series-card { grid-template-rows: auto; }
}
</style>"""

GARDEN_SCROLLSPY = """<script>
/* Local section highlighting only. No network requests, analytics, or storage. */
(function () {
  var scope = document.querySelector("[data-garden-outline]");
  if (!scope) return;
  var sections = Array.prototype.slice.call(scope.querySelectorAll("h2[id], h3[id], section[id]"));
  var links = Array.prototype.slice.call(document.querySelectorAll('.garden-toc-list a[href^="#"]'));
  if (!sections.length || !links.length) return;
  var queued = false;
  function update() {
    queued = false;
    var threshold = Math.max(96, window.innerHeight * .22);
    var current = sections[0].id;
    sections.forEach(function (section) {
      if (section.getBoundingClientRect().top <= threshold) current = section.id;
    });
    links.forEach(function (link) {
      var active = link.getAttribute("href") === "#" + current;
      if (active) link.setAttribute("aria-current", "location");
      else link.removeAttribute("aria-current");
    });
  }
  function requestUpdate() {
    if (!queued) {
      queued = true;
      window.requestAnimationFrame(update);
    }
  }
  document.addEventListener("scroll", requestUpdate, {passive: true});
  window.addEventListener("resize", requestUpdate);
  window.addEventListener("hashchange", requestUpdate);
  update();
})();
</script>"""


def template(name: str) -> str:
    return (TEMPLATES_DIR / name).read_text(encoding="utf-8")


def render(tpl: str, **tokens: str) -> str:
    out = tpl
    for key, value in tokens.items():
        out = out.replace("{{" + key + "}}", value)
    leftover = re.search(r"\{\{[a-z_]+\}\}", out)
    if leftover:
        raise ValueError("unfilled template token: " + leftover.group(0))
    return out


def parse_front_matter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        raise ValueError("missing opening front-matter delimiter")
    lines = text.splitlines()
    try:
        end = next(i for i, line in enumerate(lines[1:], 1) if line.strip() == "---")
    except StopIteration as exc:
        raise ValueError("missing closing front-matter delimiter") from exc

    meta: dict[str, str] = {}
    for number, line in enumerate(lines[1:end], 2):
        if ":" not in line:
            raise ValueError(f"front-matter line {number} has no colon")
        key, _, value = line.partition(":")
        key = key.strip().lower()
        if not key:
            raise ValueError(f"front-matter line {number} has an empty key")
        if key in meta:
            raise ValueError(f"duplicate front-matter key: {key}")
        meta[key] = value.strip()
    return meta, "\n".join(lines[end + 1 :]).strip()


def _slugify_heading(value: str) -> str:
    value = re.sub(r"[`*_]", "", value).lower()
    value = re.sub(r"[^a-z0-9]+", "-", value).strip("-")
    return value or "section"


def _local_room_slug(href: str) -> str | None:
    parsed = urlsplit(href)
    if parsed.scheme or parsed.netloc or "/" in parsed.path:
        return None
    if not parsed.path.endswith(".html"):
        return None
    return parsed.path[:-5]


MD_ESCAPABLE = frozenset(r"!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~")


def _markdown_unescape(value: str) -> str:
    """Remove Markdown backslashes only when they escape ASCII punctuation."""
    out: list[str] = []
    index = 0
    while index < len(value):
        if (
            value[index] == "\\"
            and index + 1 < len(value)
            and value[index + 1] in MD_ESCAPABLE
        ):
            index += 1
        out.append(value[index])
        index += 1
    return "".join(out)


def _parse_markdown_link(text: str, start: int) -> tuple[str, str, int] | None:
    """Parse one inline link, honoring escaped and balanced delimiters.

    The returned end offset is exclusive. Link titles and destinations with
    unescaped whitespace are deliberately outside this garden's small Markdown
    dialect; rejecting them is safer than guessing where a URL ends.
    """
    if start >= len(text) or text[start] != "[":
        return None

    index = start + 1
    label_depth = 1
    while index < len(text):
        char = text[index]
        if char == "\\" and index + 1 < len(text):
            index += 2
            continue
        if char == "[":
            label_depth += 1
        elif char == "]":
            label_depth -= 1
            if label_depth == 0:
                break
        index += 1
    if label_depth or index + 1 >= len(text) or text[index + 1] != "(":
        return None

    label = text[start + 1 : index]
    href_start = index + 2
    index = href_start
    href_depth = 1
    unescaped_whitespace = False
    while index < len(text):
        char = text[index]
        if char == "\\" and index + 1 < len(text):
            index += 2
            continue
        if char.isspace():
            unescaped_whitespace = True
        elif char == "(":
            href_depth += 1
        elif char == ")":
            href_depth -= 1
            if href_depth == 0:
                href = text[href_start:index]
                if not href or unescaped_whitespace:
                    return None
                return label, _markdown_unescape(href), index + 1
        index += 1
    return None


def iter_markdown_links(text: str):
    """Yield ``(label, href)`` pairs outside inline code spans."""
    index = 0
    while index < len(text):
        if text[index] == "\\" and index + 1 < len(text):
            index += 2
            continue
        if text[index] == "`":
            width = 1
            while index + width < len(text) and text[index + width] == "`":
                width += 1
            delimiter = "`" * width
            closing = text.find(delimiter, index + width)
            # An unmatched delimiter is literal text in the renderer. Advance
            # past those backticks and keep scanning so later links are exposed
            # to the checker exactly as they are rendered.
            index = index + width if closing < 0 else closing + width
            continue
        if text[index] == "[":
            parsed = _parse_markdown_link(text, index)
            if parsed is not None:
                label, href, end = parsed
                yield label, href
                index = end
                continue
        index += 1


def _find_unescaped(text: str, token: str, start: int) -> int:
    index = start
    while True:
        index = text.find(token, index)
        if index < 0:
            return -1
        backslashes = 0
        cursor = index - 1
        while cursor >= 0 and text[cursor] == "\\":
            backslashes += 1
            cursor -= 1
        if backslashes % 2 == 0:
            return index
        index += len(token)


def _plain_link_label(label: str) -> str:
    """Return a compact text alternative for a Markdown link label."""
    label = re.sub(r"`+([^`]*)`+", r"\1", label)
    label = re.sub(r"[*_]", "", label)
    return _markdown_unescape(label)


def _inline(text: str, rendered_slugs: set[str], *, allow_links: bool = True) -> str:
    """Render the garden's small inline-Markdown dialect without sentinels.

    Parsing first and escaping at the leaf avoids two old failure modes at
    once: URLs containing balanced parentheses are not truncated, and code
    spans nested inside link labels cannot leak placeholder control bytes.
    """
    out: list[str] = []
    index = 0
    while index < len(text):
        char = text[index]

        if char == "\\" and index + 1 < len(text) and text[index + 1] in MD_ESCAPABLE:
            out.append(html.escape(text[index + 1], quote=False))
            index += 2
            continue

        if char == "`":
            width = 1
            while index + width < len(text) and text[index + width] == "`":
                width += 1
            delimiter = "`" * width
            closing = text.find(delimiter, index + width)
            if closing >= 0:
                code = text[index + width : closing].replace("\n", " ")
                if len(code) >= 2 and code.startswith(" ") and code.endswith(" "):
                    code = code[1:-1]
                out.append("<code>%s</code>" % html.escape(code, quote=False))
                index = closing + width
                continue

        if allow_links and char == "[":
            parsed = _parse_markdown_link(text, index)
            if parsed is not None:
                label, href, end = parsed
                target = _local_room_slug(href)
                pending = target is not None and target not in rendered_slugs
                attrs = ""
                if pending:
                    aria = _plain_link_label(label) + " (room pending)"
                    attrs = ' class="pending" aria-label="%s"' % html.escape(
                        aria, quote=True
                    )
                out.append(
                    '<a href="%s"%s>%s</a>'
                    % (
                        html.escape(href, quote=True),
                        attrs,
                        _inline(label, rendered_slugs, allow_links=False),
                    )
                )
                index = end
                continue

        if text.startswith("**", index):
            closing = _find_unescaped(text, "**", index + 2)
            if closing >= 0:
                out.append(
                    "<strong>%s</strong>"
                    % _inline(
                        text[index + 2 : closing],
                        rendered_slugs,
                        allow_links=allow_links,
                    )
                )
                index = closing + 2
                continue

        if char == "*":
            closing = _find_unescaped(text, "*", index + 1)
            if closing >= 0:
                out.append(
                    "<em>%s</em>"
                    % _inline(
                        text[index + 1 : closing],
                        rendered_slugs,
                        allow_links=allow_links,
                    )
                )
                index = closing + 1
                continue

        out.append(html.escape(char, quote=False))
        index += 1

    return "".join(out)


def _is_table_separator(line: str) -> bool:
    cells = _split_table_row(line)
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", cell.strip()) for cell in cells)


def _split_table_row(line: str) -> list[str]:
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|"):
        line = line[:-1]
    return [cell.strip() for cell in re.split(r"(?<!\\)\|", line)]


def _is_block_start(lines: list[str], index: int) -> bool:
    stripped = lines[index].strip()
    if (
        stripped.startswith(("#", ">", "```"))
        or re.fullmatch(r"(-{3,}|\*{3,}|_{3,})", stripped)
        or re.match(r"[-*]\s+", stripped)
        or re.match(r"\d+\.\s+", stripped)
    ):
        return True
    return (
        "|" in stripped
        and index + 1 < len(lines)
        and _is_table_separator(lines[index + 1].strip())
    )


def _plain_heading_text(value: str, rendered_slugs: set[str]) -> str:
    """Reduce the supported inline Markdown in a heading to readable text."""
    rendered = _inline(value, rendered_slugs)
    return html.unescape(re.sub(r"<[^>]+>", "", rendered))


def md_to_html(
    md: str,
    rendered_slugs: set[str],
    outline: list[tuple[int, str, str]] | None = None,
) -> str:
    lines = md.splitlines()
    out: list[str] = []
    heading_counts: dict[str, int] = {}
    i = 0

    while i < len(lines):
        stripped = lines[i].strip()
        if not stripped:
            i += 1
            continue

        if stripped.startswith("```"):
            block: list[str] = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                block.append(lines[i])
                i += 1
            if i < len(lines):
                i += 1
            out.append(
                "<pre><code>%s</code></pre>"
                % html.escape("\n".join(block), quote=False)
            )
            continue

        if re.fullmatch(r"(-{3,}|\*{3,}|_{3,})", stripped):
            out.append("<hr>")
            i += 1
            continue

        heading = re.match(r"(#{1,6})\s+(.*)", stripped)
        if heading:
            level = len(heading.group(1))
            heading_text = heading.group(2)
            base_id = _slugify_heading(heading_text)
            heading_counts[base_id] = heading_counts.get(base_id, 0) + 1
            suffix = "" if heading_counts[base_id] == 1 else "-%d" % heading_counts[base_id]
            heading_id = base_id + suffix
            rendered_heading = _inline(heading_text, rendered_slugs)
            out.append(
                '<h%d id="%s">%s</h%d>'
                % (level, heading_id, rendered_heading, level)
            )
            if outline is not None and level in {2, 3}:
                outline.append(
                    (level, heading_id, _plain_heading_text(heading_text, rendered_slugs))
                )
            i += 1
            continue

        if stripped.startswith(">"):
            quote_lines: list[str] = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                quote_lines.append(re.sub(r"^\s*>\s?", "", lines[i]))
                i += 1
            out.append(
                "<blockquote>%s</blockquote>"
                % md_to_html("\n".join(quote_lines), rendered_slugs)
            )
            continue

        if (
            "|" in stripped
            and i + 1 < len(lines)
            and _is_table_separator(lines[i + 1].strip())
        ):
            headers = _split_table_row(stripped)
            i += 2
            rows: list[list[str]] = []
            while i < len(lines) and "|" in lines[i] and lines[i].strip():
                rows.append(_split_table_row(lines[i]))
                i += 1
            head = "".join(
                "<th>%s</th>" % _inline(cell, rendered_slugs)
                for cell in headers
            )
            body_rows = []
            for row in rows:
                padded = (row + [""] * len(headers))[: len(headers)]
                body_rows.append(
                    "<tr>%s</tr>"
                    % "".join(
                        "<td>%s</td>"
                        % _inline(cell, rendered_slugs)
                        for cell in padded
                    )
                )
            out.append(
                '<div class="garden-table-wrap"><table class="garden-table">'
                "<thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>"
                % (head, "".join(body_rows))
            )
            continue

        if re.match(r"[-*]\s+", stripped):
            items: list[str] = []
            while i < len(lines) and re.match(r"[-*]\s+", lines[i].strip()):
                item = re.sub(r"^[-*]\s+", "", lines[i].strip())
                i += 1
                while i < len(lines) and lines[i].startswith("  ") and lines[i].strip():
                    item += " " + lines[i].strip()
                    i += 1
                items.append(item)
            out.append(
                "<ul>%s</ul>"
                % "".join(
                    "<li>%s</li>"
                    % _inline(item, rendered_slugs)
                    for item in items
                )
            )
            continue

        if re.match(r"\d+\.\s+", stripped):
            items = []
            while i < len(lines) and re.match(r"\d+\.\s+", lines[i].strip()):
                item = re.sub(r"^\d+\.\s+", "", lines[i].strip())
                i += 1
                while i < len(lines) and lines[i].startswith("  ") and lines[i].strip():
                    item += " " + lines[i].strip()
                    i += 1
                items.append(item)
            out.append(
                "<ol>%s</ol>"
                % "".join(
                    "<li>%s</li>"
                    % _inline(item, rendered_slugs)
                    for item in items
                )
            )
            continue

        paragraph: list[str] = []
        while i < len(lines) and lines[i].strip() and not _is_block_start(lines, i):
            paragraph.append(lines[i].strip())
            i += 1
        if not paragraph:
            # Defensive progress for unusual Markdown that is not recognized above.
            paragraph.append(lines[i].strip())
            i += 1
        out.append(
            "<p>%s</p>"
            % _inline(" ".join(paragraph), rendered_slugs)
        )

    return "\n".join(out)


VOID_TAGS = {"meta", "link", "br", "hr", "img", "input", "source", "wbr"}


class BalanceChecker(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.stack: list[str] = []
        self.errors: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag not in VOID_TAGS:
            self.stack.append(tag)

    def handle_endtag(self, tag: str) -> None:
        if tag in VOID_TAGS:
            return
        if not self.stack:
            self.errors.append("stray closing </%s>" % tag)
        elif self.stack[-1] != tag:
            self.errors.append("mismatched </%s>, expected </%s>" % (tag, self.stack[-1]))
            self.stack.pop()
        else:
            self.stack.pop()


def check_well_formed(
    path: Path,
    *,
    expected_corridors: list[str] | None = None,
    expected_visual_count: int | None = None,
) -> list[str]:
    checker = BalanceChecker()
    try:
        source = path.read_text(encoding="utf-8")
        controls = sorted(set(re.findall(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]", source)))
        if controls:
            checker.errors.append(
                "forbidden control character(s): "
                + ", ".join("0x%02x" % ord(value) for value in controls)
            )
        toc_targets = re.findall(
            r'<li class="level-[23]"><a href="#([^"]+)">', source
        )
        if 'data-garden-room="' in source:
            outline_ids = re.findall(r'<h[23] id="([^"]+)">', source)
            if len(outline_ids) != len(set(outline_ids)):
                checker.errors.append("duplicate H2/H3 id in room outline")
            if sorted(toc_targets) != sorted(outline_ids * 2):
                checker.errors.append("desktop/mobile room navigation does not match H2/H3 outline")
            corridor_count = re.search(
                r'<nav class="garden-corridors"[^>]*data-corridor-count="(\d+)"',
                source,
            )
            corridor_targets = re.findall(
                r'<a class="garden-corridor" href="([^"]+)">', source
            )
            expected_corridor_count = (
                int(corridor_count.group(1)) if corridor_count else 0
            )
            if not corridor_count:
                checker.errors.append("room is missing its corridor navigation")
            elif len(corridor_targets) != expected_corridor_count:
                checker.errors.append("corridor count does not match rendered links")
            if len(corridor_targets) != len(set(corridor_targets)):
                checker.errors.append("duplicate room target in corridor navigation")
            if (
                expected_corridors is not None
                and corridor_targets != expected_corridors
            ):
                checker.errors.append(
                    "corridor navigation does not match source terms_linked order"
                )
            for target in corridor_targets:
                if not (path.parent / target).is_file():
                    checker.errors.append("corridor target does not exist: %s" % target)
            if source.count('<figure class="garden-series-plate ') != 1:
                checker.errors.append("room must contain exactly one series artwork")
            rendered_visual_count = source.count('<figure class="garden-visual ')
            if (
                expected_visual_count is not None
                and rendered_visual_count != expected_visual_count
            ):
                checker.errors.append(
                    "room teaching visual count is %d; expected %d"
                    % (rendered_visual_count, expected_visual_count)
                )
            image_targets = re.findall(
                r'<img src="(assets/series/[^"]+\.png)"', source
            )
            webp_targets = re.findall(
                r'<source srcset="(assets/series/[^"]+\.webp)"', source
            )
            if len(image_targets) != 1:
                checker.errors.append("room must reference exactly one series image")
            if len(webp_targets) != 1:
                checker.errors.append("room must reference exactly one optimized series image")
            for target in image_targets:
                if not (path.parent / target).is_file():
                    checker.errors.append("series artwork does not exist: %s" % target)
            for target in webp_targets:
                if not (path.parent / target).is_file():
                    checker.errors.append("optimized series artwork does not exist: %s" % target)
        elif 'class="garden-index-layout"' in source:
            outline_ids = re.findall(
                r'<section class="garden-series" id="([^"]+)">', source
            )
            if len(outline_ids) != len(set(outline_ids)):
                checker.errors.append("duplicate series id in garden index")
            if sorted(toc_targets) != sorted(outline_ids * 2):
                checker.errors.append("desktop/mobile index navigation does not match series outline")
            if source.count('class="garden-series-card"') != len(SERIES):
                checker.errors.append("garden index must contain one visual card per series")
            image_targets = re.findall(
                r'<img src="(assets/series/[^"]+\.png)"', source
            )
            webp_targets = re.findall(
                r'<source srcset="(assets/series/[^"]+\.webp)"', source
            )
            if len(image_targets) != len(SERIES):
                checker.errors.append("garden index series artwork count is wrong")
            if len(webp_targets) != len(SERIES):
                checker.errors.append("garden index optimized artwork count is wrong")
            for target in image_targets:
                if not (path.parent / target).is_file():
                    checker.errors.append("series artwork does not exist: %s" % target)
            for target in webp_targets:
                if not (path.parent / target).is_file():
                    checker.errors.append("optimized series artwork does not exist: %s" % target)
        checker.feed(source)
        checker.close()
    except Exception as exc:  # HTMLParser errors should become build evidence.
        checker.errors.append(str(exc))
    if checker.stack:
        checker.errors.append("unclosed tags: " + ", ".join(checker.stack))
    return checker.errors


def display_date(value: str) -> str:
    try:
        parsed = date.fromisoformat(value)
        return "%d %s %d" % (parsed.day, parsed.strftime("%B"), parsed.year)
    except ValueError:
        return value


def strip_source_title(body: str) -> str:
    """The source contract includes an H1; the page chrome already supplies it."""
    return re.sub(r"\A\s*#\s+[^\n]+\n+", "", body, count=1)


def load_rooms() -> tuple[list[dict[str, str]], list[str]]:
    rooms: list[dict[str, str]] = []
    skipped: list[str] = []
    seen: set[str] = set()
    for path in sorted(SOURCE_DIR.glob("*.md")):
        try:
            meta, body = parse_front_matter(path.read_text(encoding="utf-8"))
            missing = sorted(REQUIRED_META - set(meta))
            if missing:
                raise ValueError("missing keys: " + ", ".join(missing))
            slug = meta["slug"]
            if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug):
                raise ValueError("slug is not URL-safe: %s" % slug)
            if slug != path.stem:
                raise ValueError("slug %s does not match filename" % slug)
            if slug in seen:
                raise ValueError("duplicate slug: %s" % slug)
            if meta["series"] not in SERIES_NAMES:
                raise ValueError("unknown series: %s" % meta["series"])
            date.fromisoformat(meta["date"])
            if meta["status"].lower() not in {"draft", "published", "forthcoming"}:
                raise ValueError("unknown status: %s" % meta["status"])
            seen.add(slug)
            rooms.append({**meta, "body": strip_source_title(body), "path": str(path)})
        except (OSError, UnicodeError, ValueError) as exc:
            skipped.append("%s: %s" % (path.name, exc))
    return rooms, skipped


def ordered_series_rooms(series_slug: str, rooms: dict[str, dict[str, str]]) -> list[str]:
    canonical = [slug for slug in SERIES_ORDER[series_slug] if slug in rooms]
    extras = sorted(
        slug
        for slug, room in rooms.items()
        if room["series"] == series_slug and slug not in SERIES_ORDER[series_slug]
    )
    return canonical + extras


def rendered_room_slugs(rooms: dict[str, dict[str, str]]) -> set[str]:
    return {
        slug
        for slug, room in rooms.items()
        if room["status"].lower() != "forthcoming"
    }


def _png_dimensions(path: Path) -> tuple[int, int]:
    header = path.read_bytes()[:24]
    if len(header) < 24 or header[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("not a PNG")
    return struct.unpack(">II", header[16:24])


def _webp_dimensions(path: Path) -> tuple[int, int]:
    data = path.read_bytes()
    if len(data) < 20 or data[:4] != b"RIFF" or data[8:12] != b"WEBP":
        raise ValueError("not a WebP image")
    declared_size = struct.unpack("<I", data[4:8])[0] + 8
    if declared_size != len(data):
        raise ValueError("WebP RIFF length does not match file size")
    offset = 12
    dimensions: tuple[int, int] | None = None
    while offset + 8 <= len(data):
        chunk_type = data[offset : offset + 4]
        chunk_size = struct.unpack("<I", data[offset + 4 : offset + 8])[0]
        payload_start = offset + 8
        payload_end = payload_start + chunk_size
        if payload_end > len(data):
            raise ValueError("truncated WebP chunk")
        payload = data[payload_start:payload_end]
        if chunk_type == b"VP8X" and len(payload) >= 10:
            dimensions = (
                int.from_bytes(payload[4:7], "little") + 1,
                int.from_bytes(payload[7:10], "little") + 1,
            )
        elif chunk_type == b"VP8L" and len(payload) >= 5 and payload[0] == 0x2F:
            bits = int.from_bytes(payload[1:5], "little")
            dimensions = ((bits & 0x3FFF) + 1, ((bits >> 14) & 0x3FFF) + 1)
        elif (
            chunk_type == b"VP8 "
            and len(payload) >= 10
            and payload[3:6] == b"\x9d\x01\x2a"
        ):
            dimensions = (
                struct.unpack("<H", payload[6:8])[0] & 0x3FFF,
                struct.unpack("<H", payload[8:10])[0] & 0x3FFF,
            )
        offset = payload_end + (chunk_size & 1)
    if offset != len(data):
        raise ValueError("malformed WebP chunk padding")
    if dimensions is None or dimensions[0] < 1 or dimensions[1] < 1:
        raise ValueError("WebP dimensions not found")
    return dimensions


def _sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_visual_catalog(
    rooms: dict[str, dict[str, str]],
) -> tuple[dict[str, object], list[str]]:
    """Load and validate evidence-bound visual specs plus series artwork."""
    catalog: dict[str, object] = {"art": {}, "rooms": {}}
    art_catalog: dict[str, dict[str, object]] = catalog["art"]  # type: ignore[assignment]
    room_catalog: dict[str, dict[str, object]] = catalog["rooms"]  # type: ignore[assignment]
    errors: list[str] = []
    available_slugs = rendered_room_slugs(rooms)

    for series_slug, _, canonical_slugs in SERIES:
        spec_path = VISUAL_SPECS_DIR / (series_slug + ".json")
        if not spec_path.is_file():
            errors.append("missing visual spec: %s" % spec_path.relative_to(ROOT))
            continue
        try:
            data = json.loads(spec_path.read_text(encoding="utf-8"))
        except (OSError, UnicodeError, json.JSONDecodeError) as exc:
            errors.append("%s: %s" % (spec_path.relative_to(ROOT), exc))
            continue
        if not isinstance(data, dict):
            errors.append("%s: root must be an object" % spec_path.relative_to(ROOT))
            continue
        if data.get("schema") != VISUAL_SCHEMA:
            errors.append("%s: wrong visual schema" % spec_path.relative_to(ROOT))
        if data.get("series") != series_slug:
            errors.append("%s: series does not match filename" % spec_path.relative_to(ROOT))

        art = data.get("art")
        expected_art_src = "assets/series/%s.png" % series_slug
        if not isinstance(art, dict):
            errors.append("%s: art must be an object" % spec_path.relative_to(ROOT))
        else:
            art_error_count = len(errors)
            src = art.get("src")
            alt = art.get("alt")
            prompt = art.get("prompt")
            png_sha256 = art.get("png_sha256")
            webp_sha256 = art.get("webp_sha256")
            if src != expected_art_src:
                errors.append("%s: art.src must be %s" % (spec_path.name, expected_art_src))
            if not isinstance(alt, str) or not alt.strip():
                errors.append("%s: art.alt must be nonempty" % spec_path.name)
            if not isinstance(prompt, str) or not prompt.strip():
                errors.append("%s: art.prompt must be nonempty" % spec_path.name)
            for field, value in (
                ("png_sha256", png_sha256),
                ("webp_sha256", webp_sha256),
            ):
                if not isinstance(value, str) or not re.fullmatch(
                    r"[0-9a-f]{64}", value
                ):
                    errors.append(
                        "%s: art.%s must be 64 lowercase hex characters"
                        % (spec_path.name, field)
                    )
            source_path = VISUAL_ASSETS_DIR / "series" / (series_slug + ".png")
            webp_source_path = VISUAL_ASSETS_DIR / "series" / (series_slug + ".webp")
            dimensions = (0, 0)
            if not source_path.is_file():
                errors.append("missing series artwork: %s" % source_path.relative_to(ROOT))
            else:
                try:
                    dimensions = _png_dimensions(source_path)
                    if dimensions[0] < 1000 or dimensions[1] < 500:
                        errors.append(
                            "%s: artwork is too small (%dx%d)"
                            % (source_path.relative_to(ROOT), *dimensions)
                        )
                    if (
                        isinstance(png_sha256, str)
                        and _sha256_file(source_path) != png_sha256
                    ):
                        errors.append(
                            "%s: PNG digest does not match manifest"
                            % source_path.relative_to(ROOT)
                        )
                except (OSError, ValueError) as exc:
                    errors.append("%s: %s" % (source_path.relative_to(ROOT), exc))
            if not webp_source_path.is_file():
                errors.append(
                    "missing optimized series artwork: %s"
                    % webp_source_path.relative_to(ROOT)
                )
            else:
                try:
                    webp_dimensions = _webp_dimensions(webp_source_path)
                    if webp_dimensions != dimensions:
                        errors.append(
                            "%s: dimensions %dx%d do not match PNG %dx%d"
                            % (
                                webp_source_path.relative_to(ROOT),
                                *webp_dimensions,
                                *dimensions,
                            )
                        )
                    if (
                        isinstance(webp_sha256, str)
                        and _sha256_file(webp_source_path) != webp_sha256
                    ):
                        errors.append(
                            "%s: WebP digest does not match manifest"
                            % webp_source_path.relative_to(ROOT)
                        )
                    if source_path.is_file() and webp_source_path.stat().st_size >= source_path.stat().st_size:
                        errors.append(
                            "%s: optimized artwork is not smaller than its PNG"
                            % webp_source_path.relative_to(ROOT)
                        )
                except (OSError, ValueError) as exc:
                    errors.append("%s: %s" % (webp_source_path.relative_to(ROOT), exc))
            if (
                len(errors) == art_error_count
                and src == expected_art_src
                and isinstance(alt, str)
                and isinstance(prompt, str)
                and isinstance(png_sha256, str)
                and isinstance(webp_sha256, str)
            ):
                art_catalog[series_slug] = {
                    "src": expected_art_src,
                    "alt": alt.strip(),
                    "prompt": prompt.strip(),
                    "source_path": source_path,
                    "webp_src": "assets/series/%s.webp" % series_slug,
                    "webp_source_path": webp_source_path,
                    "dimensions": dimensions,
                }

        visual_rooms = data.get("rooms")
        if not isinstance(visual_rooms, dict):
            errors.append("%s: rooms must be an object" % spec_path.relative_to(ROOT))
            continue
        expected_rooms = {
            slug for slug in canonical_slugs if slug in rooms and slug in available_slugs
        }
        missing_rooms = sorted(expected_rooms - set(visual_rooms))
        extra_rooms = sorted(set(visual_rooms) - expected_rooms)
        if missing_rooms:
            errors.append("%s: missing rooms: %s" % (spec_path.name, ", ".join(missing_rooms)))
        if extra_rooms:
            errors.append("%s: unexpected rooms: %s" % (spec_path.name, ", ".join(extra_rooms)))

        for room_slug in sorted(expected_rooms & set(visual_rooms)):
            room_entry = visual_rooms[room_slug]
            location = "%s:%s" % (spec_path.name, room_slug)
            if not isinstance(room_entry, dict):
                errors.append("%s: room entry must be an object" % location)
                continue
            visuals = room_entry.get("visuals")
            if not isinstance(visuals, list) or not 3 <= len(visuals) <= 5:
                errors.append("%s: three to five visuals are required" % location)
                continue
            outline: list[tuple[int, str, str]] = []
            md_to_html(rooms[room_slug]["body"], available_slugs, outline)
            heading_ids = {heading_id for _, heading_id, _ in outline}
            heading_titles = {
                heading_id: heading_title for _, heading_id, heading_title in outline
            }
            after_ids: list[str] = []
            valid_visuals: list[dict[str, object]] = []
            for visual_index, visual in enumerate(visuals, 1):
                visual_location = "%s:visual-%d" % (location, visual_index)
                if not isinstance(visual, dict):
                    errors.append("%s: visual must be an object" % visual_location)
                    continue
                visual_error_count = len(errors)
                after = visual.get("after")
                kind = visual.get("kind")
                claim_scope = visual.get("claim_scope", "section-synthesis")
                if not isinstance(after, str) or after not in heading_ids:
                    errors.append("%s: after does not match an H2/H3 id" % visual_location)
                else:
                    after_ids.append(after)
                if kind not in VISUAL_KINDS:
                    errors.append("%s: unknown kind %r" % (visual_location, kind))
                if claim_scope not in VISUAL_CLAIM_SCOPES:
                    errors.append(
                        "%s: unknown claim_scope %r" % (visual_location, claim_scope)
                    )
                evidence_sections_value = visual.get("evidence_sections")
                evidence_sections: list[str] = []
                if claim_scope == "section-synthesis":
                    if evidence_sections_value is not None:
                        errors.append(
                            "%s: section-synthesis derives evidence from after; "
                            "remove evidence_sections" % visual_location
                        )
                    if isinstance(after, str) and after in heading_ids:
                        evidence_sections = [after]
                elif claim_scope == "room-synthesis":
                    if (
                        not isinstance(evidence_sections_value, list)
                        or not 2 <= len(evidence_sections_value) <= 8
                        or not all(isinstance(value, str) for value in evidence_sections_value)
                    ):
                        errors.append(
                            "%s: room-synthesis requires 2–8 evidence_sections"
                            % visual_location
                        )
                    else:
                        evidence_sections = [str(value) for value in evidence_sections_value]
                        if len(evidence_sections) != len(set(evidence_sections)):
                            errors.append(
                                "%s: evidence_sections must be unique" % visual_location
                            )
                        unknown_sections = sorted(set(evidence_sections) - heading_ids)
                        if unknown_sections:
                            errors.append(
                                "%s: unknown evidence_sections: %s"
                                % (visual_location, ", ".join(unknown_sections))
                            )
                for field in ("kicker", "title", "caption"):
                    value = visual.get(field)
                    if not isinstance(value, str) or not value.strip():
                        errors.append("%s: %s must be nonempty" % (visual_location, field))
                as_of = visual.get("as_of")
                if as_of is not None and (
                    not isinstance(as_of, str) or not as_of.strip()
                ):
                    errors.append("%s: as_of must be nonempty text" % visual_location)
                items = visual.get("items")
                if not isinstance(items, list) or not 3 <= len(items) <= 6:
                    errors.append("%s: items must contain 3–6 entries" % visual_location)
                else:
                    labels: list[str] = []
                    for item_index, item in enumerate(items, 1):
                        item_location = "%s:item-%d" % (visual_location, item_index)
                        if not isinstance(item, dict):
                            errors.append("%s: item must be an object" % item_location)
                            continue
                        for field in ("label", "detail"):
                            value = item.get(field)
                            if not isinstance(value, str) or not value.strip():
                                errors.append("%s: %s must be nonempty" % (item_location, field))
                        label = item.get("label")
                        if isinstance(label, str):
                            labels.append(label.strip())
                        meta = item.get("meta", "")
                        if not isinstance(meta, str):
                            errors.append("%s: meta must be text" % item_location)
                    if len(labels) != len(set(labels)):
                        errors.append("%s: item labels must be unique" % visual_location)
                if len(errors) == visual_error_count:
                    validated_visual = dict(visual)
                    validated_visual["evidence_heading"] = heading_titles[str(after)]
                    validated_visual["_claim_scope"] = claim_scope
                    validated_visual["_evidence_sections"] = evidence_sections
                    validated_visual["_evidence_titles"] = [
                        heading_titles[heading_id] for heading_id in evidence_sections
                    ]
                    valid_visuals.append(validated_visual)
            if len(after_ids) != len(set(after_ids)):
                errors.append("%s: visuals must use different insertion headings" % location)
            if (
                3 <= len(valid_visuals) <= 5
                and len(after_ids) == len(set(after_ids))
            ):
                heading_positions = {
                    heading_id: position
                    for position, (_, heading_id, _) in enumerate(outline)
                }
                valid_visuals.sort(
                    key=lambda item: heading_positions[str(item["after"])]
                )
                room_catalog[room_slug] = {
                    "series": series_slug,
                    "visuals": valid_visuals,
                }

    return catalog, errors


def copy_visual_assets(catalog: dict[str, object]) -> None:
    art_catalog: dict[str, dict[str, object]] = catalog["art"]  # type: ignore[assignment]
    for series_slug, art in art_catalog.items():
        source_path = art["source_path"]
        destination = OUTPUT_DIR / "assets" / "series" / (series_slug + ".png")
        if isinstance(source_path, Path) and source_path.is_file():
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source_path, destination)
        webp_source_path = art["webp_source_path"]
        webp_destination = OUTPUT_DIR / "assets" / "series" / (series_slug + ".webp")
        if isinstance(webp_source_path, Path) and webp_source_path.is_file():
            webp_destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(webp_source_path, webp_destination)


def room_navigation(room: dict[str, str], rooms: dict[str, dict[str, str]]) -> str:
    order = [
        slug
        for slug in ordered_series_rooms(room["series"], rooms)
        if rooms[slug]["status"].lower() != "forthcoming"
    ]
    position = order.index(room["slug"])
    previous = rooms[order[position - 1]] if position else None
    following = rooms[order[position + 1]] if position + 1 < len(order) else None
    links = []
    if previous:
        links.append(
            '<a class="previous" href="%s.html">← %s</a>'
            % (previous["slug"], html.escape(previous["title"], quote=False))
        )
    if following:
        links.append(
            '<a class="next" href="%s.html">%s →</a>'
            % (following["slug"], html.escape(following["title"], quote=False))
        )
    return '<nav class="garden-nav" aria-label="Rooms">%s</nav>' % "".join(links)


def _corridor_label(title: str) -> str:
    """Remove front-matter quote wrappers without shortening the room title."""
    title = title.strip()
    if len(title) >= 2 and title[0] == title[-1] and title[0] in {'"', "'"}:
        return title[1:-1]
    return title


def corridor_navigation(room: dict[str, str], rooms: dict[str, dict[str, str]]) -> str:
    links: list[str] = []
    seen = {room["slug"]}
    for value in room["terms_linked"].split(","):
        slug = value.strip()
        target = rooms.get(slug)
        if (
            not slug
            or slug in seen
            or target is None
            or target["status"].lower() == "forthcoming"
        ):
            continue
        seen.add(slug)
        label = _corridor_label(target["title"])
        links.append(
            '<li><a class="garden-corridor" href="%s.html">%s</a></li>'
            % (html.escape(slug, quote=True), html.escape(label, quote=False))
        )
    return (
        '<nav class="garden-corridors" aria-label="Explore connected rooms" '
        'data-corridor-count="%d"><ul class="garden-corridor-list">%s</ul></nav>'
        % (len(links), "".join(links))
    )


def render_series_plate(room: dict[str, str], catalog: dict[str, object]) -> str:
    art_catalog: dict[str, dict[str, object]] = catalog["art"]  # type: ignore[assignment]
    art = art_catalog.get(room["series"])
    if art is None:
        return ""
    width, height = art.get("dimensions", (0, 0))
    terms = [
        value.strip()
        for value in room["terms_defined"].split(",")
        if value.strip()
    ][:4]
    return """<figure class="garden-series-plate garden-series-plate--{series}">
<div class="garden-series-plate-media"><picture><source srcset="{webp_src}" type="image/webp"><img src="{src}" alt="{alt}" width="{width}" height="{height}" loading="eager" decoding="async"></picture></div>
<figcaption><span class="garden-series-plate-kicker">Visual field</span><strong>{series_name}</strong><span class="garden-series-plate-terms">{terms}</span></figcaption>
</figure>""".format(
        series=html.escape(room["series"], quote=True),
        src=html.escape(str(art["src"]), quote=True),
        webp_src=html.escape(str(art["webp_src"]), quote=True),
        alt=html.escape(str(art["alt"]), quote=True),
        width=int(width),
        height=int(height),
        series_name=html.escape(SERIES_NAMES[room["series"]], quote=False),
        terms=" · ".join(html.escape(term, quote=False) for term in terms),
    )


def render_teaching_visual(
    room_slug: str, visual_index: int, visual: dict[str, object]
) -> str:
    visual_id = "visual-%s-%d" % (room_slug, visual_index)
    kind = str(visual.get("kind", "contrast"))
    list_tag = "ol" if kind in {"sequence", "layers", "timeline"} else "ul"
    as_of = str(visual.get("as_of", "")).strip()
    as_of_html = (
        '<p class="garden-visual-as-of">As of %s</p>'
        % html.escape(as_of, quote=False)
        if as_of
        else ""
    )
    after = str(visual.get("after", ""))
    claim_scope = str(visual.get("_claim_scope", "section-synthesis"))
    evidence_sections = visual.get("_evidence_sections", [after])
    evidence_titles = visual.get(
        "_evidence_titles", [str(visual.get("evidence_heading", after))]
    )
    evidence_links: list[str] = []
    if isinstance(evidence_sections, list) and isinstance(evidence_titles, list):
        for heading_id, heading_title in zip(evidence_sections, evidence_titles):
            evidence_links.append(
                '<a href="#%s">%s</a>'
                % (
                    html.escape(str(heading_id), quote=True),
                    html.escape(str(heading_title), quote=False),
                )
            )
    evidence_prefix = "Drawn across" if claim_scope == "room-synthesis" else "Drawn from"
    evidence_html = (
        '<span class="garden-visual-evidence">%s: %s</span>'
        % (evidence_prefix, " · ".join(evidence_links))
    )
    items_html: list[str] = []
    items = visual.get("items", [])
    if isinstance(items, list):
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = str(item.get("meta", "")).strip()
            meta_html = (
                '<span class="garden-visual-item-meta">%s</span>'
                % html.escape(meta, quote=False)
                if meta
                else ""
            )
            items_html.append(
                """<li class="garden-visual-item">{meta}<strong class="garden-visual-item-label">{label}</strong><span class="garden-visual-item-detail">{detail}</span></li>""".format(
                    meta=meta_html,
                    label=html.escape(str(item.get("label", "")), quote=False),
                    detail=html.escape(str(item.get("detail", "")), quote=False),
                )
            )
    return """<figure class="garden-visual garden-visual--{kind}" aria-labelledby="{visual_id}" data-claim-scope="{claim_scope}" data-placement-heading="{after}" data-evidence-headings="{evidence_headings}">
<div class="garden-visual-head"><p class="garden-visual-kicker">{kicker}</p><p class="garden-visual-title" id="{visual_id}">{title}</p>{as_of}</div>
<{list_tag} class="garden-visual-items" role="list">{items}</{list_tag}>
<figcaption class="garden-visual-caption"><span>{caption}</span>{evidence}</figcaption>
</figure>""".format(
        kind=html.escape(kind, quote=True),
        visual_id=html.escape(visual_id, quote=True),
        claim_scope=html.escape(claim_scope, quote=True),
        after=html.escape(after, quote=True),
        evidence_headings=html.escape(
            " ".join(str(value) for value in evidence_sections), quote=True
        )
        if isinstance(evidence_sections, list)
        else "",
        evidence=evidence_html,
        kicker=html.escape(str(visual.get("kicker", "")), quote=False),
        title=html.escape(str(visual.get("title", "")), quote=False),
        as_of=as_of_html,
        list_tag=list_tag,
        items="".join(items_html),
        caption=html.escape(str(visual.get("caption", "")), quote=False),
    )


def inject_room_visuals(
    body_html: str, room_slug: str, visuals: list[dict[str, object]]
) -> str:
    for visual_index, visual in enumerate(visuals, 1):
        after = str(visual["after"])
        pattern = re.compile(
            r'(<h[23] id="%s">.*?</h[23]>)' % re.escape(after), re.DOTALL
        )
        rendered = render_teaching_visual(room_slug, visual_index, visual)
        body_html, count = pattern.subn(
            lambda match: match.group(1) + "\n" + rendered,
            body_html,
            count=1,
        )
        if count != 1:
            raise ValueError(
                "%s: visual insertion heading not found: %s" % (room_slug, after)
            )
    return body_html


def render_series_gallery(catalog: dict[str, object]) -> str:
    art_catalog: dict[str, dict[str, object]] = catalog["art"]  # type: ignore[assignment]
    cards: list[str] = []
    for series_slug, series_name, _ in SERIES:
        art = art_catalog.get(series_slug)
        if art is None:
            continue
        width, height = art.get("dimensions", (0, 0))
        cards.append(
            """<a class="garden-series-card" href="#{series}"><picture><source srcset="{webp_src}" type="image/webp"><img src="{src}" alt="" width="{width}" height="{height}" loading="lazy" decoding="async"></picture><span>{name}</span></a>""".format(
                series=html.escape(series_slug, quote=True),
                src=html.escape(str(art["src"]), quote=True),
                webp_src=html.escape(str(art["webp_src"]), quote=True),
                width=int(width),
                height=int(height),
                name=html.escape(series_name, quote=False),
            )
        )
    return (
        '<nav class="garden-series-gallery" aria-label="Explore the seven series">%s</nav>'
        % "".join(cards)
    )


def toc_list(outline: list[tuple[int, str, str]]) -> str:
    items = ['<ol class="garden-toc-list">']
    h2_open = False
    sublist_open = False
    for level, heading_id, label in outline:
        link = '<a href="#%s">%s</a>' % (
            html.escape(heading_id, quote=True),
            html.escape(label, quote=False),
        )
        if level == 2:
            if sublist_open:
                items.append("</ol>")
                sublist_open = False
            if h2_open:
                items.append("</li>")
            items.append('<li class="level-2">%s' % link)
            h2_open = True
        elif h2_open:
            if not sublist_open:
                items.append('<ol class="garden-toc-sublist">')
                sublist_open = True
            items.append('<li class="level-3">%s</li>' % link)
        else:
            # Keep an orphaned H3 navigable even when no H2 precedes it.
            items.append('<li class="level-3">%s</li>' % link)
    if sublist_open:
        items.append("</ol>")
    if h2_open:
        items.append("</li>")
    items.append("</ol>")
    return "".join(items)


def sidebar_toc(
    outline: list[tuple[int, str, str]], title: str = "In this room"
) -> str:
    safe_text = html.escape(title, quote=False)
    safe_attribute = html.escape(title, quote=True)
    return (
        '<aside class="garden-toc" aria-label="%s">'
        '<nav aria-label="Page sections"><p class="garden-toc-title">%s</p>%s</nav>'
        "</aside>"
    ) % (safe_attribute, safe_text, toc_list(outline))


def inline_toc(
    outline: list[tuple[int, str, str]], title: str = "In this room"
) -> str:
    return (
        '<details class="garden-toc-inline">'
        '<summary>%s</summary>%s</details>'
    ) % (html.escape(title, quote=False), toc_list(outline))


def garden_base(*, title: str, description: str, content: str) -> str:
    page = render(
        template("base.html"),
        title=html.escape(title, quote=False),
        description=html.escape(description, quote=True),
        root="../",
        content=content,
    )
    page = page.replace(
        "Theme memory — the only JavaScript on this site. No analytics, no trackers.",
        "Theme memory. No analytics, no trackers.",
        1,
    )
    page = page.replace("</head>", GARDEN_STYLES + "\n</head>", 1)
    page = page.replace("<body>", '<body class="garden-page-body">', 1)
    page = page.replace(
        '<a href="../about.html">About</a>',
        '<a href="index.html">Garden</a>\n    <a href="../about.html">About</a>',
        1,
    )
    page = page.replace("</body>", GARDEN_SCROLLSPY + "\n</body>", 1)
    return page


def build_room(
    room: dict[str, str],
    rooms: dict[str, dict[str, str]],
    visual_catalog: dict[str, object],
) -> str:
    series_name = SERIES_NAMES[room["series"]]
    status = room["status"].lower()
    status_label = " · Draft" if status == "draft" else ""
    tags = [tag.strip() for tag in room["tags"].split(",") if tag.strip()]
    tags_html = " · ".join(html.escape(tag, quote=False) for tag in tags)
    available_slugs = rendered_room_slugs(rooms)
    outline: list[tuple[int, str, str]] = []
    body_html = md_to_html(room["body"], available_slugs, outline)
    room_visual_catalog: dict[str, dict[str, object]] = visual_catalog["rooms"]  # type: ignore[assignment]
    room_visuals = room_visual_catalog.get(room["slug"], {}).get("visuals", [])
    if isinstance(room_visuals, list):
        body_html = inject_room_visuals(body_html, room["slug"], room_visuals)
    content = """<div class="garden-layout">
<article data-garden-room="{slug}" data-garden-outline>
<p class="garden-series-link"><a href="index.html#{series_slug}">{series_name}</a></p>
<p class="article-meta">{date}{status}</p>
<h1 class="article-title">{title}</h1>
{banner}
<p class="garden-lede">{summary}</p>
{corridors}
{series_plate}
{inline_toc}
{body}
<p class="garden-tags"><strong>Topics:</strong> {tags}</p>
{navigation}
</article>
{sidebar_toc}
</div>""".format(
        slug=html.escape(room["slug"], quote=True),
        series_slug=room["series"],
        series_name=html.escape(series_name, quote=False),
        date=html.escape(display_date(room["date"]), quote=False),
        status=status_label,
        title=html.escape(room["title"], quote=False),
        banner=DRAFT_BANNER if status == "draft" else "",
        summary=_inline(room["summary"], available_slugs),
        corridors=corridor_navigation(room, rooms),
        series_plate=render_series_plate(room, visual_catalog),
        inline_toc=inline_toc(outline),
        body=body_html,
        tags=tags_html,
        navigation=room_navigation(room, rooms),
        sidebar_toc=sidebar_toc(outline),
    )
    return garden_base(
        title="%s · %s Garden" % (room["title"], SITE_NAME),
        description=room["summary"] or SITE_TAGLINE,
        content=content,
    )


def build_index(
    rooms: dict[str, dict[str, str]], visual_catalog: dict[str, object]
) -> str:
    sections: list[str] = []
    available_slugs = rendered_room_slugs(rooms)
    for series_slug, series_name, _ in SERIES:
        items: list[str] = []
        for slug in ordered_series_rooms(series_slug, rooms):
            room = rooms[slug]
            status = room["status"].lower()
            if status == "forthcoming":
                title = html.escape(room["title"], quote=False)
                badge = '<span class="badge-draft">Forthcoming</span>'
            else:
                title = '<a href="%s.html">%s</a>' % (
                    slug,
                    html.escape(room["title"], quote=False),
                )
                badge = (
                    '<span class="badge-draft">Draft</span>' if status == "draft" else ""
                )
            items.append(
                """<li>
<div class="garden-room-title">{title}{badge}</div>
<p class="garden-room-summary">{summary}</p>
</li>""".format(
                    title=title,
                    badge=badge,
                    summary=_inline(room["summary"], available_slugs),
                )
            )
        empty = "<li><p class=\"garden-room-summary\">Rooms are still being planted.</p></li>"
        sections.append(
            '<section class="garden-series" id="%s"><h2>%s</h2><ul class="garden-room-list">%s</ul></section>'
            % (series_slug, html.escape(series_name, quote=False), "\n".join(items) or empty)
        )

    outline = [(2, series_slug, series_name) for series_slug, series_name, _ in SERIES]
    content = """<div class="garden-index-layout">
<div class="garden-index-main" data-garden-outline>
<div class="garden-intro">
<p class="hero-kicker">The knowledge garden</p>
<h1 class="article-title">Rooms connected by ideas</h1>
<p class="standfirst">Each room teaches one subject from the ground up. Links are corridors: follow one whenever a term needs its own room. Every room begins as a draft and becomes published only after its claims, voice, and sources survive review.</p>
</div>
{series_gallery}
{inline_toc}
{sections}
</div>
{sidebar_toc}
</div>""".format(
        series_gallery=render_series_gallery(visual_catalog),
        inline_toc=inline_toc(outline, "Series"),
        sections="\n".join(sections),
        sidebar_toc=sidebar_toc(outline, "Series"),
    )
    return garden_base(
        title="The Knowledge Garden · %s" % SITE_NAME,
        description="Darshan's knowledge garden: connected, sourced rooms for learning from first principles.",
        content=content,
    )


def prune_stale(expected_names: set[str]) -> None:
    if not OUTPUT_DIR.exists():
        return
    for path in OUTPUT_DIR.glob("*.html"):
        if path.name == "index.html" or path.name in expected_names:
            continue
        try:
            source = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            print("KEEP  garden/%s: cannot prove generated ownership: %s" % (path.name, exc))
            continue
        generated = 'data-garden-room="' in source or (
            '<p class="garden-series-link">' in source
            and '<nav class="garden-nav" aria-label="Rooms">' in source
        )
        if generated:
            path.unlink()
            print("pruned stale output: garden/%s" % path.name)


def build(strict: bool = False) -> int:
    rooms_list, skipped = load_rooms()
    rooms = {room["slug"]: room for room in rooms_list}
    missing = sorted(EXPECTED_SLUGS - set(rooms))

    for reason in skipped:
        print("SKIP  garden_src/%s" % reason)
    if missing:
        print("missing canonical room(s): %s" % ", ".join(missing))

    visual_catalog, visual_errors = load_visual_catalog(rooms)
    for error in visual_errors:
        print("VISUAL  %s" % error)
    if visual_errors:
        print(
            "\n0 pages written, 0 parse failures; %d room sources, 0 pending links, "
            "%d skipped sources, %d visual errors."
            % (len(rooms), len(skipped), len(visual_errors))
        )
        return 1

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    copy_visual_assets(visual_catalog)
    written: list[Path] = []
    for series_slug, _, _ in SERIES:
        for slug in ordered_series_rooms(series_slug, rooms):
            room = rooms[slug]
            if room["status"].lower() == "forthcoming":
                continue
            out_path = OUTPUT_DIR / (slug + ".html")
            out_path.write_text(
                build_room(room, rooms, visual_catalog), encoding="utf-8"
            )
            written.append(out_path)

    index_path = OUTPUT_DIR / "index.html"
    index_path.write_text(build_index(rooms, visual_catalog), encoding="utf-8")
    written.append(index_path)
    prune_stale({path.name for path in written})

    failures = 0
    pending_links = 0
    available_slugs = rendered_room_slugs(rooms)
    for path in written:
        expected_corridors = None
        expected_visual_count = None
        room = rooms.get(path.stem)
        if room is not None:
            expected_corridors = [
                slug + ".html"
                for value in room["terms_linked"].split(",")
                if (slug := value.strip()) in available_slugs
                and slug != room["slug"]
            ]
            room_visual_catalog: dict[str, dict[str, object]] = visual_catalog[
                "rooms"
            ]  # type: ignore[assignment]
            visuals = room_visual_catalog[path.stem]["visuals"]
            if isinstance(visuals, list):
                expected_visual_count = len(visuals)
        errors = check_well_formed(
            path,
            expected_corridors=expected_corridors,
            expected_visual_count=expected_visual_count,
        )
        pending_links += path.read_text(encoding="utf-8").count('class="pending"')
        if errors:
            failures += 1
            print("FAIL  %s" % path.relative_to(ROOT))
            for error in errors:
                print("      - %s" % error)
        else:
            print("ok    %s" % path.relative_to(ROOT))

    print(
        "\n%d pages written, %d parse failures; %d room sources, %d pending links, "
        "%d skipped sources, %d visual errors."
        % (
            len(written),
            failures,
            len(rooms),
            pending_links,
            len(skipped),
            len(visual_errors),
        )
    )
    if strict and (missing or skipped or visual_errors):
        return 1
    return 1 if failures or visual_errors else 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--strict",
        action="store_true",
        help="fail if any canonical room source is missing or malformed",
    )
    args = parser.parse_args()
    return build(strict=args.strict)


if __name__ == "__main__":
    sys.exit(main())
