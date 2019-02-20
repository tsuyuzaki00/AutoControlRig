import maya.cmds as cmds

sel = pm.ls(sl=True, dag=True)

cmds.duplicate(n='joint',rc=True)
sel2 = pm.ls(sl=True, dag=True)

print sel
print sel2
