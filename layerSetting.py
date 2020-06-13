import pymel.core as pm

def main():
    sceneName = pm.sceneName().basename()
    part = sceneName.split("_")
    if part[0].endswith('.ma') or part[0].endswith('.mb'):
        name = part[0][:-3]
    elif part[0] == '':
        name = 'scene'
    else:
        name = part[0]

    pm.createNode('transform', n = 'grp_geo_' + name)
    pm.createNode('transform', n = 'grp_jnt_' + name)
    pm.createNode('transform', n = 'grp_ctrl_' + name)

    pm.select('grp_geo_' + name)
    pm.createDisplayLayer(n = 'geo_' + name + '_layer', num = 1 , nr = True)
    pm.select('grp_jnt_' + name)
    pm.createDisplayLayer(n = 'jnt_' + name + '_layer', num = 2 , nr = True)
    pm.select('grp_ctrl_' + name)
    pm.createDisplayLayer(n = 'ctrl_' + name + '_layer', num = 3 , nr = True)