import import pymel.core as pm

sels = pm.selected()
pm.polySelectConstraint(a = 1, m = 3, t = 0x8000, ab = (30, 150) )
pm.polySelectConstraint(m = 0)