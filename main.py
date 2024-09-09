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

class ObjectInfoPanel(bpy.types.Panel):
    bl_idname = "Virtual Painter"
    bl_label = "Object Info"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'

    def draw(self, context):
        layout = self.layout
        obj = context.object
        if obj:
            layout.label(text="Object Type: " + obj.type)
            if obj.type == 'MESH':
                layout.label(text="Object Face: " + str(len(obj.data.polygons)))
                layout.label(text="Polygon Info: " + str(obj.data.polygons))

def register():
    bpy.utils.register_class(ObjectInfoPanel)

def unregister():
    bpy.utils.unregister_class(ObjectInfoPanel)

if __name__ == "__main__":
    register()