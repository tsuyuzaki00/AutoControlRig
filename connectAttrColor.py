import pymel.core as pm

jointName = 'lowLeg'
RL = 'L'

pm.select(jointName + '_jntPrx_' + RL)
jntPrxs = pm.ls(sl=True)

pm.select(jointName + '_jntFK_' + RL)
jntFKs = pm.ls(sl=True)

pm.select(jointName + '_jntIK_' + RL)
jntIKs = pm.ls(sl=True)

pm.select(jointName + '_rotateBlend_' + RL)
rotateBlends = pm.ls(sl=True)

pm.select(jointName + '_translateBlend_' + RL)
translateBlends = pm.ls(sl=True)

for i in range(len(jntPrxs)):
    pm.connectAttr( jntFKs[i]+'.'+'rotate', rotateBlends[i]+'.'+'color2',f=True )
    pm.connectAttr( jntIKs[i]+'.'+'rotate', rotateBlends[i]+'.'+'color1',f=True )
    pm.connectAttr( rotateBlends[i]+'.'+'output', jntPrxs[i]+'.'+'rotate',f=True )

for i in range(len(jntPrxs)):
    pm.connectAttr( jntFKs[i]+'.'+'translate', translateBlends[i]+'.'+'color2',f=True )
    pm.connectAttr( jntIKs[i]+'.'+'translate', translateBlends[i]+'.'+'color1',f=True )
    pm.connectAttr( translateBlends[i]+'.'+'output', jntPrxs[i]+'.'+'translate',f=True )