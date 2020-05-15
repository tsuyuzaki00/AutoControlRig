import pymel.core as pm

sel = pm.selected()
shapes = pm.listRelatives(sel[0:], type='nurbsCurve')

for shape in shapes:
    pm.setAttr(shape+'.overrideEnabled',1)
    if shape.endswith('_CShape') == True:
        #真ん中
        pm.setAttr(shape+'.overrideColor',17) #ベースカラー、黄色
        pm.setAttr(shape+'.overrideColor',14) #ベースカラー、グリーン
        pm.setAttr(shape+'.overrideColor',27) #セカンドカラー、あっさり緑
        pm.setAttr(shape+'.overrideColor',7 ) #オートサポートカラー、濃い緑
    elif shape.endswith('_LShape') == True:
        #左
        pm.setAttr(shape+'.overrideColor',6 ) #ベースカラー、ブルー
        pm.setAttr(shape+'.overrideColor',18) #セカンドカラー、シアン
        pm.setAttr(shape+'.overrideColor',30) #オートサポートカラー、紫 
    elif shape.endswith('_RShape') == True:
        #右
        pm.setAttr(shape+'.overrideColor',13) #ベースカラー、レッド
        pm.setAttr(shape+'.overrideColor',20) #セカンドカラー、ピンク
        pm.setAttr(shape+'.overrideColor',31) #オートサポートカラー、マゼンダ
    