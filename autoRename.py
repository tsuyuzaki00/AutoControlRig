import pymel.core as pm

def scene(sel):
    sceneName = pm.sceneName().basename()
    part = sceneName.split("_")
    if part[0].endswith('.ma') or part[0].endswith('.mb'):
        scene = part[0][:-3]
    elif part[0] == '':
        scene = 'scene'
    else:
        scene = part[0]
    return scene

def obj(sel):
    part = sel.split("_")
    
    if part[0] == pos(sel):
        if part[1] == scene(sel):
            obj = part[2]
            return obj
        else :
            obj = part[1]
            return obj
    elif part[0] == node(sel):
        obj = part[1]
        return obj
    elif part[0] == scene(sel):
        obj = part[1]
        return obj
    else :
        obj = part[0]
        return obj

def node(sel):
    if sel.nodeType() == 'transform':
        if pm.listRelatives(sel, s = True) == []:
            node = 'null'
            return node
        elif pm.listRelatives(sel, c = True, type = 'mesh'):
            node = 'geo'
            return node
        elif pm.listRelatives(sel, c = True, type = 'nurbsCurve'):
            node = 'ctrl'
            return node
        elif pm.listRelatives(sel, c = True, type = 'nurbsSurface'):
            node = 'surf'
            return node
        elif pm.listRelatives(sel, c = True, type = 'camera'):
            node = 'cam'
            return node
        elif pm.listRelatives(sel, c = True, type = 'locator'):
            node = 'loc'
            return node
        elif pm.listRelatives(sel, c = True, type = 'imagePlane'):
            node = 'image'
            return node
        elif pm.listRelatives(sel, c = True, type = 'spotLight'):
            node = 'stl'
            return node
        elif pm.listRelatives(sel, c = True, type = 'ambientLight'):
            node = 'atl'
            return node
        elif pm.listRelatives(sel, c = True, type = 'pointLight'):
            node = 'ptl'
            return node
        elif pm.listRelatives(sel, c = True, type = 'directionalLight'):
            node = 'dtl'
            return node
        #transNode
        'null'
        'offset'
        'move' 
        'space'
        'trs'
        'grp'
    elif sel.nodeType() == 'joint':
        node = 'jnt'
        return node
    elif sel.nodeType() == 'parentConstraint':
        node = 'prc'
        return node
    elif sel.nodeType() == 'pointConstraint':
        node = 'ptc'
        return node
    elif sel.nodeType() == 'orientConstraint':
        node = 'otc'
        return node
    elif sel.nodeType() == 'scaleConstraint':
        node = 'slc'
        return node
    elif sel.nodeType() == 'aimConstraint':
        node = 'amc'
        return node
    elif sel.nodeType() == 'poleVectorConstraint':
        node = 'pvc'
        return node
    elif sel.nodeType() == 'IKhandle':
        node = 'ikh'
        return node
    elif sel.nodeType() == 'effector':
        node = 'eft'
        return node
    elif sel.nodeType() == 'condition':
        node = 'cnd'
        return node
    elif sel.nodeType() == 'multiplyDivide':
        node = 'mdp'
        return node
    elif sel.nodeType() == 'plusMinusAverage':
        node = 'pma'
        return node
    elif sel.nodeType() == 'reverse':
        node = 'rvs'
        return node
    elif sel.nodeType() == 'clamp':
        node = 'clp'
        return node
    elif sel.nodeType() == 'blendColors':
        node = 'bdc'
        return node
    elif sel.nodeType() == 'multMatrix':
        node = 'mmx'
        return node
    elif sel.nodeType() == 'decomposeMatrix':
        node = 'dmx'
        return node
    elif sel.nodeType() == 'composeMatrix':
        node = 'cmx'
        return node
    elif sel.nodeType() == 'distanceBetween':
        node = 'dist'
        return node
    elif sel.nodeType() == 'lambert':
        node = 'lbt'
        #test = pm.listConnections(sel + '.color', d = True)
        #print test
        #pm.rename(color,node + obj(sel) + scene(sel))
        return node

    #elif sel.nodeType() == 'file':
        node = 'color' #baseColor
        node = 'nmp' #normalMap

def pos(sel):
    pos = 'C'
    if 'joint' == node(sel):
        if pm.listRelatives(sel, c = True) == []:
            pos = 'CT'

    elif sel.endswith('_C') or sel.startswith('C_'):
        pos = 'C'
    elif sel.endswith('_CT') or sel.startswith('CT_'):
        pos = 'CT'
    elif sel.endswith('_L') or sel.startswith('L_'):
        pos = 'L'
    elif sel.endswith('_LT') or sel.startswith('LT_'):
        pos = 'LT'
    elif sel.endswith('_R') or sel.startswith('R_'):
        pos = 'R'
    elif sel.endswith('_RT') or sel.startswith('RT_'):
        pos = 'RT'

    return pos

def num(sel):
    if 'geo' == node(sel):
        num = '1'.zfill(3)
    elif 'cam' == node(sel):
        num = '1'.zfill(3)
    elif 'image' == node(sel):
        num = '1'.zfill(3)
    elif 'stl' == node(sel):
        num = '1'.zfill(3)
    elif 'atl' == node(sel):
        num = '1'.zfill(3)
    elif 'ptl' == node(sel):
        num = '1'.zfill(3)
    elif 'dtl' == node(sel):
        num = '1'.zfill(3)
    elif 'jnt' == node(sel):
        num = '1'.zfill(2)
    elif 'ctrl' == node(sel):
        num = '1'.zfill(2)
    return num

def main():
    sels = pm.selected()
    for sel in sels:
        lists = [pos(sel),obj(sel),node(sel),scene(sel),num(sel)]
        names = [l for l in lists if l != '']
        autoRename = '_'.join(names)
        pm.rename(sel, autoRename)

main()