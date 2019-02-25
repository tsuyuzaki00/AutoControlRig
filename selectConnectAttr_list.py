import maya.cmds as cmds   

sel = cmds.ls(sl=True, dag=True)

cmds.duplicate(n='joint',rc=True)
sel2 = cmds.ls(sl=True, dag=True)

transAttr = 'translate'
rotateAttr = 'rotate'

for i in range(len(sel)):
    cmds.connectAttr( sel2[i]+'.'+transAttr, sel[i]+'.'+transAttr,f=True )
    cmds.connectAttr( sel2[i]+'.'+rotateAttr, sel[i]+'.'+rotateAttr,f=True )