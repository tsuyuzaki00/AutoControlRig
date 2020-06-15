import pymel.core as pm

def colorChage(center,left,right):
    sel = pm.selected()
    shapes = pm.listRelatives(sel[0:], type='nurbsCurve')
    
    for shape in shapes:
        pm.setAttr(shape+'.overrideEnabled',1)
        print center
            #真ん中
        if shape.endswith('_CShape') or shape.endswith('_CTShape'):
            if center == 1:
                pm.setAttr(shape+'.overrideColor',17) #ベースカラー、黄色
            elif center == 2:
                pm.setAttr(shape+'.overrideColor',14) #ベースカラー、グリーン
            elif center == 3:
                pm.setAttr(shape+'.overrideColor',27) #セカンドカラー、あっさり緑
            elif center == 4:
                pm.setAttr(shape+'.overrideColor',7 ) #オートサポートカラー、濃い緑
            
            #左
        if shape.endswith('_LShape') or shape.endswith('_LTShape'):
            if left == 1:
                pm.setAttr(shape+'.overrideColor',6 ) #ベースカラー、ブルー
            elif left == 2:
                pm.setAttr(shape+'.overrideColor',18) #セカンドカラー、シアン
            elif left == 3:
                pm.setAttr(shape+'.overrideColor',30) #オートサポートカラー、紫 
            
            #右
        if shape.endswith('_RShape') or shape.endswith('_RTShape'):
            if right == 1:
                pm.setAttr(shape+'.overrideColor',13) #ベースカラー、レッド
            elif right == 2:
                pm.setAttr(shape+'.overrideColor',20) #セカンドカラー、ピンク
            elif right == 3:
                pm.setAttr(shape+'.overrideColor',31) #オートサポートカラー、マゼンダ

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

