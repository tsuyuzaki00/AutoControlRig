import pymel.core as pm

selects = pm.ls(sl=True, dag=True)

for allKey in selects:
    if allKey.nodeType() == 'transform':
        if '_ctrl' in allKey.name():
            pm.setKeyframe(allKey)