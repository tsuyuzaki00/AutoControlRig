import maya.cmds as cmds

def OKList(sel, check):
    print 'OK' + ' : ' + check + ' : ' + sel
def NGList(sel, check):
    print 'NG' + ' : ' + check + ' : ' + sel

def legalUVCheck(sels):
    check = 'Legal UV'
    for sel in sels:
        test = None
        if test == None:
            OKList(sel, check)
        else :
            cmds.select(test)
            NGList(sel, check)
            
def main():
    sels = cmds.ls(sl = True)
    legalUVCheck(sels)

main()