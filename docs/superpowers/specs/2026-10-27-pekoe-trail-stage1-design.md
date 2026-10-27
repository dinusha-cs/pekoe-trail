# Pekoe Trail Walk — v1 (Stage 1) Design

Date: 2026-10-27
Status: approved design, pending spec review

## Goal

A browser-based 3D walk along **Stage 1 of the Pekoe Trail** (Ceylon Tea Museum, Hanthana → Galaha Post Office, Sri Lanka), in the spirit of browser worlds like abeto's *Messenger*: a small original character walks through a stylized low-poly world. The route and terrain are real; landmarks along the way open photo cards.

v1 = Stage 1 only. Later stages reuse the same page with a different GPX + landmarks file.

## Decisions (from brainstorming)

| Topic | Decision |
|---|---|
| Photos | Popup card when the walker reaches a landmark |
| Movement | Guided: walker follows the GPX route; forward/back only |
| Packaging | One `index.html` holding all code; data + photos as files next to it |
| Geography | Real GPX route + real elevation (DEM) |
| Walk time | ~5–8 min for the full 12.84 km |
| Art style | Stylized low-poly, flat shading, soft palette |
| Character | Original hiker design (hat + backpack). Not a copy of any existing game's character |

## Inputs (already in repo)

- `the-pekoe-trail-stage-1-hantana-to-galaha-official-profile.gpx`: official route from Wikiloc. 226 track points, 12.84 km, 776–1,067 m.
- `data/stage-01-landmarks.json`: 19 landmarks with `km` along the GPX, lat/lon, elevation, text, confidence and photo list. All 20 photos are assigned.
- `images/`: 13 `s*.webp` from the official site gallery, plus 7 of the user's own JPGs.

## File layout

```
index.html                      all app code (HTML + CSS + JS module), Three.js via CDN importmap
the-pekoe-trail-stage-1-...gpx  route (parsed in browser)
data/stage-01-landmarks.json    landmarks + photo mapping
data/terrain/manifest.json      tile list + bbox + zoom (generated)
data/terrain/13_x_y.png         Terrarium elevation tiles (generated)
images/                         original photos (source)
photos/                         resized copies used by the page (generated, max 1600 px)
tools/fetch-terrain.ps1         one-time: download DEM tiles covering route + margin
tools/resize-photos.ps1         one-time: resize JPGs into photos/
```

Why the tools are PowerShell: no Node and no Python imaging library on this machine. PowerShell has `Invoke-WebRequest` and `System.Drawing`, and Python TLS fails against some hosts on this network.

## Data pipeline

1. **Elevation:** AWS Terrain Tiles (Terrarium PNG, open data, `s3.amazonaws.com/elevation-tiles-prod/terrarium/{z}/{x}/{y}.png`) at zoom 13 (~19 m/px at this latitude).
   - Coverage: route bbox (lat 7.1972–7.2685, lon 80.6294–80.6697) plus a 1.5 km margin, about 4×5 tiles.
   - The script writes the PNGs and `manifest.json`.
   - Decoding happens in the browser: draw tiles to a canvas, `getImageData`, then `height = R*256 + G + B/256 − 32768`. No image library needed at build time.
2. **Route:** the GPX is parsed in the browser with `DOMParser`, giving the points and the cumulative distance in metres.
3. **Photos:**
   - JPGs are resized to max 1600 px in `photos/` with the same base names.
   - WebPs are copied as-is (already 2048 px).
   - `landmarks.json` photo paths point to `photos/`. The build step rewrites the `images/` prefix.

## Coordinates

- Local metres, origin at the route bbox centre.
- `x` = east, `z` = −north, `y` = elevation × **1.5** vertical exaggeration (one constant, `VERT_EXAG`).
- lat/lon → metres via equirectangular projection (error is negligible over 10 km).

## World

- **Terrain mesh:** a grid of ~200×300 segments covering the tile area, with heights sampled bilinearly from the decoded DEM.
  - Non-indexed geometry, for flat-shaded facets.
  - Vertex colors by zone + slope + height: tea green, forest dark green, pine blue-green, rock grey on steep slopes, and earthy brown along the trail corridor.
- **Zones** (by km of the nearest trail point; config array in `index.html`):

  | km | Zone |
  |---|---|
  | 0–0.3 | museum grounds |
  | 0.3–5.2 | tea estate |
  | 5.2–5.8 | pines and boulders |
  | 5.8–7.2 | rock faces (Katusu Konda) |
  | 7.2–10.4 | tea and forest |
  | 10.4–11.3 | pine forest |
  | 11.3–12.0 | river valley |
  | 12.0–end | Galaha village |

- **Trail:**
  - The route is a `CatmullRomCurve3` through the GPX points, with `y` taken from the terrain (not the GPX elevation) so it sits on the ground.
  - It is drawn as a 4 m ribbon 0.3 m above the terrain.
  - The GPX elevation is used only for HUD numbers and the profile.
- **Scatter:** `InstancedMesh` low-poly props placed within ~300 m of the trail, kept ≥6 m off the path, with density by zone.
  - Tea bushes: ~6,000.
  - Broadleaf shade trees: ~1,500.
  - Pines: ~800.
  - Boulders: ~300.
  - A seeded RNG keeps placement stable between loads.
- **Landmark props:** simple low-poly stand-ins.
  - Tea factory block at the start.
  - White stupa at Sandagiri.
  - Post office hut at the finish.
  - River and bridge at 11.85 km.
  - Every other landmark gets a glowing marker post.
- **Sky, light and backdrop:**
  - Gradient sky dome, warm directional sun, hemisphere fill, exponential fog.
  - A distant ring of low-poly ridge silhouettes beyond the DEM edge suggests the Knuckles range and Victoria Reservoir direction.

## Walker and camera

- **State:** one number, `s` = metres along the route (0 to the route length). Position = `curve.getPointAt(s/len)`; facing = curve tangent.
- **Speed:** walk 30 m/s and run 60 m/s, so 12.84 km takes ~7 min walking. Constants `WALK_SPEED` and `RUN_SPEED`.
- **Look:** the character is ~4 m tall (stylized scale), made of grouped primitives. Walk cycle is procedural: leg/arm swing plus body bob, driven by distance travelled.
- **Controls:**

  | Action | Desktop | Touch |
  |---|---|---|
  | Forward | W / ↑ | hold the right half of the screen |
  | Back | S / ↓ | on-screen back button |
  | Run | Shift | — |
  | Orbit camera | drag (springs back after release) | drag |

- **Camera:** third-person follow, ~25 m behind and ~12 m up, with smoothing. Pulled up whenever terrain would block the view.

## Landmarks

- **Trigger:** when `|s − landmark.km*1000| < 60 m`.
- **First arrival:** walking pauses and the card opens.
- **Later passes:** a "View" prompt appears (E key, or tap).
- **Card contents:**
  - Name, km, elevation and text.
  - Photo carousel with left/right arrows.
  - If the landmark has no photos, a placeholder illustration.
  - Close with Esc, ✕ or a tap outside.
- **Visited list:** tracked in memory only for v1, not persisted.

## UI

- **Top bar:** "Stage 1 · Hanthana → Galaha", distance `x.xx / 12.84 km`, elevation `m`.
- **Bottom:** elevation profile canvas drawn from the GPX, with a moving dot and landmark ticks.
- **Loading screen:** progress bar over the GPX, landmarks, terrain tiles and scene build.
- **Finish screen:** at `s = len`, shows the stats (distance, elevation gain/loss from the GPX, landmarks seen) and a "Walk again" button.
- **Credits/attribution footer:** route by The Pekoe Trail (Wikiloc); terrain from AWS Terrain Tiles (Mapzen / USGS / others); place data from © OpenStreetMap contributors; gallery photos from thepekoetrail.org.

## Errors

- **No WebGL:** message explaining that the walk needs WebGL.
- **A tile fails to load:** that area is flat at the median height and a warning goes to the console. The page still runs.
- **A photo fails to load:** placeholder image in the card.
- **Opened via `file://`:** module and fetch requests fail, so the page shows "run `npx serve` / any static server" instead of a blank screen.

## Testing

- **`?debug=1` self-check on load (console):**
  - Route length within 1% of 12.84 km.
  - The terrain covers every route point.
  - Every landmark km lies inside [0, len].
  - Every photo URL returns 200.
  - Trail-to-terrain gap < 1 m.
- **Manual:**
  - Desktop Chrome: 60 fps target.
  - Phone (Chrome Android): ≥30 fps.
  - Walk start → finish and confirm every landmark card opens.
  - Check against real geography: summit at ~5.76 km reads as highest, valley floor near 11.85 km.

## Performance budget

≤150k triangles of terrain, instanced props, a single shadow-casting light (shadows off on mobile), and `devicePixelRatio` capped at 2 (1.5 on mobile).

## Out of scope (v1)

Stages 2–22, NPC dialogue, audio, saved progress, free roam, multiplayer, and satellite imagery.

## Known risks / open items

- **River bridge position:** the site says 10.8 km / 754 m, while the GPX minimum is 11.85 km / 776 m. v1 uses the GPX; adjust in the JSON if needed.
- **Low-confidence photo placements:** 7 entries were placed by scenery match. The user can correct them in `data/stage-01-landmarks.json` without code changes.
- **Gallery photos:** the `s*.webp` files come from thepekoetrail.org. Fine for a private prototype; get permission before publishing, or replace them.
- **Pace:** 30 m/s may feel too fast or too slow. It's a tunable constant.
