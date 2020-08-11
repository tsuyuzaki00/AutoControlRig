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
        value4 = QtWidgets.QRadioButton('0.1', self)
        value5 = QtWidgets.QRadioButton('0.5', self)
        value6 = QtWidgets.QRadioButton('1', self)
        value6.setChecked(True)

        acrossLayout = QtWidgets.QHBoxLayout(self)
        acrossLayout.addWidget(value1, True)
        acrossLayout.addWidget(value2, True)
        acrossLayout.addWidget(value3, True)
        acrossLayout.addWidget(value4, True)
        acrossLayout.addWidget(value5, True)
        acrossLayout.addWidget(value6, True)
        mainLayout.addRow('ValueNum', acrossLayout)

        self.__across = QtWidgets.QButtonGroup(self)
        self.__across.addButton(value1, 0)
        self.__across.addButton(value2, 1)
        self.__across.addButton(value3, 2)
        self.__across.addButton(value4, 3)
        self.__across.addButton(value5, 4)
        self.__across.addButton(value6, 5)

        self.num = self.__across.checkedId()

        button1 = QtWidgets.QPushButton('replace')
        button2 = QtWidgets.QPushButton('add')
        button3 = QtWidgets.QPushButton('sub')
        button4 = QtWidgets.QPushButton('flood')

        widthLayout = QtWidgets.QHBoxLayout(self)
        widthLayout.addWidget(button1, True)
        widthLayout.addWidget(button2, True)
        widthLayout.addWidget(button3, True)
        widthLayout.addWidget(button4, True)
        mainLayout.addRow(widthLayout)
        
        button1.clicked.connect(self._setRep)
        button2.clicked.connect(self._setAdd)
        button3.clicked.connect(self._setSub)
        button4.clicked.connect(self._setflood)

    def _setRep(self):
        self.num = self.__across.checkedId()
        rep(self.num)

    def _setAdd(self):
        self.num = self.__across.checkedId()
        add(self.num)

    def _setSub(self):
        self.num = self.__across.checkedId()
        sub(self.num)

    def _setflood(self):
        self.flood = True
        flood(self.flood)
        
def rep(across):
        if across == 0:
            value = 0
            paintValues(value)
        elif across == 1:
            value = 0.001
            paintValues(value)
        elif across == 2:
            value = 0.01
            paintValues(value)
        elif across == 3:
            value = 0.1
            paintValues(value)
        elif across == 4:
            value = 0.5
            paintValues(value)
        elif across == 5:
            value = 1
            paintValues(value)
       
def add(across):
    getValue = pm.artAttrCtx('artAttrSkinContext', query = True, val = 0)
    if across == 1:
        value = getValue + 0.001
        paintValues(value)
    elif across == 2:
        value = getValue + 0.01
        paintValues(value)
    elif across == 3:
        value = getValue + 0.1
        paintValues(value)
    elif across == 4:
        value = getValue + 0.5
        paintValues(value)
    elif across == 5:
        value = getValue + 1
        paintValues(value)

def sub(across):
    getValue = pm.artAttrCtx('artAttrSkinContext', query = True, val = 0)
    if across == 1:
        value = getValue - 0.001
        paintValues(value)
    elif across == 2:
        value = getValue - 0.01
        paintValues(value)
    elif across == 3:
        value = getValue - 0.1
        paintValues(value)
    elif across == 4:
        value = getValue - 0.5
        paintValues(value)
    elif across == 5:
        value = getValue - 1
        paintValues(value)

def flood(flood):
    if flood == True :
        pm.artAttrCtx('artAttrSkinContext', edit = True, clear = True)
        pm.artAttrCtx('artAttrContext', edit = True, clear = True)
        pm.artAttrCtx('artAttrBlendShapeContext', edit = True, clear = True)

def paintValues(value):
    pm.artAttrCtx('artAttrSkinContext', edit = True, val = value)
    pm.artAttrCtx('artAttrContext', edit = True, val = value)
    pm.artAttrCtx('artAttrBlendShapeContext', edit = True, val = value)

def main():
    window = SkinValueWindow(qt.getMayaWindow())
    window.setWindowFlags(QtCore.Qt.Window)
    window.show()