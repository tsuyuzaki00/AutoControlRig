import pymel.core as pm

def main():
    lowAngle = 30
    highAngle = 150
    
    sels = pm.selected()
    for sel in sels:
        selEdge = pm.polyEvaluate(e = True)
        edge = selEdge - 1
        pm.select(sel + '.e[0:' + str(edge) + ']', add = True)
        pm.polySelectConstraint(a = 1, m = 3, t = 0x8000, ab = (lowAngle, highAngle) )
        pm.polySelectConstraint(m = 0)