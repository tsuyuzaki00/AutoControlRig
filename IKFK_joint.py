import pymel.core as pm

IKjnt = pm.selected()[0]
FKjnt = pm.selected()[1]
blendc = pm.selected()[2]
jnt = pm.selected()[3]

trsAttr = 'translate'
blendc_inAttr1 = 'color1'
blendc_inAttr2 = 'color2'
blendc_outAttr = 'output'

pm.connectAttr( IKjnt.name()+'.'+trsAttr, blendc.name()+'.'+blendc_inAttr1,f=True )
pm.connectAttr( FKjnt.name()+'.'+trsAttr, blendc.name()+'.'+blendc_inAttr2,f=True )
pm.connectAttr( blendc.name()+'.'+blendc_outAttr, jnt.name()+'.'+trsAttr,f=True )
