import pymel.core as pm

selects = pm.ls(sl=True, dag=True)

for ctrl in selects:
    if ctrl.nodeType() == 'nurbsCurve':
        pm.setAttr( ctrl+'.overrideEnabled', 1)
        pm.setAttr( ctrl+'.overrideColor', 6)#Left
        pm.setAttr( ctrl+'.overrideColor', 14)#Right