# Beyond the Trail: instructions

**Theme:** Beyond the Trail: Smiles, Kindness, and Rural Life in Sri Lanka’s Central Highlands.

This is a browser 3D walk of **Pekoe Trail Stage 1** (Ceylon Tea Museum, Hanthana → Galaha Post Office), built from our own walk. Version 1 covers Stage 1 only.

## Sources

- Trail site: https://thepekoetrail.org/
- Stage 1 page: https://thepekoetrail.org/pekoe-stages/stage-01/
- Stage 1 map: https://thepekoetrail.org/wp-content/uploads/Stage_01-768x802.png

## The team

Five people, modelled from `photos/team.jpeg`. Walking order, front to back:

| # | Name | Look |
|---|---|---|
| 1 | Sudesh | Shortest, no cap. Usually at the front |
| 2 | Dinusha (me) | Green t-shirt with a cap |
| 3 | Sithara | Sunglasses |
| 4 | Theshawa | No cap |
| 5 | Adithya | Hat. Usually last |

- No name labels above the people, and no names on the start screen.
- All five start together at the museum.
- Mostly single file, and from time to time two by two.

## Our story along the trail

| Where | What happened | In the walk |
|---|---|---|
| First km, left side | Saw Hanthana Sandagiri Maha Seya | White stupa on the left; stop at 0.95 km |
| Along the trail | Met a few local people | Locals in Galaha town; foreign hikers who wave; tea pluckers |
| 7–8 km | Very light rain. Dinusha had a purple umbrella, Sudesh a black raincoat, the others nothing | Rain, haze and stronger wind between 7 and 8 km |
| ~8 km, right side | Small Hindu kovil. We filled our water bottles and gave 5 chocolates to the kids at the temple | Kovil with 5 waving kids; the team stops and holds out chocolates |
| Just after the kovil (8.2 km) | Gave 2 more chocolates to other kids, and they gave us a flower bouquet | 2 kids, one holding a bouquet |
| Stream crossing the road, right side (~8.5 km) | Everyone cooled off; Adithya had a full bath | Adithya chest-deep in the stream pool, dunking and splashing while the stop is open |

## Start: Ceylon Tea Museum

- Nameboard "Ceylon Tea Museum" on the building and at the trailhead.
- Stage 1 map as a banner beside the path at the start.
- Trail logo at the start and the end. Also used as the favicon.
- Tourists arriving at the museum, with a tour van.
- The top floor (modelled on `Museum top floor-1.webp`):
  - a timber hall with a tea shop and the "Tea Tasting Unit";
  - café tables and bench tables;
  - a viewing telescope;
  - visitors.

## Along the trail

- Foreign tourists met on the path several times.
- Women plucking tea in well-kept, dense tea plantations.
- Dense, vivid hill-country forest:
  - canopy trees and silver oaks;
  - eucalyptus and pines;
  - bamboo, coconut palms, banana plants and flame trees.

  All trees sway in the wind.
- Guide marks for navigation:
  - painted arrows on trees and rocks;
  - signposts at key junctions.
- More houses in the last 2 km into Galaha.

## End: Galaha

- "Welcome to Stage 2" arch: Stage 1 ends here, Stage 2 starts from here.
- Bus stop with buses to Kandy, and a bus marked "KANDY".
- The finish screen thanks "every smile and kindness along the way".

## Music and sound

The music is generated in the browser, with no audio files and so no licensing. It is calm and suits the theme:
- a soft pad on D, Bm, G and A;
- a gentle D-major pentatonic melody with an echo;
- a light hand drum.

The nature sounds follow the walk:
- birdsong, with fewer birds in the rain and in Galaha town;
- the stream near the bath stop;
- rain between 7 and 8 km.

It starts when you press Start walk. Turn it on or off with the 🔊 button or the M key; the browser remembers the choice.

## Photos

- Every stop shows its photos on its card, plus a framed photo beside the path.
- A stop with no photo shows no picture at all; there is no "coming soon" placeholder.
- Name new photos after the place or the km (e.g. `tree-7-km.jpeg`) so they can be placed. The full photo list, used and unused, is in `requirement.md`.

## Controls

- **Buttons:**
  - start again from the beginning
  - walk back
  - walk / stop
  - speed 1× / 2×
  - run
  - look left / right
- **Landmarks:** click a marker or its framed photo to see its information.
- **Keyboard:**

  | Key | Action |
  |---|---|
  | W / ↑ | Walk |
  | S / ↓ | Back |
  | Space | Walk / stop |
  | Shift | Run |
  | A / D | Look left / right |
  | E | Reopen a landmark |
  | M | Music on / off |

## Removed on request

- Landmarks: Crossroads shop, River bridge (and its 3D bridge).
- Photos:
  - our group photos `14f6…`, `61ef…`, `304b…`;
  - the chocolate photos;
  - the wrong stream photo `s13.webp`.

## Status

All items above are done in `index.html`.

To change a landmark's position, side, text or photos, edit `tools/build-landmarks.py` and re-run it (see `requirement.md`).
