import pymel.core as pm

name = 'root'

pm.select(name + '_jnt')
jnts = pm.ls(sl=True, dag=True)

pm.select(name + '_jntPrx')
jntPrxs = pm.ls(sl=True, dag=True)
jntPrx =[i for i in jntPrxs if '_jntPrx' in i.name()]

for i in range(len(jnts)):
    pm.connectAttr( jntPrx[i]+'.'+'translate', jnts[i]+'.'+'translate',f=True )
    pm.connectAttr( jntPrx[i]+'.'+'rotate', jnts[i]+'.'+'rotate',f=True )