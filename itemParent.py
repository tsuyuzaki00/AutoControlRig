import pymel.core as pm

def itemParent():
    exParent = pm.selected()[0]
    itemParents = pm.selected()[1:]
    for itemParent in itemParents:
        part = itemParent.split("_")
        patternName = '_' + part[1] + '_' + part[2] + '_' + part[3] 
        ctrlName = 'ctrl' + patternName
        parentName = 'prc' + patternName
        
        cnd = pm.createNode('condition', n='cnd' + patternName)
        pm.setAttr(cnd + '.colorIfTrueR', 1)
        pm.setAttr(cnd + '.colorIfFalseR', 0)
        
        pm.parentConstraint(exParent, itemParent, n = parentName, mo = True, w = 1)
        
        pm.select(ctrlName)
        pm.addAttr(ln = 'parent', nn = 'Parent', at = 'enum', en = 'Local:World')
        pm.setAttr(ctrlName + '.parent', k = True)
        
        pm.connectAttr(ctrlName + ".parent", cnd + ".firstTerm")
        pm.connectAttr(cnd+".outColorR", parentName + "." + exParent + "W0")