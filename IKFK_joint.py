import pymel.core as pm

jnt = pm.ls(sl=True, dag=True)
pm.duplicate(n='FK',rc=True)
FKjnt = pm.ls(sl=True, dag=True)
pm.duplicate(n='IK',rc=True)
IKjnt = pm.ls(sl=True, dag=True)

trsAttr = 'translate'
rotateAttr = 'rotate'
blendc_inAttr1 = 'color1'
blendc_inAttr2 = 'color2'
blendc_outAttr = 'output'

for i in range(len(jnt)):
    blendc = pm.createNode('blendColors', n='blendColor_{}'.format(i))
    pm.connectAttr( IKjnt[i]+'.'+trsAttr, blendc+'.'+blendc_inAttr1)
    pm.connectAttr( FKjnt[i]+'.'+trsAttr, blendc+'.'+blendc_inAttr2)
    pm.connectAttr( blendc+'.'+blendc_outAttr, jnt[i]+'.'+trsAttr )
    
    #pm.connectAttr( IKjnt[i]+'.'+rotateAttr, blendc+'.'+blendc_inAttr1)
    #pm.connectAttr( FKjnt[i]+'.'+rotateAttr, blendc+'.'+blendc_inAttr2)
    #pm.connectAttr( blendc+'.'+blendc_outAttr, jnt[i]+'.'+rotateAttr)