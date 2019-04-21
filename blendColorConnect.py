import pymel.core as pm



pm.connectAttr( +'.FKIK', +'translateBlend_L.blender')
pm.connectAttr( +'.FKIK', +'translateBlend_R.blender')

pm.connectAttr('hand_jntPrxIK_L.translate', 'hand_blendColor_L.color1')
pm.connectAttr('hand_jntPrxFK_L.translate', 'hand_blendColor_L.color2')
pm.connectAttr('hand_blendColor_L.output', 'hand_jnt_L.translate')
