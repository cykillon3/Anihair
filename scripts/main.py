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
        row.operator("edit_curve.curve_operator01", icon='CURVE_BEZCURVE')
        row = layout.row()
        row.operator("add_mirror_modifier.curve_operator03", icon='MOD_MIRROR')
        row = layout.row()
        row.operator("convert_curve.curve_operator02", icon='CURVE_DATA')

class patreon_panel(panel):
    bl_label = "Credits"
    bl_idname = "PT_patreon_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = category_name
    bl_parent_id = "PT_main_panel"
    
    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.label(text="💟 Become a patron",)
        row = layout.row()
        row.operator("wm.url_open", text="Patreon 💖").url = "https://www.patreon.com/CYkillon3"
        row = layout.row()
        row.operator("wm.url_open", text="Join our Discord 💬").url = "https://discord.gg/RNYSBDGyxC"
        
        
        
        row = layout.row()
        row.label(text="CY's Army:")
        
