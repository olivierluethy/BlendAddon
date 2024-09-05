import bpy

# Get the selected objects
selected_objects = bpy.context.selected_objects

# Define the addon name and description
bl_info = {
    "name": "VirtualPainter",
    "description": "A basic Blender addon",
    "author": "Andrin, Marco, Olivier",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Tool Shelf > My Addon",
    "category": "Misc"
}

# Define the addon's functionality
class MyAddon(bpy.types.Panel):
    bl_label = "VirtualPainter"
    bl_idname = "VIEW3D_PT_my_addon"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'

    def draw(self, context):
        layout = self.layout
        layout.label(text="Hello, World!")

        for obj in selected_objects:
            layout.label(text="Object Type: " + obj.type)
            layout.label(text="Object Face: " + obj.data.faces)
            # Check if the object has mesh data
            if obj.type == 'MESH':
                layout.label(text="Polygon Info: " + obj.data.polygons)

# Register the addon
def register():
    bpy.utils.register_class(MyAddon)

# Unregister the addon
def unregister():
    bpy.utils.unregister_class(MyAddon)

if __name__ == "__main__":
    register()