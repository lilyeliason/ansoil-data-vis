"""
Recolor existing prediction map PNGs using Option B colormaps.
No GeoTIFFs needed — works directly from the PNGs already in assets/images/.

Run from your project root:
  python recolor_maps.py
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

PROJECT_ROOT = Path(
    "/Users/lilyeliason/Documents/2025-2026/dspx_113/Antarctic_vis/the-018-percent"
)
ASSETS = PROJECT_ROOT / "assets" / "images"

# ── Option B colormap assignments ──────────────────────────────────────────
CONFIGS = {
    "clean_01_delta-15N.png": {
        "cmap": "RdBu_r",
        "diverging": True,
    },
    "clean_02_phosphorus.png": {
        "cmap": "YlOrRd",
        "diverging": False,
    },
    "clean_03_sodium.png": {
        "cmap": "Blues",
        "diverging": False,
    },
    "clean_04_nickel.png": {
        "cmap": "Purples",
        "diverging": False,
    },
    "clean_10_titanium.png": {
        "cmap": "Greens",
        "diverging": False,
    },
}


def recolor(filename, config):
    src_path = ASSETS / filename
    img = Image.open(src_path).convert("RGBA")
    arr = np.array(img, dtype=float)

    # Extract alpha mask (transparent = background/ocean, keep it transparent)
    alpha = arr[:, :, 3]
    land_mask = alpha > 10  # pixels that are actual land data

    # Convert existing RGB to grayscale intensity (0-1) to get relative values
    rgb = arr[:, :, :3] / 255.0
    intensity = 0.299 * rgb[:, :, 0] + 0.587 * rgb[:, :, 1] + 0.114 * rgb[:, :, 2]

    # Only work on land pixels
    land_vals = intensity[land_mask]

    # Normalize to 0-1 range
    vmin, vmax = np.percentile(land_vals, 2), np.percentile(land_vals, 98)
    if vmax == vmin:
        vmax = vmin + 1e-6
    normed = np.clip((intensity - vmin) / (vmax - vmin), 0, 1)

    # For diverging: re-center around 0.5
    if config["diverging"]:
        normed = normed  # already 0-1, RdBu_r will handle the visual centering

    # Apply new colormap
    cmap = plt.get_cmap(config["cmap"])
    colored = cmap(normed)  # returns RGBA float 0-1

    # Build output array
    out = np.zeros_like(arr)
    out[:, :, 0] = (colored[:, :, 0] * 255).astype(np.uint8)
    out[:, :, 1] = (colored[:, :, 1] * 255).astype(np.uint8)
    out[:, :, 2] = (colored[:, :, 2] * 255).astype(np.uint8)
    out[:, :, 3] = arr[:, :, 3].astype(np.uint8)  # preserve original alpha/transparency

    # Zero out non-land pixels (keep them transparent)
    out[~land_mask] = [0, 0, 0, 0]

    out_img = Image.fromarray(out.astype(np.uint8), "RGBA")
    out_img.save(src_path)  # overwrite in place
    print(f"  Recolored: {filename}  ({config['cmap']})")


if __name__ == "__main__":
    print("Recoloring prediction maps with Option B colormaps...")
    print(f"Working in: {ASSETS}\n")

    # Backup originals first
    archive = ASSETS / "asset_archive" / "originals_before_recolor"
    archive.mkdir(parents=True, exist_ok=True)

    for filename in CONFIGS:
        src = ASSETS / filename
        if src.exists():
            backup = archive / filename
            if not backup.exists():
                import shutil

                shutil.copy2(src, backup)
                print(f"  Backed up: {filename}")
        else:
            print(f"  WARNING: {filename} not found, skipping")

    print()
    for filename, config in CONFIGS.items():
        src = ASSETS / filename
        if src.exists():
            recolor(filename, config)
        else:
            print(f"  SKIP: {filename} not found")

    print("\nDone! Refresh your browser to see the new colors.")
    print(f"Originals backed up to: {archive}")
