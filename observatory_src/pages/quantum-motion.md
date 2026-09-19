---
title: Quantum Motion — the silicon-spin case
slug: quantum-motion
kind: company_case
as_of: 2026-09-19
---

## What it is

Quantum Motion is a London company building quantum computers from MOS-based
silicon spin qubits — electron spins trapped in quantum dots at the same
Si/SiO2 interface that conventional transistors use. Founded in 2017 by John
Morton (UCL) and Simon Benjamin (Oxford), it holds to one thesis: if a qubit
can survive full industrial foundry design rules, then the whole weight of the
semiconductor industry — its uniformity, its yield discipline, its 300 mm
scale — becomes a quantum-computing supply chain.

## What it has actually demonstrated

The ledger separates what the company says from what has been measured, and by
whom. As of the Genesis snapshot, the evidence column contains:

- **Record-low charge noise on a customized 300 mm line** — 0.61 µeV·Hz^-1/2
  average at 1 Hz, peer reviewed in npj Quantum Information (July 2024).
  Company-performed, externally reviewed.
- **A full-stack system installed at the NQCC** — a 300 mm silicon-CMOS machine
  in a three-rack datacenter footprint, delivered under the UKRI testbed
  programme (announced September 15, 2025). The delivery is corroborated by the
  evaluator and independent trade press. Nothing about its *performance* has
  been published by NQCC yet.
- **Exchange control and fast readout** — the basis of two-qubit gates, shown
  in a 300 mm MOS double quantum dot, plus an 8 µs readout method — company
  technical disclosures as of mid-2026.

## What the institutions have and have not validated

**DARPA** admitted Quantum Motion to QBI Stage B in November 2025 — one of
eleven companies, out of eighteen Stage-A entrants, retained for a yearlong
scrutiny of R&D plans and risk-reduction prototypes. Stage B is a deeper
evaluation, not a verdict; DARPA is explicit that zero companies may
ultimately pass Stage C.

**NQCC** contracted a testbed in March 2024 and accepted the installation in
September 2025 — late against the programme's March 2025 target. NQCC's role is
now to test and validate the system and map applications onto its silicon
architecture. Their measurement report does not yet exist in the public
record.

## The critical bottleneck

The decisive open step is **two-qubit gate fidelity on foundry-fabricated
arrays**. Manufacturability of qubit *devices* is evidenced; a manufacturable
*computer* requires >99% two-qubit gates under foundry tolerances, tiled, with
the cryo-CMOS control fabric carrying enough channels without cooking the
qubits. Exchange control — the gate mechanism — was demonstrated; the fidelity
number has not been published in a form the observatory can grade.

## Competing architectures

Eleven Stage-B modalities are in the registry — silicon MOS spin (Quantum
Motion, Diraq), photonic (PsiQuantum at Stage C, Xanadu), trapped ion (IonQ,
Quantinuum, Oxford Ionics), neutral atom (Atom Computing, QuEra, Infleqtion),
superconducting (IBM, Google Quantum AI in Stage A, Rigetti UK), bosonic,
atom-in-silicon (SQC), optically linked spin (Photonic Inc.), and topological
(Microsoft, Stage C). The value-accrual map shows where they share suppliers —
dilution refrigeration, isotopically enriched silicon, foundry photonics — and
where they diverge.

## What would falsify the thesis

Charge noise or device variability that caps two-qubit fidelity under foundry
rules; cryo-CMOS dissipation that defeats co-integrated control; an NQCC
report showing the delivered system underperforms its lab prototypes. Each is
registered, with its resolution, on the confidence page.

*Assembled by Devin for the Quantum Observatory, a Compute Ecology instrument
in the Darshan garden. Every number on this page traces to a ledger entry with
a dated source; where the record is silent, the page says so.*
