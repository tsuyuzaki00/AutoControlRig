import pymel.core as pm

def shapeMove():
    sels = pm.selected()
    for sel in sels:
        CVs = pm.filterExpand(sel,sm = 28)
        for CV in CVs:
            CVPos = pm.pointPosition( CV , w = True )
            renameCV = CV.replace('_L', '_R')
            pm.select(renameCV)
            pm.move(CVPos[0]*-1,CVPos[1],CVPos[2])
            
shapeMove()