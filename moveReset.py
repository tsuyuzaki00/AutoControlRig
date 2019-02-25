import maya.cmds as cmds

def main():
    sel = pm.ls(sl=True)
    cmds.move( 0, 0, 0 )
