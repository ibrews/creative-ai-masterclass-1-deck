"""Run in Blender background mode with -- --out NEW_DIR --rails vermilion|jade."""
import argparse
from pathlib import Path
import math
import sys
import bpy
from mathutils import Vector

parser = argparse.ArgumentParser()
parser.add_argument("--out", type=Path, required=True)
parser.add_argument("--rails", choices=["vermilion", "jade"], default="vermilion")
args = parser.parse_args(sys.argv[sys.argv.index("--") + 1:])
out = args.out.resolve()
out.mkdir(parents=True, exist_ok=False)
bpy.ops.wm.read_factory_settings(use_empty=True)
scene = bpy.context.scene
scene.unit_settings.system = 'METRIC'
def stock(name, rgb):
    mat = bpy.data.materials.new(name)
    mat.diffuse_color = (*rgb, 1)
    mat.use_nodes = True
    shader = mat.node_tree.nodes.get("Principled BSDF")
    shader.inputs['Base Color'].default_value = (*rgb, 1)
    shader.inputs['Roughness'].default_value = 0.78
    return mat
paper = stock("Ivory card", (.94,.75,.48))
pink = stock("Clay paper", (.76,.32,.22))
roof = stock("Folded ochre", (.8,.35,.065))
water = stock("Midnight river", (.033,.16,.21))
island = stock("Stone paper", (.21,.31,.29))
rail = stock(args.rails.title(), (.84,.065,.025) if args.rails=="vermilion" else (.03,.43,.24))
glow = stock("Lantern gold", (1,.70,.26))
def box(name, xyz, dims, mat):
    bpy.ops.mesh.primitive_cube_add(size=1, location=xyz)
    obj=bpy.context.object
    obj.name=name
    obj.dimensions=dims
    bpy.ops.object.transform_apply(location=False,rotation=False,scale=True)
    obj.data.materials.append(mat)
    return obj
def folded_roof(x, height, i):
    z=height-.65
    vertices=[(x+dx,1.3+dy,h) for dx,dy,h in [(-.78,-.68,z),(.78,-.68,z),(0,-.68,height),(-.78,.68,z),(.78,.68,z),(0,.68,height)]]
    mesh=bpy.data.meshes.new("Fold");mesh.from_pydata(vertices,[],[(0,1,2),(5,4,3),(0,3,4,1),(1,4,5,2),(2,5,3,0)]);mesh.update()
    obj=bpy.data.objects.new(f"Tower {i} folded roof",mesh);scene.collection.objects.link(obj);obj.data.materials.append(roof)
box("River plinth",(0,0,-.31),(10,7,.40),water)
box("North bank",(0,1.65,-.08),(9,2.7,.16),island)
box("Lantern quay",(-1.8,-2.45,-.08),(3.5,1.25,.16),island)
for i,(x,h) in enumerate([(-2.5,2),(0,3),(2.5,4)],1):
    wall=h-.65
    box(f"Tower {i} wall",(x,1.3,wall/2),(1.43,1.24,wall),[paper,pink,paper][i-1])
    folded_roof(x,h,i)
    for level in range(1,h):
        for offset in (-.35,.35):
            box(f"Tower {i} window {level}",(x+offset,.668,level-.4),(.22,.035,.32),glow)
box("Footbridge",(-1.8,-.78,.06),(1.30,2.64,.12),paper)
for x in (-2.4,-1.2):
    box("Bridge rail",(x,-.78,.63),(.10,2.65,.12),rail)
    for y in (-2,-.78,.45):box("Bridge post",(x,y,.34),(.10,.10,.62),rail)
for x in (-2.35,-1.25):box("Lantern Gate post",(x,-2.45,.63),(.15,.15,1.26),roof)
box("Lantern Gate lintel",(-1.8,-2.45,1.27),(1.55,.28,.19),roof)
box("Lantern",(-1.8,-2.45,1.04),(.28,.25,.31),glow)
def aim(obj,target):obj.rotation_euler=(Vector(target)-obj.location).to_track_quat('-Z','Y').to_euler()
bpy.ops.object.camera_add(location=(8,-16,9));cam=bpy.context.object;aim(cam,(0,0,1.15));cam.data.type='ORTHO';cam.data.ortho_scale=11.5;scene.camera=cam
for pos,energy,size in [((-5,-7,10),1700,7),((7,1,8),1100,6)]:
    bpy.ops.object.light_add(type='AREA',location=pos);light=bpy.context.object;aim(light,(0,0,0));light.data.energy=energy;light.data.shape='DISK';light.data.size=size
scene.world=bpy.data.worlds.new('Dusk');scene.world.use_nodes=True;scene.world.node_tree.nodes['Background'].inputs[0].default_value=(.18,.20,.27,1)
scene.render.engine='CYCLES';scene.cycles.samples=12;scene.cycles.use_denoising=True;scene.render.resolution_x=960;scene.render.resolution_y=640;scene.render.resolution_percentage=100
for area in bpy.context.screen.areas:
    if area.type=='VIEW_3D':area.spaces.active.region_3d.view_perspective='CAMERA';area.spaces.active.shading.color_type='MATERIAL'
scene.render.filepath='//Postcard.png'
bpy.ops.wm.save_as_mainfile(filepath=str(out/'Paper City.blend'))
bpy.ops.render.render(write_still=True)
bpy.ops.export_scene.gltf(filepath=str(out/'Paper City.glb'), export_cameras=False,export_lights=False)
print(f"SW-17: three roofs at 2, 3, 4 m; rails {args.rails}; wrote {out}")
