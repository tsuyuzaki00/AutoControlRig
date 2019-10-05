import pymel.core as pm

def main():
    pm.selected()
    jnts = pm.ls(sl=True, dag=True)
    jntPrxs = [jntPrx.replace("_jnt",'_jntPrx') for jntPrx in jnts]

    for i in range(len(jnts)):
        pm.connectAttr( jntPrxs[i]+'.'+'translate', jnts[i]+'.'+'translate',f=True )
        pm.connectAttr( jntPrxs[i]+'.'+'rotate', jnts[i]+'.'+'rotate',f=True )
        pm.connectAttr( jntPrxs[i]+'.'+'scale', jnts[i]+'.'+'scale',f=True )