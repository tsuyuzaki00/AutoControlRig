from maya import cmds
def main():
    cmds.menu(l = 'My Tools', p ='MayaWindow', to = True)
    cmds.menuItem( subMenu=True, label='Colors' )
    cmds.menuItem( label='Blue' )
    cmds.menuItem( label='Green' )
    cmds.menuItem( label='Yellow' )
    cmds.setParent( '..', menu=True )
    cmds.menuItem( label='createCtrl',
    c = 'from scripts.AutoControlRig import ctrlOneConnect;ctrlOneConnect.main()'
    )
    cmds.menuItem( optionBox=True )
    cmds.menuItem( label='allCtrlKey',
    c = 'from scripts.AutoControlRig import grpCtrlAllKey;grpCtrlAllKey.main()'
    )
    cmds.menuItem( optionBox=True )