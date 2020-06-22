import pymel.core as pm

def main():
    addNullNode('')


def addNullNode(node):
    node = ''
    sel = pm.selected()[0]
    nullName = pm.listRelatives(sel, p = True)
    part = sel.split("_")
    offName = 'off'+ node + '_' + part[1] + '_' + part[2] + '_' + part[3]
    movName = 'mov'+ node + '_' + part[1] + '_' + part[2] + '_' + part[3]
    
    off = pm.duplicate(nullName , po = True, n = offName)
    mov = pm.duplicate(sel , po = True, n = movName)
    
    pm.parent(mov[0], off[0])
    pm.parent(nullName,mov[0])
    return node