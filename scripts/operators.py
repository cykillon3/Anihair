import bpy


operator = bpy.types.Operator


class create_curve(operator):
    bl_idname = "create_curve.curve_operator"
    bl_label = "Create new hair"
    bl_description = "Creates a new hair"
    bl_options = {"REGISTER"}

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        bpy.ops.curve.primitive_nurbs_circle_add(rotation=(1.5708, 0, 0))
        bpy.context.object.name = "Hair"
        return {"FINISHED"}


class edit_curve(operator):
    bl_idname = "edit_curve.curve_operator01"
    bl_label = "Edit hair"
    bl_description = "Edits created hair"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        bpy.ops.object.select_all(action='DESELECT')
        
        # Select the curve object (assuming the curve is named "NurbsCircle")
        curve_object = bpy.data.objects.get("Hair")
        if curve_object:
            curve_object.select_set(True)
            context.view_layer.objects.active = curve_object
            
            # Set the mode to 'EDIT'
            bpy.ops.object.mode_set(mode='EDIT')
            bpy.ops.view3d.view_axis(type='FRONT', align_active=False)
            bpy.context.space_data.region_3d.view_perspective = 'ORTHO'
        return {"FINISHED"}



