import pymel.core as pm

pm.select('jnt_set')
jnts = pm.ls(sl=True, dag=True)

pm.select('jntPrx_set')
jntPrxs = pm.ls(sl=True, dag=True)

for i in range(len(jnts)):
    pm.connectAttr( jntPrxs[i]+'.'+'translate', jnts[i]+'.'+'translate',f=True )
    pm.connectAttr( jntPrxs[i]+'.'+'rotate', jnts[i]+'.'+'rotate',f=True )