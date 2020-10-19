import pymel.core as pm
import maya.mel as mel

#public
width = 16
Ucount = 8
length = 1.5

#private
melUcount = Ucount + 1
nurbsName = 'C_ribbon_nurb_scene_00'
hairName = 'C_hairSystem_null_scene_00'

pm.nurbsPlane( ax = [0, 1, 0], d = 1, w = width, u = Ucount, v = 1, lr = length * 0.1, ch = False, n = nurbsName)
mel.eval('string $Ucount = "%s";' % melUcount)
#createHair(name Ucount,Vcount,PointPerHair,CreateRestCurves,PassiveFill,EdgeBounded,Equalize,Length,Randomization,Output,Dynamic||Static,PlaceHairsInto)
mel.eval('createHair $Ucount 1 10 0 0 1 0 5 0 2 1 1')
hairParents = pm.rename('hairSystem1Follicles', hairName)
pm.delete('nucleus1', 'hairSystem1OutputCurves','hairSystem1')
parentFollicle = pm.listRelatives(hairParents, c = True)
for follicle in parentFollicle:
    deleteCurve = pm.listRelatives(follicle , c = True, typ = 'transform')
    pm.delete(deleteCurve[0])
    pm.select(follicle)
    pm.rename(follicle, 'C_hair_foll_scene_00')
    pm.joint(r = True, rad= 0.1, n = 'C_hair_jnt_scene_00')