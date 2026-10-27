# Pekoe Trail Walk: Stage 1

A virtual 3D walk through **Stage 1 of the Pekoe Trail** in Sri Lanka. The stage runs 12.8 km from the Ceylon Tea Museum in Hanthana to the Galaha Post Office. It runs in the browser.

## Purpose

The [Pekoe Trail](https://thepekoetrail.org/) is a long-distance hiking trail through Sri Lanka's tea country. This project retells our own walk of Stage 1 as an interactive scene:

- It follows the real route and the real hills (GPS track and elevation data).
- It shows the places along the way, each with photos.
- It replays what happened to our team of five on the day.

Anyone can open it and "walk" the stage in about 5–8 minutes. Use it as a memory of the trip, or as a preview for someone planning to hike it.

Version 1 covers Stage 1 only. Later stages can reuse the same page with their own route, landmarks and photos.

## What you'll see

- **The real route and terrain:** the official Stage 1 GPX track laid over real elevation data, drawn in a low-poly style. You pass through tea estates, pine forest, the Katusu Konda cliffs and down into Galaha.
- **Our team of five:** they start together at the museum and mostly walk in single file. From time to time they walk two by two.
- **Landmarks with photo cards:** 18 stops, each with a glowing marker and a framed photo beside the path.
  - Walk up to a marker, or click it, to open its card with photos and the story.
- **Our story along the trail:**
  - Hanthana Sandagiri Maha Seya, seen on the left in the first kilometre.
  - Light rain between 7 and 8 km (an umbrella and a raincoat come out).
  - Water and chocolates for the kids at a small Hindu kovil.
  - A flower bouquet in return for more chocolates.
  - At the end in Galaha, a "Welcome to Stage 2" arch and a bus stop with buses back to Kandy.
- **Life on the trail:**
  - Women plucking tea in the plantations.
  - Locals.
  - Foreign hikers who step aside and wave.
  - Visitors at the museum's top-floor tea shop.
- **Finding the way:**
  - Painted arrows on trees and rocks.
  - Signposts at key junctions.
  - The official stage map at the start.
  - An elevation profile showing where you are.

## How to use it

### 1. Start a local web server

The page loads its data files (route, terrain, photos), so it can't be opened by double-clicking `index.html`. From the project folder, run:

```
python -m http.server 8765
```

Any static server works, for example `npx serve`.

### 2. Open the walk

Go to **http://localhost:8765/index.html** in a recent Chrome, Edge, Firefox or Safari. It needs WebGL and an internet connection, because Three.js loads from a CDN. Wait for the loading bar, then press **Start walk**.

### 3. Walk

| Action | Keyboard | Buttons (bottom right) |
|---|---|---|
| Walk forward | W / ↑ | **▶ Walk** (tap again to stop) |
| Start / stop walking | Space | **▶ Walk / ■ Stop** |
| Walk back | S / ↓ | **↶** (hold) |
| Walking speed | — | **1× / 2×** |
| Run | Shift | **Run** |
| Look left / right | A / D | **⟲ ⟳** (hold) |
| Look around | Drag the mouse | Drag on screen |
| Reopen nearby landmark | E | Tap the ★ prompt |
| Open any landmark | Click its marker or framed photo | Tap it |
| Start again | — | **⏮** |

On a phone, you can also hold the screen to walk.

### Debug mode

Open `index.html?debug=1` to run self-checks in the browser console. They check:
- route length;
- terrain coverage;
- elevation match;
- that all photos load.

## Project layout

```
index.html                     the whole app (HTML, CSS, JavaScript; Three.js from CDN)
the-pekoe-trail-stage-1-...gpx  official Stage 1 route
data/stage-01-landmarks.json   landmarks: position on the route, side, text, story, photos
data/photo-credits.json        credits for Wikimedia Commons photos (shown on each photo)
data/terrain/                  elevation tiles + manifest
images/                        original photos (full size)
photos/                        smaller copies loaded by the page
tools/build-landmarks.py       generates the landmarks file
tools/resize-photos.ps1        copies/resizes images/ into photos/
tools/fetch-terrain.ps1        downloads the elevation tiles
instruction.md                 the story and feature notes
requirement.md                 files needed, photos still wanted, permissions
```

## Adding or changing photos and landmarks

1. Put the photo in `images/`. Name it after the place.
2. Run `tools/resize-photos.ps1` (PowerShell) to copy it into `photos/`.
3. Add it to the landmark's photo list in `tools/build-landmarks.py`. You can also change a landmark's position (km), side or text there.
4. Regenerate the landmarks file:

   ```
   python tools/build-landmarks.py the-pekoe-trail-stage-1-hantana-to-galaha-official-profile.gpx data/stage-01-landmarks.json
   ```

5. Reload the page.

[requirement.md](requirement.md) lists which photos are still stand-ins and would be better replaced with our own.

## Credits

- **Route, gallery photos, stage map and logo:** [The Pekoe Trail](https://thepekoetrail.org/pekoe-stages/stage-01/). They are used for this private version; ask for permission before publishing.
- **Elevation:** AWS Terrain Tiles (Mapzen, SRTM/USGS and others).
- **Place data:** © [OpenStreetMap](https://www.openstreetmap.org/copyright) contributors.
- **Extra photos:** [Wikimedia Commons](https://commons.wikimedia.org/), CC BY-SA. The author and licence are shown on each photo.
- **3D engine:** [Three.js](https://threejs.org/).
- **Team photos and story:** our own walk of Stage 1.
