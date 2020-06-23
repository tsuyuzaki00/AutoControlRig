import pymel.core as pm

with pm.window( title = 'WeightValueEdit', ret = True):
    with pm.columnLayout( adjustableColumn = True ):
        pm.text( label = 'powerValue' )
        value1 = pm.radioButton(label = '0')
        value2 = pm.radioButton(label = '0.001')
        value3 = pm.radioButton(label = '0.01')
        value4 = pm.radioButton(label = '0.5')
        value5 = pm.radioButton(label = '1')
        
        pm.button( label = 'replace', c = 'rep(value1.getSelect(),value2.getSelect(),value3.getSelect(),value4.getSelect(),value5.getSelect())')
        pm.button( label = 'add', c = 'add(value1.getSelect(),value2.getSelect(),value3.getSelect(),value4.getSelect(),value5.getSelect())')
        pm.button( label = 'sub', c = 'sub(value1.getSelect(),value2.getSelect(),value3.getSelect(),value4.getSelect(),value5.getSelect())')

def rep(count1,count2,count3,count4,count5):
    if count1 == True:
        value = 0
        pm.artAttrSkinPaintCtx('artAttrSkinContext', edit=True, val = value)
    elif count2 == True:
        value = 0.001
        pm.artAttrSkinPaintCtx('artAttrSkinContext', edit=True, val = value)
    elif count3 == True:
        value = 0.01
        pm.artAttrSkinPaintCtx('artAttrSkinContext', edit=True, val = value)
    elif count4 == True:
        value = 0.5
        pm.artAttrSkinPaintCtx('artAttrSkinContext', edit=True, val = value)
    elif count5 == True:
        value = 1
        pm.artAttrSkinPaintCtx('artAttrSkinContext', edit=True, val = value)
       
def add(count1,count2,count3,count4,count5):
    getValue = pm.artAttrSkinPaintCtx('artAttrSkinContext', query = True, val = 0)
    if count2 == True:
        value = getValue + 0.001
        pm.artAttrSkinPaintCtx('artAttrSkinContext', edit=True, val = value)
    elif count3 == True:
        value = getValue + 0.01
        pm.artAttrSkinPaintCtx('artAttrSkinContext', edit=True, val = value)
    elif count4 == True:
        value = getValue + 0.5
        pm.artAttrSkinPaintCtx('artAttrSkinContext', edit=True, val = value)
    elif count5 == True:
        value = getValue + 1
        pm.artAttrSkinPaintCtx('artAttrSkinContext', edit=True, val = value)

def sub(count1,count2,count3,count4,count5):
    getValue = pm.artAttrSkinPaintCtx('artAttrSkinContext', query = True, val = 0)
    if count2 == True:
        value = getValue - 0.001
        pm.artAttrSkinPaintCtx('artAttrSkinContext', edit=True, val = value)
    elif count3 == True:
        value = getValue - 0.01
        pm.artAttrSkinPaintCtx('artAttrSkinContext', edit=True, val = value)
    elif count4 == True:
        value = getValue - 0.5
        pm.artAttrSkinPaintCtx('artAttrSkinContext', edit=True, val = value)
    elif count5 == True:
        value = getValue - 1
        pm.artAttrSkinPaintCtx('artAttrSkinContext', edit=True, val = value)
