# God's Eye Weather

Hyperlocal rain & snow forecast PWA. Companion to
[God's Eye View](https://github.com/bilawalsidhu/gods-eye-view) — same data
philosophy, phone-sized: GPS location in, "is it raining on me" out.

## What it shows
- **Right now**: raining/snowing/dry + temp/feels-like + plain-English condition
- **Next 2 hours**: 15-min precipitation strip (start/stop of rain or snow)
- **Next 7 days**: daily precip totals + chance, snow highlighted
- Bonus chips: wind + humidity

## Data (all free, no keys)
- [Open-Meteo](https://open-meteo.com/) — forecast (CC BY 4.0)
- [OpenStreetMap Nominatim](https://nominatim.openstreetmap.org/) — reverse geocoding
- Browser Geolocation — device GPS (nothing stored server-side; coords live in localStorage only)

## Run
Single-file app, no build step. Serve over HTTPS (required for geolocation):
- Local test: `python -m http.server` then open `http://localhost:8000` (geolocation needs `localhost` or HTTPS)
- Production: GitHub Pages — Settings → Pages → deploy from main branch root

## Install on Android
Open the Pages URL in Chrome → menu → **Add to Home screen**. Launches full-screen like a native app.

## Units
°F, inches, mph (hardcoded US units for v1).
