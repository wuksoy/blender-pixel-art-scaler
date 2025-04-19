# Pixel Art Scaler (Blender Addon)

A simple Blender addon to scale pixel art image sequences using nearest-neighbor filtering — perfect for upscaling retro-style sprite sheets or frame sequences without any blurring.

---

## Features

- Scales PNG, JPG, and JPEG images
- Preserves crisp edges using nearest-neighbor interpolation
- Fully integrated panel in the **Image Editor > Sidebar**
- Batch processes all images in a folder
- Uses Pillow (Python Imaging Library), bundled with the addon

---

## Installation

1. [Download the latest release](https://github.com/wuksoy/blender-pixel-art-scaler/releases) (`.zip` file)
2. Open Blender and go to **Edit > Preferences > Add-ons**
3. Click **Install**, select the `.zip` file, then enable the addon
4. Go to **Image Editor > Sidebar > Pixel Scaler** tab

---

## Usage

1. Create or open a `.blend` file.
2. Go to Rendering Tab
3. In the Pixel Scaler panel:
   - Select your **Input Folder** (with images to scale)
   - Select an **Output Folder**
   - Choose a **Scale Factor** (e.g. 2 = double the size)
4. Click **Scale Pixel Art Images**
5. Done! Scaled images will be saved in the output folder.

---

## Requirements

- Blender 2.93+ (tested with 4.x)
- No external installs required — Pillow is bundled

---

## Credits

Made with ❤️ by [Wuksoy](https://github.com/wuksoy)

---

## License

MIT License — free to use, modify, and distribute.
