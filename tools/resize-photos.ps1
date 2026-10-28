# Copies photos from images/ to photos/ for the web page.
# JPGs are resized to max 1600 px (System.Drawing cannot write WebP, so WebPs are copied as-is).
param([int]$MaxSize = 1600)
$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Drawing
$src = Join-Path $PSScriptRoot '../images'
$dst = Join-Path $PSScriptRoot '../photos'
New-Item -ItemType Directory -Force $dst | Out-Null

$codec = [System.Drawing.Imaging.ImageCodecInfo]::GetImageEncoders() | Where-Object MimeType -eq 'image/jpeg'
$params = New-Object System.Drawing.Imaging.EncoderParameters 1
$params.Param[0] = New-Object System.Drawing.Imaging.EncoderParameter ([System.Drawing.Imaging.Encoder]::Quality), 82L

Get-ChildItem $src -File | Where-Object Extension -in '.jpg', '.jpeg', '.png', '.webp' | ForEach-Object {
  $target = Join-Path $dst $_.Name
  if ($_.Extension -notin '.jpg', '.jpeg') { Copy-Item $_.FullName $target -Force; return }
  $img = [System.Drawing.Image]::FromFile($_.FullName)
  try {
    # Respect EXIF orientation (tag 0x0112) so portrait phone shots stay upright.
    if ($img.PropertyIdList -contains 274) {
      switch ([int]$img.GetPropertyItem(274).Value[0]) {
        3 { $img.RotateFlip('Rotate180FlipNone') }
        6 { $img.RotateFlip('Rotate90FlipNone') }
        8 { $img.RotateFlip('Rotate270FlipNone') }
      }
    }
    $s = [math]::Min(1.0, [double]$MaxSize / [math]::Max($img.Width, $img.Height))
    $w = [int]($img.Width * $s); $h = [int]($img.Height * $s)
    $bmp = [System.Drawing.Bitmap]::new($w, $h)
    $g = [System.Drawing.Graphics]::FromImage($bmp)
    $g.InterpolationMode = 'HighQualityBicubic'
    $g.DrawImage($img, 0, 0, $w, $h)
    $bmp.Save($target, $codec, $params)
    $g.Dispose(); $bmp.Dispose()
    Write-Host ("{0} -> {1}x{2}" -f $_.Name, $w, $h)
  } finally { $img.Dispose() }
}
