import pymel.core as pm

def main():
    armleg = 'hamakaze_legFKIK'

    jnt = pm.selected()[0]
    jntIK = jnt.replace("_jnt",'IK_jnt')
    jntFK = jnt.replace("_jnt",'FK_jnt')

    part = jnt.split("_")
    name = part[0] + '_' + part[1] + '_orientConstraint_' + part[-1]

    LR = part[-1]
    reverse = armleg + '_reverse' + LR
    ctrl = armleg + '_ctrl' + LR

    pm.orientConstraint(jntIK, jnt, n = name )
    pm.orientConstraint(jntFK, jnt,)
    pm.connectAttr(ctrl+".FKIK", name + "." + jntIK + "W0")
    pm.connectAttr(reverse+".outputX", name + "." + jntFK + "W1")