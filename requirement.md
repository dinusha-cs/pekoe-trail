# Requirements: files, images and tools

## What the page needs (already in the repo)

| File | Purpose | Made by |
|---|---|---|
| `index.html` | The whole app (Three.js from the jsDelivr CDN) | hand-written |
| `the-pekoe-trail-stage-1-hantana-to-galaha-official-profile.gpx` | Route (Wikiloc export, 12.84 km) | provided |
| `data/stage-01-landmarks.json` | 22 landmarks: km, side, text, story, photos | `tools/build-landmarks.py` |
| `data/terrain/*.png`, `manifest.json` | Elevation tiles (AWS Terrain Tiles, zoom 13) | `tools/fetch-terrain.ps1` |
| `photos/` | Images used by the page (resized copies of `images/`) | `tools/resize-photos.ps1` |
| `photos/logo.png` | Trail logo: favicon, signboards, dialogs | from `images/logo.png` |
| `photos/stage-01-map.png` | Stage 1 map banner at the start | downloaded from thepekoetrail.org |
| `photos/team.jpeg` | Team photo; the people models are based on it | provided |
| `data/photo-credits.json` | Author and licence for each Wikimedia Commons photo, shown on the card | from `images/commons-credits.json` |

## Images still wanted

Put new photos in `images/`. Name them after the place, e.g. `small-kovil-1.jpg`. Then run `tools/resize-photos.ps1` and add each one to `tools/build-landmarks.py`.

### Landmarks with no photo yet (the card shows text only)

| Landmark | km | Wanted |
|---|---|---|
| Chocolates for flowers | 8.2 | A photo without people (e.g. the bouquet) |
| Stream crossing the road | 8.5 | The stream where it crosses the road |
| Pine forest road | 10.66 | The pine forest |

Only the team photos chosen for the walk are shown: `team.jpeg` and `team-2.jpeg` at Katusu Konda, `team-3-8-km.jpeg` at the kovil, and `trail-end.jpeg` at the finish. The other group photos (`14f6…`, `61ef…`, `304b…`) are deliberately left out.

`trail-end.jpeg` also shows people outside the team. Ask them, or crop them out, before publishing.

### Photo naming

Name a photo after the place, or the km where it was taken (e.g. `tree-7-km.jpeg`). Photos named with a km go on the nearest stop, or become a new stop when they show a named place.

### Stand-in photos to replace with our own

These come from Wikimedia Commons (`images/commons-*.jpg`). They show the right area (Hantana range, the Hanthana–Galaha road, Galaha), but not the exact spot:

- shooting club (second photo)
- sugarcane centre (second photo)
- boulders
- descent views
- Galaha town
- Galaha Post Office (third photo)

Our own photo of each place would be better.

## Photo inventory (`photos/`)

Checked against `data/stage-01-landmarks.json`. **Source copy in `images/`** means the original is also kept in `images/`.

### Used in the walk (41 photos on stops, plus the logo and map)

| Photo | Where it appears | Source copy in `images/` |
|---|---|---|
| `commons-tea-museum.jpg` | Ceylon Tea Museum (0 km) | yes |
| `Museum top floor-1.webp` | Ceylon Tea Museum (0 km) | yes |
| `Museum top floor ceylon tea museum-2.jpg` | Ceylon Tea Museum (0 km) | yes |
| `s12.webp`, `s4.webp` | Ceylon Tea Museum (0 km) | yes |
| `sandagiri-seya.jpg`, `s3.webp` | Hanthana Sandagiri Maha Seya (0.95 km) | yes |
| `view-2-km.jpeg`, `s11.webp`, `commons-hantana-highest-peak.jpg` | View back over Hanthana (2 km) | yes |
| `W15 Hotel.jpg`, `commons-hanthana-galaha-road.jpg` | W15 Hotel & shooting club (2.85 km) | yes |
| `Sugarcane Quarantine Center.jpg`, `commons-hanthana-galaha-road-2.jpg` | Sugarcane Quarantine Center (3.06 km) | yes |
| `s8.webp`, `commons-hantana-peaks.jpg` | Boulders above the valley (3.6 km) | yes |
| `katusu-konda-4-km.jpeg` | First view of Katusu Konda (4 km) | yes |
| `s2-1.webp`, `s10.webp`, `s1.webp`, `ba16e881….jpg` | Hanthana tea estate (4.2 km) | yes |
| `Side trail to meditation stupa.webp` | Side trail to meditation stupa (5.13 km) | yes |
| `s5.webp` | Pines & boulders (5.4 km) | yes |
| `6b7c7e89….jpg`, `e8863e5d….jpg` | Highest point (5.76 km) | yes |
| `sandagiriseya-from-6-km.jpeg` | Looking back toward Sandagiri Seya (6 km) | yes |
| `team.jpeg`, `team-2.jpeg`, `s9.webp`, `s6.webp`, `86164203….jpg` | Katusu Konda rock faces (6.61 km) | `team.jpeg`: **no**; the others: yes |
| `tree-7-km.jpeg` | Lone tree on the descent (7 km) | yes |
| `s7.webp`, `commons-hantana-after-rain.jpg` | Descent views (7.5 km) | yes |
| `Small Hindu kovil.jpg`, `team-3-8-km.jpeg` | Small Hindu kovil (8 km) | yes |
| `indian-johns-1.jpg`, `indian-johns-doom-temple.jpg`, `indian-johns-doom-temple-2.jpg` | Temple of Doom film area (9.87 km) | yes |
| `commons-galaha-1.jpg` | Galaha town (12.5 km) | yes |
| `Galaha Post Office.jpg`, `trail-end.jpeg`, `commons-galaha.jpg` | Galaha Post Office (12.67 km) | yes |
| `logo.png` | Favicon, start/finish dialogs, signboards | yes |
| `stage-01-map.png` | Stage map banner at the start | **no** |

### In `photos/` but not used

| Photo | Why |
|---|---|
| `14f6abed….jpg`, `61ef04d7….jpg`, `304b1253….jpg` | Group photos, left out on request |
| `Chocolates for flowers.jpg` | Removed on request |
| `commons-chocolate.jpg`, `commons-flower-bouquet.jpg` | Stock photos, removed on request |
| `s13.webp` | Wrong photo for the stream crossing, removed on request |
| `commons-hanthana-galaha-road-1.jpg` | Was for the Crossroads shop, which was removed |

The unused files can be deleted from both `images/` and `photos/` if you don't want them in the repo.

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
