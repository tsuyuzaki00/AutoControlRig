import maya.cmds as cmds
import pymel.core as pm

trsList = cmds.ls(v=True,tr=True)
print trsList

ctl = pm.selected()[0]
obj = pm.selected()[1]

outAttr = 'translate'
inAttr = 'color1'
pm.connectAttr( ctl.name()+'.'+outAttr, obj.name()+'.'+inAttr,f=True )
