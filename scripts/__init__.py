

bl_info = {
    "name": "AniHair",
    "author": "Cykillon3",
    "description": "",
    "blender": (2, 80, 0),
    "version": (0, 0, 1),
    "location": "",
    "warning": "",
    "category": "addon",
}


import bpy
from .main import *
from .operators import *

classes = (main_panel, create_curve, edit_curve, convert_curve, add_mirror_modifier, patreon_panel)



def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
        
if __name__ == "__main__":
    register()
        
