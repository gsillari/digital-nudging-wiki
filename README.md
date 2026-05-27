# Digital Nudging Wiki

Public static site for the Digital Nudging course wiki.

The public repository contains only compiled wiki notes and generated HTML. The private working vault keeps the raw PDFs, books, logs, and ingestion machinery.

## Local Build

From this repository:

```bash
python3 scripts/build_static_wiki.py --out docs
```

GitHub Pages can serve the site from the `docs/` folder on the `main` branch.

## Public URL

The expected GitHub Pages project URL is:

```text
https://gsillari.github.io/digital-nudging-wiki/
```

If a different GitHub owner is used, replace `gsillari` accordingly.
