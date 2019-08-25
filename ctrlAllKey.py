import pymel.core as pm

def main():
    node = pm.selected()
    pm.listRelatives(node, parent=True)
    selects = pm.ls(sl=True, dag=True)

    for allKey in selects:
        if allKey.nodeType() == 'transform':
            if '_ctrl' in allKey.name():
                if '_grp' not in allKey.name():
                    pm.setKeyframe(allKey)
                    pm.select(cl = True)