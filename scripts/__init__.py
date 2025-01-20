

import bpy
from .main import *
from .operators import *

classes = (main_panel, create_curve, edit_curve, convert_curve,)



def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
        
if __name__ == "__main__":
    register()
        
