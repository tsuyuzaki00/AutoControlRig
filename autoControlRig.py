import pymel.core as pm
import maya.cmds as cmds

def main()
    sel = pm.ls(sl=True, dag=True)
    pm.duplicate(n='joint',rc=True)
    sel2 = pm.ls(sl=True, dag=True)

    mae = sel
    ushiro = sel2

    for output,input in zip(mae,ushiro):
        pm.connectAttr(output+'.translate', input+'.translate')
        pm.connectAttr(output+'.rotate', input+'.rotate')
