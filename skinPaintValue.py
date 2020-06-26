import pymel.core as pm
from mainEdit import qt
from PySide2 import QtGui, QtCore, QtWidgets

class SkinValueWindow(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super(SkinValueWindow, self).__init__(*args, **kwargs)
        mainLayout = QtWidgets.QFormLayout(self)

        value1 = QtWidgets.QRadioButton('0', self)
        value2 = QtWidgets.QRadioButton('0.001', self)
        value3 = QtWidgets.QRadioButton('0.01', self)
        value4 = QtWidgets.QRadioButton('0.5', self)
        value5 = QtWidgets.QRadioButton('1', self)
        value5.setChecked(True)

        acrossLayout = QtWidgets.QHBoxLayout(self)
        acrossLayout.addWidget(value1, True)
        acrossLayout.addWidget(value2, True)
        acrossLayout.addWidget(value3, True)
        acrossLayout.addWidget(value4, True)
        acrossLayout.addWidget(value5, True)
        mainLayout.addRow('ValueNum', acrossLayout)

        self.__across = QtWidgets.QButtonGroup(self)
        self.__across.addButton(value1, 0)
        self.__across.addButton(value2, 1)
        self.__across.addButton(value3, 2)
        self.__across.addButton(value4, 3)
        self.__across.addButton(value5, 4)

        num = self.__across.checkedId()

        button1 = QtWidgets.QPushButton('replace')
        button2 = QtWidgets.QPushButton('add')
        button3 = QtWidgets.QPushButton('sub')

        widthLayout = QtWidgets.QHBoxLayout(self)
        widthLayout.addWidget(button1, True)
        widthLayout.addWidget(button2, True)
        widthLayout.addWidget(button3, True)
        mainLayout.addRow(widthLayout)
        
        button1.clicked.connect(qt.Callback(rep(num)))
        button2.clicked.connect(qt.Callback(add(num)))
        button3.clicked.connect(qt.Callback(sub(num)))
        

def rep(across):
    print across
    if across == 0:
        value = 0
        pm.artAttrSkinPaintCtx('artAttrSkinContext', edit=True, val = value)
    elif across == 1:
        value = 0.001
        pm.artAttrSkinPaintCtx('artAttrSkinContext', edit=True, val = value)
    elif across == 2:
        value = 0.01
        pm.artAttrSkinPaintCtx('artAttrSkinContext', edit=True, val = value)
    elif across == 3:
        value = 0.5
        pm.artAttrSkinPaintCtx('artAttrSkinContext', edit=True, val = value)
    elif across == 4:
        value = 1
        pm.artAttrSkinPaintCtx('artAttrSkinContext', edit=True, val = value)
       
def add(across):
    getValue = pm.artAttrSkinPaintCtx('artAttrSkinContext', query = True, val = 0)
    if across == 1:
        value = getValue + 0.001
        pm.artAttrSkinPaintCtx('artAttrSkinContext', edit=True, val = value)
    elif across == 2:
        value = getValue + 0.01
        pm.artAttrSkinPaintCtx('artAttrSkinContext', edit=True, val = value)
    elif across == 3:
        value = getValue + 0.5
        pm.artAttrSkinPaintCtx('artAttrSkinContext', edit=True, val = value)
    elif across == 4:
        value = getValue + 1
        pm.artAttrSkinPaintCtx('artAttrSkinContext', edit=True, val = value)

def sub(across):
    getValue = pm.artAttrSkinPaintCtx('artAttrSkinContext', query = True, val = 0)
    if across == 1:
        value = getValue - 0.001
        pm.artAttrSkinPaintCtx('artAttrSkinContext', edit=True, val = value)
    elif across == 2:
        value = getValue - 0.01
        pm.artAttrSkinPaintCtx('artAttrSkinContext', edit=True, val = value)
    elif across == 3:
        value = getValue - 0.5
        pm.artAttrSkinPaintCtx('artAttrSkinContext', edit=True, val = value)
    elif across == 4:
        value = getValue - 1
        pm.artAttrSkinPaintCtx('artAttrSkinContext', edit=True, val = value)

def main():
    window = SkinValueWindow(qt.getMayaWindow())
    window.setWindowFlags(QtCore.Qt.Window)
    window.show()