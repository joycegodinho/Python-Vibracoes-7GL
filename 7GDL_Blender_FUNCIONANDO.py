import bpy
import csv
import numpy as np
import time
import math

fpath = 'C:/7GDL_Resposta4.csv'
csvFile = csv.reader(open(fpath))
data = [row for row in csvFile][0:]
data_7gdl = []
response = []

L1 = (3/5)*1.7
L2 = 1.7-L1
L3 = 1.4

for i in range(len(data)):
    data_list = data[i]
    data_str = data_list[0]
    data_float = [float(x) for x in data_str.split(' ')]
    if i == 0:
        gdls = len(data_float)
    data_7gdl.append(data_float)
    
for i in range(gdls):
    response_col = []
    for j in range(len(data)):
        data_point = data_7gdl[j][i]
        response_col.append(data_point)
    response.append(response_col)


resp_1 = response[0]
resp_2 = response[1]
resp_3 = response[2]
resp_4 = response[3]
resp_5 = response[4]
resp_6 = response[5] 
resp_7 = response[6]

#for i in range(len(resp_6)):
#    resp_6[i] = resp_6[i] 

op1 = bpy.ops.mesh.primitive_cylinder_add(radius= 0.25, depth=0.15, enter_editmode=False, align='CURSOR', location=(L1, L3/2, 0), rotation=(math.pi/2, 0, 0), scale=(1, 1, 1))
op2 = bpy.ops.mesh.primitive_cylinder_add(radius= 0.25, depth=0.15, enter_editmode=False, align='CURSOR', location=(L1, -L3/2, 0), rotation=(math.pi/2, 0, 0), scale=(1, 1, 1))
op3 = bpy.ops.mesh.primitive_cylinder_add(radius= 0.25, depth=0.15, enter_editmode=False, align='CURSOR', location=(-L2, -L3/2, 0), rotation=(math.pi/2, 0, 0), scale=(1, 1, 1))
op4 = bpy.ops.mesh.primitive_cylinder_add(radius= 0.25, depth=0.15, enter_editmode=False, align='CURSOR', location=(-L2, L3/2, 0), rotation=(math.pi/2, 0, 0), scale=(1, 1, 1))
op5 = bpy.ops.mesh.primitive_cube_add(size=0.5, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))

#op1 = bpy.ops.mesh.primitive_uv_sphere_add(radius=0.3, enter_editmode=False, align='WORLD', location=(L1, L3/2, 0), scale=(1, 1, 1))
#op2 = bpy.ops.mesh.primitive_uv_sphere_add(radius=0.3, enter_editmode=False, align='WORLD', location=(L1, -L3/2, 0), scale=(1, 1, 1))
#op3 = bpy.ops.mesh.primitive_uv_sphere_add(radius=0.3, enter_editmode=False, align='WORLD', location=(-L2, -L3/2, 0), scale=(1, 1, 1))
#op4 = bpy.ops.mesh.primitive_uv_sphere_add(radius=0.3, enter_editmode=False, align='WORLD', location=(-L2, L3/2, 0), scale=(1, 1, 1))
#op5 = bpy.ops.mesh.primitive_plane_add(size=0.7, calc_uvs=True, enter_editmode=False, align='CURSOR', location=(0, 0, L1/3), rotation=(0,math.pi/2, 0), scale=(1, 1, 1))
#bpy.context.active_object.name = 'Plano_Chassi'


## Go to edit mode, face selection mode and select all faces
#bpy.ops.object.mode_set( mode   = 'EDIT'   )
#bpy.ops.mesh.select_mode( type  = 'FACE'   )
#bpy.ops.mesh.select_prev_item()

#bpy.ops.mesh.extrude_region_move(
#    TRANSFORM_OT_translate={"value":(1, 0, 0)}
#)

#bpy.ops.object.mode_set( mode = 'OBJECT' )


sphere1 = bpy.data.collections[0].objects['Cylinder']
sphere2 = bpy.data.collections[0].objects['Cylinder.001']
sphere3 = bpy.data.collections[0].objects['Cylinder.002']
sphere4 = bpy.data.collections[0].objects['Cylinder.003']
sphere5 = bpy.data.collections[0].objects['Cube']
frame_num = 0

for i in range(len(data)):
    
    bpy.context.scene.frame_set(frame_num)
    sphere1.location = (L1, L3/2,resp_1[i])
    sphere1.keyframe_insert(data_path = "location", frame = frame_num)
    sphere2.location = (L1, -L3/2,resp_2[i])
    sphere2.keyframe_insert(data_path = "location", frame = frame_num)
    sphere3.location = (-L2, -L3/2,resp_3[i])
    sphere3.keyframe_insert(data_path = "location", frame = frame_num)
    sphere4.location = (-L2, L3/2,resp_4[i])
    sphere4.keyframe_insert(data_path = "location", frame = frame_num)
    sphere5.location = (0,0,L1/3 + resp_5[i])
    obj = bpy.context.window.scene.objects[0]
    bpy.context.view_layer.objects.active = obj 
    bpy.ops.transform.rotate(value=resp_6[i], orient_axis='Y', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, release_confirm=True)
    bpy.ops.transform.rotate(value=resp_7[i], orient_axis='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, release_confirm=True)
    sphere5.keyframe_insert(data_path = "rotation_euler", frame = frame_num)
    sphere5.keyframe_insert(data_path = "location", frame = frame_num)
    frame_num += 5
    
#bpy.ops.material.new()
#bpy.data.materials["Material"].node_tree.nodes["Emission"].inputs[0].default_value = (0.0217484, 0.898564, 1, 1)
#bpy.data.materials["Material"].node_tree.nodes["Emission"].inputs[1].default_value = 2.4
#bpy.ops.object.modifier_add(type='WIREFRAME')
#bpy.ops.object.make_links_data(type='MODIFIERS')
#bpy.ops.object.make_links_data(type='MATERIAL')
