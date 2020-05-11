import pymel.core as pm

sel = pm.selected()
shapes = pm.listRelatives(sel[0:])

for shape in shapes:
    pm.setAttr(shape+'.overrideEnabled',1)
    pm.setAttr(shape+'.overrideColor',18)