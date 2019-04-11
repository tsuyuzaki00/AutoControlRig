import pymel.core as pm

pm.select('jnt_set')
jnts = pm.ls(sl=True, dag=True)

pm.select('jntPrx_set')
jntPrxs = pm.ls(sl=True, dag=True)

for i in range(4):
    pm.connectAttr( jnts[i]+'.'+'translate', jntPrxs[i]+'.'+'translate',f=True )
    pm.connectAttr( jnts[i]+'.'+'rotate', jntPrxs[i]+'.'+'rotate',f=True )