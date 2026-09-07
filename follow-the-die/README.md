# Follow the Die — standalone public demonstration

Public URL: https://amitabhainarunachala.github.io/darshan/follow-the-die/

Authorized by the owner in the September 7, 2026 conversation. This folder is a standalone delivery of the v2.2 atlas, not a change to Darshan's existing pages or its canonical research model. No private notes, credentials, personal records, analytics or external runtime libraries are included.

The 25 ordered data files concatenate to one base64-encoded gzip stream. They preserve the existing 481159-byte self-contained HTML, SHA-256 `6b572e2bbff2049ebeeac22121c46b5aad82dee4a08ba7eafe5ee89bf270690c`. The loader fetches only these same-origin assets, uses native browser decompression, verifies the SHA-256, updates two footer delivery-status sentences, and opens the decoded atlas. Errors remain visible with a retry control. HTTPS and a current browser supporting DecompressionStream and Web Crypto are required.

To reconstruct the source locally from this folder:

```python
from pathlib import Path
import base64, gzip, hashlib
packed = ''.join((Path('data') / f'{i:02}.txt').read_text() for i in range(1, 26))
html = gzip.decompress(base64.b64decode(packed, validate=True))
assert hashlib.sha256(html).hexdigest() == '6b572e2bbff2049ebeeac22121c46b5aad82dee4a08ba7eafe5ee89bf270690c'
Path('atlas-source.html').write_bytes(html)
```

Verification before publication: exact byte reconstruction; 17 passing local loader/interface checks at 390 and 1440 pixels, including native gzip decoding, all 37 cards, map navigation, gate-to-etch-to-ring exploration, real-time mechanism playback, layout fit, and visible corrupt-data failure. These loader checks used Playwright set_content with local fetch responses and a Python SHA-256 test binding because about:blank is not a secure origin. They are not a live-URL, physical iPhone or Safari test. The earlier v2.2 app report documents its separate 244 document-level assertions. Technology illustrations and company-capability examples remain a partial educational atlas, not a foundry-specific recipe or a verified commercial-chip supply chain.
