import pymel.core as pm

name = 'root'

pm.select(name + '_jnt')
jnts = pm.ls(sl=True, dag=True)

pm.select(name + '_jntPrx')
jntPrxs = pm.ls(sl=True, dag=True)

for i in range(len(jnts)):
    pm.connectAttr( jntPrxs[i]+'.'+'translate', jnts[i]+'.'+'translate',f=True )
    pm.connectAttr( jntPrxs[i]+'.'+'rotate', jnts[i]+'.'+'rotate',f=True )