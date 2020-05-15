import pymel.core as pm

def shapeMove():
    sels = pm.ls(sl = True)
    for j in range(len(sels)):
        objName = sels[j].rsplit("[",1)
        numText = objName[1].split(':')[-1].split(']')[0]
        number = int(numText) + 1
        for i in range(number):
            posName = objName[0]+"["+ str(i) +"]"
            oriPoss = pm.pointPosition( posName , w = True )
            renamePos = posName.replace('_L', '_R')
        
            pm.select(renamePos)
            pm.move(oriPoss[0]*-1,oriPoss[1],oriPoss[2])
            
shapeMove()