import pymel.core as pm

def main():
    sceneName = pm.sceneName().basename()
    part = sceneName.split("_")
    
    if pm.objExists(part[0]) or pm.objExists('scene'):
        pm.error('Group name already exists')
    
    if part[0].endswith('.ma') or part[0].endswith('.mb'):
        name = part[0][:-3]
    elif part[0] == '':
        name = 'scene'
    else:
        name = part[0]
        
    allGrp = pm.createNode('transform', n = name)
    guideGrp = pm.createNode('transform', n = '_'.join( ['grp','guide',name] ))
    geoGrp = pm.createNode('transform', n = '_'.join( ['grp','geo',name] ))
    pm.setAttr('grp_geo_' + name + '.inheritsTransform', 0)
    camGrp = pm.createNode('transform', n = '_'.join( ['grp','cam',name] ))
    litGrp = pm.createNode('transform', n = '_'.join( ['grp','lit',name] ))
    jntGrp = pm.createNode('transform', n = '_'.join( ['grp','jnt',name] ))
    ctrlGrp = pm.createNode('transform', n = '_'.join( ['grp','ctrl',name] ))
    
    pm.parent(camGrp, allGrp)
    pm.parent(litGrp, allGrp)
    pm.parent(ctrlGrp, allGrp)
    pm.parent(jntGrp, allGrp)
    pm.parent(geoGrp, allGrp)
    pm.parent(guideGrp, allGrp)
        
    allSel = pm.select(all = True)
    getMesh = pm.listRelatives(type='mesh')
    getGeo = pm.listRelatives(getMesh, p = True)
    pm.select(cl = True)
    for i in getGeo:
        pm.parent(i, geoGrp)
    
    pm.select(all = True)
    layers = pm.selected(type='displayLayer')
    pm.select(cl = True)
    if layers == []:
        guideLayer = pm.createDisplayLayer(n = '_'.join( ['guide',name,'layer'] ), num = 1)
        geoLayer = pm.createDisplayLayer(n = '_'.join( ['geo',name,'layer'] ), num = 2)
        jntLayer = pm.createDisplayLayer(n = '_'.join( ['jnt',name,'layer'] ), num = 3)
        ctrlLayer = pm.createDisplayLayer(n = '_'.join( ['ctrl',name,'layer'] ), num = 6)
        camLayer = pm.createDisplayLayer(n = '_'.join( ['cam',name,'layer'] ), num = 4)
        litLayer = pm.createDisplayLayer(n = '_'.join( ['lit',name,'layer'] ), num = 5)
        pm.editDisplayLayerMembers(guideLayer, guideGrp)
        pm.editDisplayLayerMembers(geoLayer, geoGrp)
        pm.editDisplayLayerMembers(jntLayer, jntGrp)
        pm.editDisplayLayerMembers(ctrlLayer, ctrlGrp)
        pm.editDisplayLayerMembers(litLayer, litGrp)
        pm.editDisplayLayerMembers(camLayer, camGrp)
    
    for i in layers:
        if i == 'geo_' + name + '_layer':
            geoLayer = 'geo_' + name + '_layer'
            pm.editDisplayLayerMembers(geoLayer, geoGrp)
        elif i == 'guide_' + name + '_layer':
            guideLayer = 'guide_' + name + '_layer'
            pm.editDisplayLayerMembers(guideLayer, guideGrp)
        elif i == 'jnt_' + name + '_layer':
            jntLayer = 'jnt_' + name + '_layer'
            pm.editDisplayLayerMembers(jntLayer, jntGrp)
        elif i == 'ctrl_' + name + '_layer':    
            ctrlLayer = 'ctrl_' + name + '_layer'
            pm.editDisplayLayerMembers(ctrlLayer, ctrlGrp)
        elif i == 'lit_' + name + '_layer':    
            litLayer = 'lit_' + name + '_layer'
            pm.editDisplayLayerMembers(litLayer, litGrp)
        elif i == 'cam_' + name + '_layer':    
            camLayer = 'cam_' + name + '_layer'
            pm.editDisplayLayerMembers(camLayer, camGrp)
            