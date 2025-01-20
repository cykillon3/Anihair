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
        
        hair_id = len(bpy.data.objects)
        
        bpy.ops.curve.primitive_bezier_circle_add(rotation=(1.5708, 0, 0))
        hair_shape = bpy.context.object
        hair_shape.name = f"Hair Shape{hair_id}"
        hair_shape.data.resolution_u = 5
        
        
        bpy.ops.curve.primitive_nurbs_path_add(location=(3, 0, 0), rotation=(0, 0, 1.5708))
        hair_strand = bpy.context.object
        hair_strand.name = f"Hair Strand{hair_id}"
        hair_strand.data.resolution_u = 3
        hair_strand.data.bevel_mode = 'OBJECT'
        hair_strand.data.bevel_object = hair_shape
        hair_strand.data.splines[0].resolution_u = 3

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
        #bpy.ops.object.select_all(action='DESELECT')
        
        # Select the curve object (assuming the curve is named "NurbsCircle")
        curve_object = bpy.context.view_layer.objects.active
        if curve_object:
            curve_object.select_set(True)
            context.view_layer.objects.active = curve_object
            
            # Check if the object is in 'EDIT' mode
            if bpy.context.object.mode == 'EDIT':
                bpy.ops.object.mode_set(mode='OBJECT')
            
            # Set the mode to 'EDIT'
            bpy.ops.object.mode_set(mode='EDIT')
            bpy.ops.view3d.view_axis(type='FRONT', align_active=False)
            bpy.context.space_data.region_3d.view_perspective = 'ORTHO'

        return {"FINISHED"}



