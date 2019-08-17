import pymel.core as pm

name = 'root'

select = pm.select( name +'_jnt')
jnts = pm.ls(sl=True, dag=True)

jntPrxs = [jntPrx.replace("_jnt",'_trs') for jntPrx in jnts]
for i in range(len(jnts)):
    node = pm.createNode( 'transform',n=jntPrxs[i])
    pm.parent( node , jnts[i] )
    pm.move( 0, 0, 0 ,ls=True)
    pm.rotate( 0, 0, 0 , os=True)