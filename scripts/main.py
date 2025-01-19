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
        row.label(text="AniHair Menu", icon='IPO_EASE_IN')
        row = layout.row()
        row.operator("create_curve.curve_operator", icon='CURVE_DATA')
        row = layout.row()
        row.operator("edit_curve.curve_operator01", icon='CURVE_DATA')



        
        


    