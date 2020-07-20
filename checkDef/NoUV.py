import maya.cmds as cmds

def OKList(sel, check):
    print 'OK' + ' : ' + check + ' : ' + sel
def NGList(sel, check):
    print 'NG' + ' : ' + check + ' : ' + sel

def NoUVCheck(sels):
    check = 'No UV'
    for sel in sels:
        cmds.polyListComponentConversion(sel, tuv = True)

        try:
            OKList(sel, check)
        except:
            cmds.select(sel)
            NGList(sel, check)
            
def main():
    sels = cmds.ls(sl = True)
    NoUVCheck(sels)

main()