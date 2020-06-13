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
    obj = part[0]
    return obj

def node(sel):
    sels = pm.selected()
    for sel in sels:
        if sel.nodeType() == 'transform':
            if pm.listRelatives(sel, c = True, type = 'mesh'):
                node = 'geo'
            elif pm.listRelatives(sel, c = True, type = 'nurbsCurve'):
                node = 'ctrl'
            elif pm.listRelatives(sel, c = True, type = 'camera'):
                node = 'cam'
            elif pm.listRelatives(sel, c = True, type = 'locator'):
                node = 'loc'
            elif pm.listRelatives(sel, c = True, type = 'imagePlane'):
                node = 'image'
            elif pm.listRelatives(sel, c = True, type = 'spotLight'):
                node = 'stl'
            elif pm.listRelatives(sel, c = True, type = 'ambientLight'):
                node = 'atl'
            elif pm.listRelatives(sel, c = True, type = 'pointLight'):
                node = 'ptl'
            elif pm.listRelatives(sel, c = True, type = 'directionalLight'):
                node = 'dtl'
            #transNode
            'null'
            'offset'
            'move' 
            'space'
            'trs'
            'grp'
        elif sel.nodeType() == 'joint':
            node = 'jnt' #joint
        elif sel.nodeType() == 'parentConstraint':
            node = 'prc' #ParentConstraint
        elif sel.nodeType() == 'pointConstraint':
            node = 'ptc' #PointConstraint
        elif sel.nodeType() == 'orientConstraint':
            node = 'otc' #OrientConstraint
        elif sel.nodeType() == 'scaleConstraint':
            node = 'slc' #ScaleConstraint
        elif sel.nodeType() == 'aimConstraint':
            node = 'amc' #AimConstraint
        elif sel.nodeType() == 'poleVectorConstraint':
            node = 'pvc' #PoleVectorConstraint
        elif sel.nodeType() == 'IKhandle':
            node = 'ikh' #IKhandle
        elif sel.nodeType() == 'effector':
            node = 'eft' #effector
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
    return node

def other(sel):
    other = 'C'
    if node(node) == 'joint':
        if pm.listRelatives(sel, c = True) == []:
            other = 'CT'
    'L'
    'LT'
    'R'
    'RT'

    if node(node) == 'geo':
        other = '1'.zfill(3)
    return other

def main():
    sels = pm.selected()
    for sel in sels:
        lists = [node(sel),obj(sel),scene(sel),other(sel)]
        names = [l for l in lists if l != '']
        autoRename = '_'.join(names)
        pm.rename(sel, autoRename)

main()