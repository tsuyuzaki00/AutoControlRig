import pymel.core as pm

def colorChage(center,left,right):
    sel = pm.selected()
    shapes = pm.listRelatives(sel[0:], type='nurbsCurve')
    
    for shape in shapes:
        pm.setAttr(shape+'.overrideEnabled',1)
        print center
            #�^��
        if shape.endswith('_CShape') or shape.endswith('_CTShape'):
            if center == 1:
                pm.setAttr(shape+'.overrideColor',17) #�x�[�X�J���[�A���F
            elif center == 2:
                pm.setAttr(shape+'.overrideColor',14) #�x�[�X�J���[�A�O���[��
            elif center == 3:
                pm.setAttr(shape+'.overrideColor',27) #�Z�J���h�J���[�A���������
            elif center == 4:
                pm.setAttr(shape+'.overrideColor',7 ) #�I�[�g�T�|�[�g�J���[�A�Z����
            
            #��
        if shape.endswith('_LShape') or shape.endswith('_LTShape'):
            if left == 1:
                pm.setAttr(shape+'.overrideColor',6 ) #�x�[�X�J���[�A�u���[
            elif left == 2:
                pm.setAttr(shape+'.overrideColor',18) #�Z�J���h�J���[�A�V�A��
            elif left == 3:
                pm.setAttr(shape+'.overrideColor',30) #�I�[�g�T�|�[�g�J���[�A�� 
            
            #�E
        if shape.endswith('_RShape') or shape.endswith('_RTShape'):
            if right == 1:
                pm.setAttr(shape+'.overrideColor',13) #�x�[�X�J���[�A���b�h
            elif right == 2:
                pm.setAttr(shape+'.overrideColor',20) #�Z�J���h�J���[�A�s���N
            elif right == 3:
                pm.setAttr(shape+'.overrideColor',31) #�I�[�g�T�|�[�g�J���[�A�}�[���_

with pm.window( title = 'colorChenge', ret = True):
    with pm.columnLayout( adjustableColumn = True ):
        pm.text( label = 'select Color' )
        centerRdoGrp = pm.radioButtonGrp( numberOfRadioButtons = 4,
                                            label = 'Center',
                                            labelArray4 = [ 'Base Yellow','Base Green','Second Green','AutoSupport Green'])
        pm.separator()
        leftRdoGrp = pm.radioButtonGrp( numberOfRadioButtons = 3,
                                            label = 'Left',
                                            labelArray3 = [ 'Base Blue','Second Cyan','AutoSupport Purple'])
        pm.separator()
        rightRdoGrp = pm.radioButtonGrp( numberOfRadioButtons = 3,
                                            label = 'Right',
                                            labelArray3 = [ 'Base Red','Second Pink','AutoSupport Magenta'])
        pm.separator()
        pm.button( label = 'colorChange', c = "colorChage(centerRdoGrp.getSelect(),leftRdoGrp.getSelect(),rightRdoGrp.getSelect())")

