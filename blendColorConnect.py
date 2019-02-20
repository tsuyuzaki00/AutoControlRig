import pymel.core as pm
import maya.cmds as cmds

cmds.shadingNode('blendColors', asUtility=True, n='hand_blendColor_L')

cmds.connectAttr('hand_jntPrxIK_L.translate', 'hand_blendColor_L.color1')
cmds.connectAttr('hand_jntPrxFK_L.translate', 'hand_blendColor_L.color2')
cmds.connectAttr('hand_blendColor_L.output', 'hand_jnt_L.translate')
