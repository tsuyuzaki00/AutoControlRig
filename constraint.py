import pymel.core as pm

parts = 'upArm'
jntType = '_jntFK'
LR = '_R'

pm.select(upArm + jntType + LR)
Prx = pm.ls(sl=True, dag=True)

jntPrxs =[i for i in Prx if i.endswith(LR)]
names = [jntPrx.replace('_jntFK' + LR, '') for jntPrx in jntPrxs]

for name in names:
    pm.pointConstraint( name + '_ctrlFK' + LR, name + jntType + LR, n = name + '_pointConstraint')
    pm.orientConstraint( name + '_ctrlFK' + LR, name + jntType + LR, n = name + '_orientConstraint')