import pymel.core as pm

pm.select('upArmTwist_jntPrx_R','lowArmTwist_jntPrx_R')
jntPrxs = pm.ls(sl=True)

pm.select('upArmTwist_jntIK_R','lowArmTwist_jntIK_R')
jntIKs = pm.ls(sl=True)

pm.select('upArmTwist_jntFK_R','lowArmTwist_jntFK_R')
jntFKs = pm.ls(sl=True)

pm.select('upArmTwist_rotateBlend_R','lowArmTwist_rotateBlend_R')
rollblend = pm.ls(sl=True)

pm.select('upArmTwist_translateBlend_R','lowArmTwist_translateBlend_R')
trsblend = pm.ls(sl=True)

for i in range(len(jntIKs)):
    pm.connectAttr( jntIKs[i]+'.'+'translate', trsblend[i]+'.'+'color1',f=True )
    pm.connectAttr( jntFKs[i]+'.'+'translate', trsblend[i]+'.'+'color2',f=True )
    pm.connectAttr( trsblend[i]+'.'+'output', jntPrxs[i]+'.'+'translate',f=True )
    
    pm.connectAttr( jntIKs[i]+'.'+'rotate', rollblend[i]+'.'+'color1',f=True )
    pm.connectAttr( jntFKs[i]+'.'+'rotate', rollblend[i]+'.'+'color2',f=True )
    pm.connectAttr( rollblend[i]+'.'+'output', jntPrxs[i]+'.'+'rotate',f=True )