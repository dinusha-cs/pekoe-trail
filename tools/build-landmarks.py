import json, math, re, sys

gpx_path, out_path = sys.argv[1], sys.argv[2]
pts = [(float(a), float(b), float(c)) for a, b, c in re.findall(
    r'<trkpt lat="([\d.]+)" lon="([\d.]+)"><ele>([\d.]+)</ele>', open(gpx_path, encoding="utf-8").read())]

def hav(a, b):
    p1, p2 = math.radians(a[0]), math.radians(b[0])
    dl = math.radians(b[1] - a[1])
    h = math.sin((p2 - p1) / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 12742000 * math.asin(math.sqrt(h))

cum = [0.0]
for i in range(1, len(pts)):
    cum.append(cum[-1] + hav(pts[i - 1], pts[i]))

def at_km(km):
    m = km * 1000
    for i in range(1, len(cum)):
        if cum[i] >= m:
            t = (m - cum[i - 1]) / max(cum[i] - cum[i - 1], 1e-9)
            return [round(pts[i - 1][j] + (pts[i][j] - pts[i - 1][j]) * t, 6 if j < 2 else 0) for j in range(3)]
    return [pts[-1][0], pts[-1][1], round(pts[-1][2])]

# km = distance along the GPX track. source: where the position came from.
# confidence: high = named place geocoded on OSM / shown in photo; medium = matched from site description;
# low = scenery-type match only, place by eye in v1 and adjust.
L = [
 ("tea-museum", "Ceylon Tea Museum (trailhead)", 0.00, "osm", "high",
  "Start of Stage 1, in the former Hantana tea factory. The top floor has a tea shop and tea tasting room.",
  ["photos/commons-tea-museum.jpg", "photos/Museum top floor-1.webp", "photos/s12.webp", "photos/s4.webp"]),
 ("sandagiri-stupa", "Hanthana Sandagiri Maha Seya", 0.95, "osm + team memory", "high",
  "The white Sandagiri Maha Seya on the ridge, seen on the left of the trail in the first kilometre.",
  ["photos/sandagiri-seya.jpg", "photos/s3.webp"]),
 ("kandy-view", "View back over Hanthana & Knuckles", 2.0, "photo match", "medium",
  "Looking back at the Hanthana towers, the stupa and the Knuckles range on the horizon.",
  ["photos/s11.webp", "photos/commons-hantana-highest-peak.jpg"]),
 ("shooting-club", "W15 Hotel & Hill Country Sport Shooting Club", 2.85, "osm", "high",
  "Trail passes W15 Hanthana and the shooting club.", ["photos/W15 Hotel.jpg", "photos/commons-hanthana-galaha-road.jpg"]),
 ("sugarcane", "Sugarcane Quarantine Center", 3.06, "site 3.1 km", "medium",
  "Sugarcane quarantine station of the Sugarcane Research Institute.",
  ["photos/Sugarcane Quarantine Center.jpg", "photos/commons-hanthana-galaha-road-2.jpg"]),
 ("boulder-field", "Boulders above the valley", 3.6, "photo match", "low",
  "Granite boulders among the trees with the towered Hanthana peak behind.", ["photos/s8.webp", "photos/commons-hantana-peaks.jpg"]),
 ("tea-estate", "Hanthana tea estate", 4.2, "photo match", "low",
  "Shaded estate roads between tea bushes and tall shade trees; often misty.",
  ["photos/s2-1.webp", "photos/s10.webp", "photos/s1.webp", "photos/ba16e881-66b6-4146-8e22-0a1d752ab970.jpg"]),
 ("meditation-stupa", "Side trail to meditation stupa", 5.13, "site 5.2 km", "medium",
  "Short detour to a secluded meditation stupa.", ["photos/Side trail to meditation stupa.webp"]),
 ("pine-boulders", "Pines & boulders near the top", 5.4, "photo match", "low",
  "Pine stand and boulders on the final climb.", ["photos/s5.webp"]),
 ("summit", "Highest point & viewpoint", 5.76, "gpx max elevation", "high",
  "Top of the stage (~1,067 m): views to Victoria Reservoir and the Knuckles Range.",
  ["photos/6b7c7e89-1ba8-403e-9352-8cfd27ec10e5.jpg", "photos/e8863e5d-b664-4757-b5e9-6a708027dec6.jpg"]),
 ("katusu-konda", "Katusu Konda rock faces", 6.61, "osm", "high",
  "Sheer rock cliffs of the Katusu Konda range above the trail. Look for the trail's painted rock markers.",
  ["photos/team.jpeg", "photos/s9.webp", "photos/s6.webp", "photos/86164203-752f-4b10-93bf-c3e182e4ed20.jpg"]),
 ("valley-view", "Descent views", 7.5, "photo match", "low",
  "Long views over layered hills on the way down.", ["photos/s7.webp", "photos/commons-hantana-after-rain.jpg"]),
 ("small-kovil", "Small Hindu kovil", 8.0, "team memory", "medium",
  "A small roadside Hindu kovil on the right of the road, with village kids around it.",
  ["photos/Small Hindu kovil.jpg"]),
 ("kids-flowers", "Chocolates for flowers", 8.2, "team memory", "low",
  "More kids along the road, just after the kovil.", []),
 ("film-site", "Temple of Doom film area", 9.87, "site ~10 km", "medium",
  "Dense forest section linked to the filming of Indiana Jones and the Temple of Doom.",
  ["photos/indian-johns-doom-temple.jpg", "photos/indian-johns-doom-temple-2.jpg"]),
 ("pine-forest", "Pine forest road", 10.66, "site 10.8 km", "medium",
  "Pine forest near the end of the stage; slippery in rain.", []),
 ("galaha-town", "Galaha town", 12.5, "photo match", "medium",
  "Into Galaha: shops, a Hindu kovil and trail arrows on the walls.",
  ["photos/commons-galaha-1.jpg"]),
 ("galaha-post-office", "Galaha Post Office (finish)", 12.67, "osm", "high",
  "End of Stage 1.", ["photos/Galaha Post Office.jpg", "photos/commons-galaha.jpg"]),
]

out = {
  "stage": 1, "name": "Hanthana to Galaha",
  "gpx": "the-pekoe-trail-stage-1-hantana-to-galaha-official-profile.gpx",
  "gpxLengthKm": round(cum[-1] / 1000, 2), "officialLengthKm": 13.01,
  "note": "km = distance along GPX. Site distances scaled by gpx/official length. Low-confidence entries placed by scenery match only.",
  "landmarks": [],
}
# side of the trail (walking direction) where the place is
SIDE = {"sandagiri-stupa": "left", "small-kovil": "right", "kids-flowers": "right"}
STORY = {
  "galaha-town": ("We met a few people along the trail; locals were happy to chat with five hikers.", "locals"),
  "tea-estate": ("Tea pluckers at work on the slopes, one of the many people we met on the way.", "pluckers"),
  "katusu-konda": ("Team photo under the Katusu Konda cliffs: Adithya, Sudesh, Dinusha, Theshawa and Sithara.", None),
  "small-kovil": ("We filled our water bottles at the kovil and gave 5 chocolates to the kids at the temple.", "kovil"),
  "kids-flowers": ("We gave 2 more chocolates to some kids, and they gave us a bouquet of flowers in return.", "flowers"),
}
for id_, name, km, src, conf, text, photos in L:
    lat, lon, ele = at_km(km)
    d = dict(id=id_, name=name, km=km, lat=lat, lon=lon, ele=int(ele),
             source=src, confidence=conf, text=text, photos=photos)
    if id_ in STORY:
        d["story"], ev = STORY[id_]
        if ev: d["event"] = ev
    if id_ in SIDE: d["side"] = SIDE[id_]
    out["landmarks"].append(d)
json.dump(out, open(out_path, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
for l in out["landmarks"]:
    print(f'{l["km"]:5.2f}km {l["ele"]:5d}m {l["confidence"]:6s} {l["name"][:40]:40s} {len(l["photos"])} photo(s)')
