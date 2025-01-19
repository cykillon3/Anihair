import bpy


operator = bpy.types.Operator


class create_curve(operator):
    bl_idname = "create_curve.curve_operator"
    bl_label = "Create new hair"
    bl_description = "Description that shows in blender tooltips"
    bl_options = {"REGISTER"}

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        bpy.ops.curve.primitive_nurbs_circle_add()
        return {"FINISHED"}
