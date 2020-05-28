import pymel.core as pm

sceneName = pm.sceneName().basename()
part = sceneName.split("_")
if part[0].endswith('.ma') or part[0].endswith('.mb'):
    name = part[0][:-3]
else:
    name = part[0]


pm.createNode('transform', n = 'geometry')
pm.createNode('transform', n = 'joints')
pm.createNode('transform', n = 'ctrls')

pm.select('geometry')
pm.createDisplayLayer(n = 'GEO_' + name + '_layer', num = 1 , nr = True)
pm.select('joints')
pm.createDisplayLayer(n = 'JNT_' + name + '_layer', num = 2 , nr = True)
pm.select('ctrls')
pm.createDisplayLayer(n = 'CTL_' + name + '_layer', num = 3 , nr = True)