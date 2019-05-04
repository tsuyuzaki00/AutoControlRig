import pymel.core as pm

name = 'root'

select = pm.select( name +'_jnt')
jnts = pm.ls(sl=True, dag=True)

for i in range(len(jnts)):
    node = pm.createNode( 'transform',n='_trs')
    pm.parent( node , jnts[i] )