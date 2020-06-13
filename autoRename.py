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
    if part[0] == node(sel):
        obj = part[1]
        return obj
    else :
        obj = part[0]
        return obj

def node(sel):
    if sel.nodeType() == 'transform':
        if pm.listRelatives(sel, c = True, type = 'mesh'):
            node = 'geo'
            return node
        elif pm.listRelatives(sel, c = True, type = 'nurbsCurve'):
            node = 'ctrl'
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
        node = 'jnt' #joint
        return node
    elif sel.nodeType() == 'parentConstraint':
        node = 'prc' #ParentConstraint
        return node
    elif sel.nodeType() == 'pointConstraint':
        node = 'ptc' #PointConstraint
        return node
    elif sel.nodeType() == 'orientConstraint':
        node = 'otc' #OrientConstraint
        return node
    elif sel.nodeType() == 'scaleConstraint':
        node = 'slc' #ScaleConstraint
        return node
    elif sel.nodeType() == 'aimConstraint':
        node = 'amc' #AimConstraint
        return node
    elif sel.nodeType() == 'poleVectorConstraint':
        node = 'pvc' #PoleVectorConstraint
        return node
    elif sel.nodeType() == 'IKhandle':
        node = 'ikh' #IKhandle
        return node
    elif sel.nodeType() == 'effector':
        node = 'eft' #effector
        return node
    #elif sel.nodeType() == 'parentConstraint':
        node = 'mat' #material
        node = 'color' #baseColor
        node = 'nmp' #normalMap
        node = 'cnd' #condition
        node = 'mdp' #multiplyDivide Power
        node = 'pma' #PlusMinusAverage
        node = 'rvs' #Reverse
        node = 'clp' #Clamp
        node = 'bdc' #Blend Colors
        node = 'mmx' #multMatrix
        node = 'dmx' #decomposeMatrix
        node = 'cmx' #composeMatrix

def other(sel):
    other = 'C'
    if 'joint' == node(sel):
        if pm.listRelatives(sel, c = True) == []:
            other = 'CT'
    'L'
    'LT'
    'R'
    'RT'

    if 'geo' == node(sel):
        other = '1'.zfill(3)
    return other

def main():
    sels = pm.selected()
    for sel in sels:
        lists = [node(sel),obj(sel),scene(sel),other(sel)]
        names = [l for l in lists if l != '']
        autoRename = '_'.join(names)
        pm.rename(sel, autoRename)