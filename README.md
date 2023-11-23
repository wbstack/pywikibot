# pywikibot

A Docker image providing `pywikibot` with a Wikibase.cloud specific families, configured using environment variables.

## Configuration

Configuration is provided using the following environment variables:

---

### `SOURCE_WIKI_HOSTNAME`

The hostname of the source wiki, e.g. `coffeebase.wikibase.cloud`

### `SOURCE_WIKI_PROTOCOL` (optional)

The protocol used by the source wiki, defaults to `HTTPS`

### `SOURCE_WIKI_USERNAME` (optional)

The username tied to the OAuth 1.0 credentials.
In case this is not provided, access to the source wiki will be unauthenticated.

### `SOURCE_WIKI_CONSUMER_TOKEN` (optional)

The OAuth consumer token used for authenticating against the source wiki.

### `SOURCE_WIKI_CONSUMER_SECRET` (optional)

The OAuth consumer secret used for authenticating against the source wiki.

### `SOURCE_WIKI_ACCESS_TOKEN` (optional)

The OAuth access token used for authenticating against the source wiki.

### `SOURCE_WIKI_ACCESS_SECRET` (optional)

The OAuth access secret used for authenticating against the source wiki.

---

### `TARGET_WIKI_HOSTNAME`

The hostname of the target wiki, e.g. `newwiki.wikibase.cloud`

### `TARGET_WIKI_PROTOCOL` (optional)

The protocol used by the target wiki, defaults to `HTTPS`

### `TARGET_WIKI_USERNAME` (optional)

The username tied to the OAuth 1.0 credentials.
In case this is not provided, access to the source wiki will be unauthenticated.

### `TARGET_WIKI_CONSUMER_TOKEN` (optional)

The OAuth consumer token used for authenticating against the target wiki.

### `TARGET_WIKI_CONSUMER_SECRET` (optional)

The OAuth consumer secret used for authenticating against the target wiki.

### `TARGET_WIKI_ACCESS_TOKEN` (optional)

The OAuth access token used for authenticating against the target wiki.

### `TARGET_WIKI_ACCESS_SECRET` (optional)

The OAuth access secret used for authenticating against the target wiki.
