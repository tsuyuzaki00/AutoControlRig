import pymel.core as pm

def main():
    sel = pm.selected()
    parentSel = pm.listRelatives(sel, parent=True)
    if sel != []:
        spaceName = sel[0].replace("_jnt",'_space')
        ctrlName = sel[0].replace("_jnt",'_ctrl')
        trsName = sel[0].replace("_jnt",'_trs')
        
        spaceNode = pm.createNode( 'transform', n=spaceName)
        trsNode = pm.createNode( 'transform', n=trsName)
        
        ctrlNode = pm.curve(p=[(0, 1.11, 0), (0, 0.78, -0.78), (0, 0, -1.11), (0, -0.78, -0.78), (0, -1.11, 0), (0, -0.78, 0.78), (0, 0, 1.11), (0, 0.78, 0.78), (0, 1.11, 0)] )
        pm.rename(ctrlNode ,ctrlName)
        
        pm.parent(trsNode,ctrlNode)
        pm.setAttr(trsNode+'.translate', 0, 0, 0, type="double3")
        pm.setAttr(trsNode+'.rotate', 0, 0, 0, type="double3")
        
        pm.parent(ctrlNode,spaceNode)
        pm.setAttr(ctrlNode+'.translate', 0, 0, 0, type="double3")
        pm.setAttr(ctrlNode+'.rotate', 0, 0, 0, type="double3")
        
        pm.parent(spaceName,sel[0])
        pm.setAttr(spaceNode+'.translate', 0, 0, 0, type="double3")
        pm.setAttr(spaceNode+'.rotate', 0, 0, 0, type="double3")
        
        name_ctrl_grp = (sel[0].split('_'))
        all = pm.ls()
        
        if name_ctrl_grp[0]+'_ctrl_grp' not in all:
            pm.createNode( 'transform', n=name_ctrl_grp[0]+'_ctrl_grp')

        if parentSel == []:
            pm.parent(spaceNode, name_ctrl_grp[0]+'_ctrl_grp')
            pm.pointConstraint(trsNode,sel[0])
            pm.orientConstraint(trsNode,sel[0])
        else :
            offsetName = sel[0].replace("_jnt",'_offset')
            offsetNode = pm.createNode( 'transform', n=offsetName)
            pm.parent(offsetNode,parentSel[0])
            pm.setAttr(offsetNode+'.translate', 0, 0, 0, type="double3")
            pm.setAttr(offsetNode+'.rotate', 0, 0, 0, type="double3")
            
            pm.parent(offsetNode, name_ctrl_grp[0]+'_ctrl_grp')
            pm.parent(spaceNode,offsetNode)
            
            pm.pointConstraint(parentSel[0],offsetNode)
            pm.orientConstraint(parentSel[0],offsetNode)
            pm.pointConstraint(trsNode,sel[0])
            pm.orientConstraint(trsNode,sel[0])