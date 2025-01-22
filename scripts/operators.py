import bpy


operator = bpy.types.Operator


class create_curve(operator):
    bl_idname = "create_curve.curve_operator"
    bl_label = "Create new hair"
    bl_description = "Creates a new hair strand"
    bl_options = {"REGISTER"}

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        
        hair_id = len(bpy.data.objects)
        
        # Spawn a new bezier circle
        bpy.ops.curve.primitive_bezier_circle_add(radius=(0.01), rotation=(1.5708, 0, 0))
        hair_shape = bpy.context.object
        hair_shape.name = f"Hair Shape{hair_id}"
        hair_shape.data.resolution_u = 5
        
        # Spawn a new nurbs path
        bpy.ops.curve.primitive_nurbs_path_add( location=(0.1, 0, 0), rotation=(1.5708, -1.5708, 0))
        hair_strand = bpy.context.object
        hair_strand.name = f"Hair Strand{hair_id}"
        hair_strand.data.resolution_u = 3
        hair_strand.data.bevel_mode = 'OBJECT'
        hair_strand.data.bevel_object = hair_shape
        hair_strand.data.splines[0].resolution_u = 3
        bpy.ops.transform.resize(value=(1, 1, 0.1))
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
        
        
        self.report({'INFO'}, f'hair strand {hair_id} created')

        return {"FINISHED"}


class edit_curve(operator):
    bl_idname = "edit_curve.curve_operator01"
    bl_label = "Edit hair"
    
    bl_description = "Edits created the selected hair strand"
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
            if bpy.context.object and bpy.context.object.type == 'CURVE' and bpy.context.object.data.splines[0].type == 'BEZIER':
                bpy.ops.object.mode_set(mode='EDIT')
                bpy.ops.view3d.view_axis(type='FRONT', align_active=False)
                bpy.context.space_data.region_3d.view_perspective = 'ORTHO'
            else:
                self.report({'INFO'}, 'Please select a hair shape object')

        return {"FINISHED"}

class add_mirror_modifier(operator):
    bl_idname = "add_mirror_modifier.curve_operator03"
    bl_label = "Add mirror modifier"
    bl_description = "Adds a mirror modifier to the selected hair strand"
    bl_options = {"REGISTER", "UNDO"}
    
    @classmethod
    def poll(cls, context):
        return True
    
    def execute(self, context):
        # Deselect all objects
        bpy.ops.object.select_all(action='DESELECT')

        active_object = bpy.context.view_layer.objects.active
        
        if active_object and active_object.type == 'CURVE' and active_object.data.splines[0].type == 'NURBS':
            active_object.select_set(True)
            bpy.ops.object.modifier_add(type='MIRROR')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            self.report({'INFO'}, 'Mirror modifier added to the hair')
            return {"FINISHED"}
        else:
            self.report({'WARNING'}, 'Please select a Hair strand object first')
            return {"CANCELLED"}
            

class convert_curve(operator):
    bl_idname = "convert_curve.curve_operator02"
    bl_label = "Convert all hair to mesh"
    bl_description = "Converts all hair strands to mesh"
    bl_options = {"REGISTER", "UNDO"}
    
    @classmethod
    def poll(cls, context):
        return True
    
    def execute(self, context):
        # Deselect all objects
        bpy.ops.object.select_all(action='DESELECT')

        try:
        # Select all NURBS curves
            nurbs_selected = False
            for obj in bpy.data.objects:
                if obj.type == 'CURVE' and obj.data.splines[0].type == 'NURBS':
                    obj.select_set(True)
                    nurbs_selected = True

            # Ensure we are in object mode
            if bpy.context.object and bpy.context.object.mode != 'OBJECT':
                bpy.ops.object.mode_set(mode='OBJECT')

            # Convert selected NURBS curves to mesh if any are selected
            if nurbs_selected:
                bpy.ops.object.convert(target='MESH')
                self.report({'INFO'}, 'NURBS curves converted to mesh')
            else:
                self.report({'WARNING'}, 'No NURBS curves found to convert')
                
        except RuntimeError:
            self.report({'ERROR'}, 'Please select a Hair strand object first')

        return {"FINISHED"}