# Downloads AWS Terrain Tiles (Terrarium PNG) covering the Stage 1 GPX route + margin.
# Output: data/terrain/<z>_<x>_<y>.png and data/terrain/manifest.json
param(
  [string]$Gpx = "$PSScriptRoot/../the-pekoe-trail-stage-1-hantana-to-galaha-official-profile.gpx",
  [int]$Zoom = 13,
  [double]$MarginDeg = 0.02
)
$ErrorActionPreference = 'Stop'
$out = Join-Path $PSScriptRoot '../data/terrain'
New-Item -ItemType Directory -Force $out | Out-Null

[xml]$doc = Get-Content -Raw $Gpx
$pts = $doc.gpx.trk.trkseg.trkpt
$lats = $pts | ForEach-Object { [double]$_.lat }
$lons = $pts | ForEach-Object { [double]$_.lon }
$minLat = ($lats | Measure-Object -Minimum).Minimum - $MarginDeg
$maxLat = ($lats | Measure-Object -Maximum).Maximum + $MarginDeg
$minLon = ($lons | Measure-Object -Minimum).Minimum - $MarginDeg
$maxLon = ($lons | Measure-Object -Maximum).Maximum + $MarginDeg

$n = [math]::Pow(2, $Zoom)
function TileX([double]$lon) { [int][math]::Floor(($lon + 180) / 360 * $n) }
function TileY([double]$lat) {
  $r = $lat * [math]::PI / 180
  [int][math]::Floor((1 - [math]::Log([math]::Tan($r) + 1 / [math]::Cos($r)) / [math]::PI) / 2 * $n)
}
$x0 = TileX $minLon; $x1 = TileX $maxLon
$y0 = TileY $maxLat; $y1 = TileY $minLat

$tiles = @()
for ($x = $x0; $x -le $x1; $x++) {
  for ($y = $y0; $y -le $y1; $y++) {
    $file = "${Zoom}_${x}_${y}.png"
    $dest = Join-Path $out $file
    if (-not (Test-Path $dest)) {
      $url = "https://s3.amazonaws.com/elevation-tiles-prod/terrarium/$Zoom/$x/$y.png"
      Write-Host "GET $url"
      Invoke-WebRequest -Uri $url -OutFile $dest -UseBasicParsing
    }
    $tiles += $file
  }
}

$manifest = [ordered]@{
  source = 'AWS Terrain Tiles (Terrarium encoding): height = R*256 + G + B/256 - 32768'
  zoom   = $Zoom
  x0 = $x0; x1 = $x1; y0 = $y0; y1 = $y1
  tileSize = 256
  tiles  = $tiles
}
$manifest | ConvertTo-Json | Set-Content -Encoding utf8 (Join-Path $out 'manifest.json')
Write-Host "Tiles x $x0..$x1, y $y0..$y1 ($($tiles.Count) tiles) -> $out"
