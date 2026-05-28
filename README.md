# Digital Nudging Wiki

Public Quartz build of the Digital Nudging course wiki.

Only compiled Markdown notes from the private working vault's `wiki/` directory are copied into this repository as `content/`. Raw PDFs, books, EPUBs, and other source files are intentionally not published.

## Local Preview

```sh
NPM_CONFIG_CACHE=.npm-cache npm ci
NPM_CONFIG_CACHE=.npm-cache npm run serve
```

Quartz serves the local site at `http://localhost:8080`.

## Update Content

From this repository:

```sh
rsync -a --delete /path/to/private-vault/wiki/ content/
NPM_CONFIG_CACHE=.npm-cache npm run build
```

Deploy the generated `public/` directory to the `gh-pages` branch.

## Published Site

https://gsillari.github.io/digital-nudging-wiki/
