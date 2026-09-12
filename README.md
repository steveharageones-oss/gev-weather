# God's Eye Weather

Hyperlocal rain & snow forecast PWA. Companion to
[God's Eye View](https://github.com/bilawalsidhu/gods-eye-view) — same data
philosophy, phone-sized: GPS location in, "is it raining on me" out.

## What it shows
- **Right now**: raining/snowing/dry + temp/feels-like + plain-English condition
- **Next 2 hours**: 15-min precipitation strip (start/stop of rain or snow)
- **Next 7 days**: daily precip totals + chance, snow highlighted
- Bonus chips: wind + humidity

## Traffic tab
Same app, second tab: live road speeds and reported incidents near you, from the
**TomTom Traffic API**.
- **Right now** — your nearest main road and your own street, each measured against its own
  free-flow speed ("16 mph where 24 is normal").
- **Cross-check** — the same trick as the radar layer, applied to roads: probe-derived speeds
  are compared against the curated incident feed. Slow sensors + no reported incident =
  probable unreported congestion. Reported incident + fast sensors = clearing, or not your road.
- **Incidents near you** — top 5 by severity then distance, with road names, delay and length.
- **Map** — TomTom flow tiles (relative / absolute toggle) with incident segments drawn on top.

Budget at a 10-minute refresh: 3 non-tile calls and roughly a dozen map tiles per view, against
TomTom's freemium allowance of 50,000 tile and 2,500 non-tile requests a day.

### The API key
No key is committed. `index.html` carries the placeholder `__GEW_TOMTOM_KEY__`, which
`.github/workflows/deploy.yml` swaps for the `GEW_TOMTOM_KEY` repository secret at deploy time.
For local dev, don't edit the file — set it in the console instead:

    localStorage.gew_tomtom_key = 'YOUR_KEY'

Also set a domain whitelist on the key in MyTomTom (Edit key -> Security). Note that whitelisting
only stops other *websites* from using the key; anyone who reads it out of the page source can
still call the API directly. There is no card on file on the freemium plan, so the worst case is
a burnt free quota and a key rotation.

## Data (all free, no keys)
- [Open-Meteo](https://open-meteo.com/) — forecast (CC BY 4.0)
- [OpenStreetMap Nominatim](https://nominatim.openstreetmap.org/) — reverse geocoding
- [TomTom Traffic](https://www.tomtom.com/products/traffic-apis/) — road speeds + incidents (free key, see above)
- Browser Geolocation — device GPS (nothing stored server-side; coords live in localStorage only)

## Run
Single-file app, no build step. Serve over HTTPS (required for geolocation):
- Local test: `python -m http.server` then open `http://localhost:8000` (geolocation needs `localhost` or HTTPS)
- Production: GitHub Pages — Settings → Pages → deploy from main branch root

## Install on Android
Open the Pages URL in Chrome → menu → **Add to Home screen**. Launches full-screen like a native app.

## Units
°F, inches, mph (hardcoded US units for v1).
