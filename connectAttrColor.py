import pymel.core as pm

pm.select('jntPrx_set')
jntPrxs = pm.ls(sl=True, dag=True)

pm.select('jntFK_set')
jntFKs = pm.ls(sl=True, dag=True)

pm.select('jntIK_set')
jntIKs = pm.ls(sl=True, dag=True)

for i in range(10):
    pm.connectAttr( jntFKs[i]+'.'+'rotate', jntPrxs[i]+'.'+'color2',f=True )
    pm.connectAttr( jntIKs[i]+'.'+'rotate', jntPrxs[i]+'.'+'color1',f=True )
    pm.connectAttr( blendColors[i]+'.'+'output', jntPrxs[i]+'.'+'rotate',f=True )
