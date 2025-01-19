import bpy

panel = bpy.types.Panel

category_name = "AniHair"

class main_panel(panel):
    bl_label = "Main Panel"
    bl_idname = "PT_main_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = category_name
    
    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.label(text="Hello world!", icon='WORLD_DATA')
        
        row = layout.row()
        row.operator("wm.open_url", text="Open Blender", icon='WORLD_DATA').url = "https://www.blender.org/"
        
        row = layout.row()
        row.operator("wm.open_url", text="Open Google", icon='WORLD_DATA').url = "https://www.google.com/"
        
        row = layout.row()
        row.operator("wm.open_url", text="Open Youtube", icon='WORLD_DATA').url = "https://www.youtube.com/"
        
        row = layout.row()
        row.operator("wm.open_url", text="Open Github", icon='WORLD_DATA').url = "https://www.github.com/"