import pymel.core as pm

vtxSels = pm.selected()
pm.skinPercent('skinCluster11', vtxSels, transformValue = [('tail_C0_5_jnt', 0.3550), ('tail_C0_6_jnt', 0.6550)])