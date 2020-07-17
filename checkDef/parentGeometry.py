import maya.cmds as cmds

def OKList(sel, check):
    print 'OK' + ' : ' + check + ' : ' + sel
def NGList(sel, check):
    print 'NG' + ' : ' + check + ' : ' + sel

def parentGeometryCheck(sels):
    check = 'ParentGeometry'
    for sel in sels:
        parents = cmds.listRelatives(sel, p = True, fullPath = True)
        if parents == None:
            OKList(sel, check)
        else :
            for i in parents:
                hierarchys = i.split("|")
                for j in hierarchys:
                    print j
                    test = cmds.listRelatives('u'+ j, s = True)
                    print test
                    #if cmds.nodeType(test) == 'mesh':
                        #NGList(sel, check)


def main():
    sels = cmds.ls(sl = True)
    parentGeometryCheck(sels)

main()