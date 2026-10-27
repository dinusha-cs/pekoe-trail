# Requirements: files, images and tools

## What the page needs (already in the repo)

| File | Purpose | Made by |
|---|---|---|
| `index.html` | The whole app (Three.js from the jsDelivr CDN) | hand-written |
| `the-pekoe-trail-stage-1-hantana-to-galaha-official-profile.gpx` | Route (Wikiloc export, 12.84 km) | provided |
| `data/stage-01-landmarks.json` | 21 landmarks: km, side, text, story, photos | `tools/build-landmarks.py` |
| `data/terrain/*.png`, `manifest.json` | Elevation tiles (AWS Terrain Tiles, zoom 13) | `tools/fetch-terrain.ps1` |
| `photos/` | Images used by the page (resized copies of `images/`) | `tools/resize-photos.ps1` |
| `photos/logo.png` | Trail logo: favicon, signboards, dialogs | from `images/logo.png` |
| `photos/stage-01-map.png` | Stage 1 map banner at the start | downloaded from thepekoetrail.org |
| `photos/team.jpeg` | Team photo; the people models are based on it | provided |
| `data/photo-credits.json` | Author and licence for each Wikimedia Commons photo, shown on the card | from `images/commons-credits.json` |

## Images still wanted

Put new photos in `images/`. Name them after the place, e.g. `small-kovil-1.jpg`. Then run `tools/resize-photos.ps1` and add each one to `tools/build-landmarks.py`.

### Landmarks with no photo yet (cards show a placeholder)

| Landmark | km | Wanted |
|---|---|---|
| Chocolates for flowers | 8.2 | The flower bouquet |

### Stand-in photos to replace with our own

These come from Wikimedia Commons (`images/commons-*.jpg`). They show the right area (Hantana range, the Hanthana–Galaha road, Galaha), but not the exact spot:

- shooting club (second photo)
- sugarcane centre (second photo)
- boulders
- descent views
- Galaha town (second photo)
- Galaha Post Office (second photo)

Our own photo of each place would be better.

Each Commons photo's credit and licence is in `images/commons-credits.json` and `data/photo-credits.json`. The card shows the credit on the photo.

### Photos that would improve the 3D scenes

- **Museum top floor:** the tea shop hall is now modelled on `Museum top floor-1.webp`. A photo of the viewing telescope, and one of the building from outside showing the top floor, would help.
- **Real trail waymarks:** the painted arrows and junction signposts, to copy their colours and shape. The current ones are a stylised guess.
- **Stream crossing:** the bath spot at the stream, to replace the gallery photo `s13.webp`.
- **Team:** one front photo of each person, for more accurate outfits.

### Location help (optional)

Photos with GPS (phone location turned on) can be placed exactly. Our current JPGs have no GPS data, so 7 photos were placed by matching the scenery. A Strava or GPX recording of our own walk would also let the stops (kovil, kids, stream) sit at their exact positions.

## Permissions to check before publishing

These come from thepekoetrail.org:
- the gallery photos (`s*.webp`);
- the stage map (`stage-01-map.png`);
- the logo.

They're fine for a private version. Get their permission, or replace them, before sharing publicly.

The Wikimedia Commons photos are CC BY-SA. You can publish them as long as you:
- keep the credit line on each photo;
- link the licence.

Photos of the kids need their parents' consent before publishing.

## Tools to run it

- **A local web server.** The page loads data files, so it can't be opened as a plain file. Run:

  ```
  python -m http.server 8765
  ```

  Then open http://localhost:8765/index.html. Add `?debug=1` for self-checks in the console.
- **An internet connection**, to load Three.js from the CDN.
- **PowerShell** (Windows) for `tools/fetch-terrain.ps1` and `tools/resize-photos.ps1`.
- **Python 3** for `tools/build-landmarks.py`:

  ```
  python tools/build-landmarks.py the-pekoe-trail-stage-1-hantana-to-galaha-official-profile.gpx data/stage-01-landmarks.json
  ```

## For later stages

Each new stage needs:
- its GPX file;
- the elevation tiles (re-run `tools/fetch-terrain.ps1` with the new GPX);
- a landmarks list;
- photos.
