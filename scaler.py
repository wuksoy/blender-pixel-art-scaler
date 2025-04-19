
import bpy
from bpy.props import StringProperty, IntProperty
from bpy.types import Operator, Panel
import os
from PIL import Image


class PIXELART_OT_ScaleImages(Operator):
    bl_idname = "pixelart.scale_images"
    bl_label = "Scale Pixel Art Images"

    def execute(self, context):
        input_folder = bpy.path.abspath(context.scene.pixelart_input)
        output_folder = bpy.path.abspath(context.scene.pixelart_output)
        scale_factor = context.scene.pixelart_scale

        os.makedirs(output_folder, exist_ok=True)

        for fname in os.listdir(input_folder):
            if fname.lower().endswith(('.png', '.jpg', '.jpeg')):
                in_path = os.path.join(input_folder, fname)
                out_path = os.path.join(output_folder, fname)

                with Image.open(in_path) as img:
                    new_size = (img.width * scale_factor, img.height * scale_factor)
                    scaled = img.resize(new_size, resample=Image.NEAREST)
                    scaled.save(out_path)

        self.report({'INFO'}, f"Scaled images saved to {output_folder}")
        return {'FINISHED'}


class PIXELART_PT_Panel(Panel):
    bl_label = "Pixel Art Scaler"
    bl_idname = "PIXELART_PT_panel"
    bl_space_type = 'IMAGE_EDITOR'
    bl_region_type = 'UI'
    bl_category = "Pixel Scaler"

    def draw(self, context):
        layout = self.layout
        layout.prop(context.scene, "pixelart_input")
        layout.prop(context.scene, "pixelart_output")
        layout.prop(context.scene, "pixelart_scale")
        layout.operator("pixelart.scale_images")


def register():
    bpy.utils.register_class(PIXELART_OT_ScaleImages)
    bpy.utils.register_class(PIXELART_PT_Panel)
    bpy.types.Scene.pixelart_input = StringProperty(name="Input Folder", subtype='DIR_PATH')
    bpy.types.Scene.pixelart_output = StringProperty(name="Output Folder", subtype='DIR_PATH')
    bpy.types.Scene.pixelart_scale = IntProperty(name="Scale Factor", default=2, min=1)


def unregister():
    bpy.utils.unregister_class(PIXELART_OT_ScaleImages)
    bpy.utils.unregister_class(PIXELART_PT_Panel)
    del bpy.types.Scene.pixelart_input
    del bpy.types.Scene.pixelart_output
    del bpy.types.Scene.pixelart_scale


if __name__ == "__main__":
    register()