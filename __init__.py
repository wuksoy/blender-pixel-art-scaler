bl_info = {
    "name": "Pixel Art Scaler",
    "author": "Wuksoy",
    "version": (1, 0),
    "blender": (2, 93, 0),
    "location": "Image Editor > Tools",
    "description": "Scales pixel art image sequences with nearest-neighbor filtering.",
    "warning": "",
    "wiki_url": "https://github.com/wuksoy/blender-pixel-art-scaler",
    "tracker_url": "https://github.com/wuksoy/blender-pixel-art-scaler/issues",
    "support": "COMMUNITY",
    "category": "Image",
}

import sys
import os

addon_dir = os.path.dirname(__file__)
if addon_dir not in sys.path:
    sys.path.append(addon_dir)

from . import scaler

def register():
    scaler.register()

def unregister():
    scaler.unregister()