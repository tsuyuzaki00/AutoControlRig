import pymel.core as pm

name = 'root'

select = pm.select( name +'_jnt')
jnts = pm.ls(sl=True, dag=True)

for i in range(len(jnts)):
    node = pm.createNode( 'transform',n=jnts[i])
    pm.parent( node , jnts[i] )
    pm.move( 0, 0, 0 ,ls=True)
    pm.rotate( 0, 0, 0 , os=True)