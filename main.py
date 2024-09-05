import bpy

# Define the addon name and description
bl_info = {
    "name": "RenderAddon",
    "description": "A basic Blender addon",
    "author": "Your Name",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Tool Shelf > My Addon",
    "category": "Misc"
}

# Define the addon's functionality
class MyAddon(bpy.types.Panel):
    bl_label = "My Addon"
    bl_idname = "VIEW3D_PT_my_addon"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'

    def draw(self, context):
        layout = self.layout
        layout.label(text="Hello, World!")

# Register the addon
def register():
    bpy.utils.register_class(MyAddon)

# Unregister the addon
def unregister():
    bpy.utils.unregister_class(MyAddon)

if __name__ == "__main__":

    
    register()