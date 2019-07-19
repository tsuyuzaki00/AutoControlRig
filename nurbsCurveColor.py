import pymel.core as pm

pm.select('shoulder_ctrl_L')
selects = pm.ls(sl=True, dag=True)

for ctrl in selects:
    if ctrl.nodeType() == 'nurbsCurve':
        pm.setAttr( ctrl+'.overrideEnabled', 1)
        pm.setAttr( ctrl+'.overrideColor', 6)
        
        if '_ctrlFK' in ctrl.name():
            pm.connectAttr( 'humanRigKit_armFKIK_ctrl_L.FKIK', ctrl+'.visibility' )