# Follow-up work (reviewed 2026-08-30)

## gev-weather (this repo — rain/snow PWA)

- [ ] **`current=snowfall` missing from Open-Meteo URL** (index.html ~line 296). `showNow` reads `cur.snowfall` (line 314) but it's never requested → always undefined. "Snowing now" only fires via weather code, never actual snowfall data.
- [ ] **Daily row null-guard** (index.html ~line 401): `d.precipitation_sum[i].toFixed(2)` throws when Open-Meteo returns `null` for a day. Use `(d.precipitation_sum[i] || 0).toFixed(2)`.
- [ ] **Restore OSM attribution**: `attributionControl: false` at line 461. OSM tile usage policy requires visible attribution — repo is live on GitHub Pages using their tiles. Compliance risk.
- [ ] **Delete dead code**: `getLocation()` (lines 258-278) is never called, and reads key `gew.coords` while the rest of the app uses `gew_location`. Also `rainCode` (line 315) computed but unused.
- [ ] **PWA gap**: manifest exists but no service worker → most browsers won't offer install, no offline. Also no `apple-touch-icon` (iOS home screen gets a screenshot).

## gods-eye-view (C:\Users\steve\gods-eye-view — NWS alerts layer, uncommitted)

Working tree has complete feature: new `src/data/weatherAlerts.js` + wires in `main.js`, `layerState.js` (token `k`, no collision), `dataCredits.js`, `DATA_SOURCES.md`. Code follows earthquakes.js pattern correctly (static polys redrawn per poll, XSS-escaped popup, clean teardown). One blocker before commit:

- [ ] **Fix registry test**: `production registry is exact, canonical, and rejects incomplete contracts` in `src/data/layerState.test.mjs:158` hardcodes `REGISTERED_LAYER_IDS.length === 16` → update to 17. This is the ONLY new test failure caused by the NWS changes.
- [ ] **Add voice aliases**: `LAYER_ALIASES` in `src/voice/gevActions.js:144-179` has no `weather`/`alerts` → `weather-alerts` entry, so voice control can't toggle the layer.
- [ ] **Handle MultiPolygon**: `update()` (weatherAlerts.js:168) skips `geom.type !== 'Polygon'`; NWS issues MultiPolygon geometries for some warnings → those alerts invisible. Flatten into multiple entities.
- [ ] Optional: git add the new file + diffs, commit once above done.

## Traffic tab (built, needs the secret + a deploy)
- [ ] Set the `GEW_TOMTOM_KEY` repository secret, then push — the key is injected at deploy,
      nothing to commit by hand. Verify the live page's traffic tab afterwards.
- [ ] Set a domain whitelist on the key in MyTomTom (Edit key -> Security).
- [ ] Open item: `flowSegmentData` returns road CLASS (FRC), not the road name, so the "right now"
      lines say "nearest main road" / "your street". Naming them needs a second Nominatim reverse
      lookup per refresh; their policy wants caching and 1/sec, so it was left out. A slow
      (hourly, cached) lookup is the way to add it if wanted.
- [ ] Known data quality: TomTom's road-closure records are noisy — a 51 km test box around
      Edison returned 165 incidents, 75 of them closures on residential streets, mostly planned
      work. Hence the top-5 cap and severity-first sort rather than a full list.
- [ ] The traffic map uses TomTom raster tiles for its basemap (so the app now has two basemaps:
      OSM on the radar map, TomTom on the traffic map). Deliberate — keeps the radar map's
      attributions and behaviour untouched.

## Baseline facts (for later)

- gods-eye-view unit suite: 2587 tests; **25 pre-existing failures on clean `main`** (Cockpit/voice/UI — predate NWS work). Don't chase those as regressions.
- gev-weather git tree is clean, all pushed; deploy is upload-folder GitHub Pages workflow.
