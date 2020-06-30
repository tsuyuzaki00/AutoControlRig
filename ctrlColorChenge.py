import os, json
from PySide2 import QtWidgets, QtCore, QtGui
from mainEdit import qt
import pymel.core as pm
class Settings(object):
    def __init__(self):
        temp = __name__.split('.')
        self.__filename = os.path.join(
			os.getenv('MAYA_APP_DIR'),
			temp[0],
			temp[-1]+'.json'
			)
        self.reset()
        self.read()
        
    def read(self):
        if os.path.exists(self.__filename):
            with open(self.__filename, 'r') as f:
                saveData = json.load(f)
                #self.guide = saveData['guide']
                #self.geometry = saveData['geometry']
                #self.joint = saveData['joint']
                #self.ctrl = saveData['ctrl']
                #self.camera = saveData['camera']
                #self.light = saveData['light']
    
    def reset(self):
        self.guide = False
        self.geometry = True
        self.joint = False
        self.ctrl = False
        self.camera = False
        self.light = False
        
    def save(self):
        saveData = { #'guide':self.guide,
                    #'geometry':self.geometry
                    #'joint':self.joint
                    #'ctrl':self.ctrl
                    #'camera':self.camera
                    #'light':self.light
                    }
        if not os.path.exists(self.__filename):
            os.makedirs(os.path.dirname(self.__filename))
        with open(self.__filename, 'w') as f:
            json.dump(saveData, f)

settings = Settings()

class OptionWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super(OptionWidget, self).__init__(*args, **kwargs)
        mainLayout = QtWidgets.QFormLayout(self)
        self.setWindowTitle('ctrlColorChenge')

        baseCenter1 = QtWidgets.QRadioButton('Base Yellow', self)
        secondCenter1 = QtWidgets.QRadioButton('Second Pale', self)
        autoCenter1 = QtWidgets.QRadioButton('AutoSupport Brown', self)
        baseCenter2 = QtWidgets.QRadioButton('Base Green', self)
        secondCenter2 = QtWidgets.QRadioButton('Second Green', self)
        autoCenter2 = QtWidgets.QRadioButton('AutoSupport Green', self)
        baseLeft = QtWidgets.QRadioButton('Base Blue', self)
        secondLeft = QtWidgets.QRadioButton('Second Cyan', self)
        autoLeft = QtWidgets.QRadioButton('AutoSupport Purple', self)
        baseRight = QtWidgets.QRadioButton('Base Red', self)
        secondRight = QtWidgets.QRadioButton('Second Pink', self)
        autoRight = QtWidgets.QRadioButton('AutoSupport Magenta', self)
        baseCenter1.setChecked(True)

        acrossLayout = QtWidgets.QHBoxLayout(self)
        acrossLayout.addWidget(baseCenter1, True)
        acrossLayout.addWidget(secondCenter1, True)
        acrossLayout.addWidget(autoCenter1, True)
        mainLayout.addRow('Center Color1', acrossLayout)

        acrossLayout = QtWidgets.QHBoxLayout(self)
        acrossLayout.addWidget(baseCenter2, True)
        acrossLayout.addWidget(secondCenter2, True)
        acrossLayout.addWidget(autoCenter2, True)
        mainLayout.addRow('Center Color2', acrossLayout)

        acrossLayout = QtWidgets.QHBoxLayout(self)
        acrossLayout.addWidget(baseLeft, True)
        acrossLayout.addWidget(secondLeft, True)
        acrossLayout.addWidget(autoLeft, True)
        mainLayout.addRow('Left Color', acrossLayout)

        acrossLayout = QtWidgets.QHBoxLayout(self)
        acrossLayout.addWidget(baseRight, True)
        acrossLayout.addWidget(secondRight, True)
        acrossLayout.addWidget(autoRight, True)
        mainLayout.addRow('Right Color', acrossLayout)

        self.__across = QtWidgets.QButtonGroup(self)
        self.__across.addButton(baseCenter1, 0)
        self.__across.addButton(secondCenter1, 1)
        self.__across.addButton(autoCenter1, 2)
        self.__across.addButton(baseCenter2, 3)
        self.__across.addButton(secondCenter2, 4)
        self.__across.addButton(autoCenter2, 5)
        self.__across.addButton(baseLeft, 6)
        self.__across.addButton(secondLeft, 7)
        self.__across.addButton(autoLeft, 8)
        self.__across.addButton(baseRight, 9)
        self.__across.addButton(secondRight, 10)
        self.__across.addButton(autoRight, 11)

        self.num = self.__across.checkedId()

        button = QtWidgets.QPushButton('chengeColor')

        widthLayout = QtWidgets.QHBoxLayout(self)
        widthLayout.addWidget(button, True)
        mainLayout.addRow(widthLayout)

        button.clicked.connect(self.chenge)

    def chenge(self):
        self.num = self.__across.checkedId()
        colorChange(self.num)

def colorChange(radio):
    sel = pm.selected()
    shapes = pm.listRelatives(sel[0:], type='nurbsCurve')
    for shape in shapes:
        pm.setAttr(shape + '.overrideEnabled', 1)
        if radio == 0:
            pm.setAttr(shape + '.overrideColor', 17)
        elif radio == 1:
            pm.setAttr(shape + '.overrideColor', 21)
        elif radio == 2:
            pm.setAttr(shape + '.overrideColor', 24)
        elif radio == 3:
            pm.setAttr(shape + '.overrideColor', 14)
        elif radio == 4:
            pm.setAttr(shape + '.overrideColor', 27)
        elif radio == 5:
            pm.setAttr(shape + '.overrideColor', 7 )
        elif radio == 6:
            pm.setAttr(shape + '.overrideColor', 6 )
        elif radio == 7:
            pm.setAttr(shape + '.overrideColor', 18)
        elif radio == 8:
            pm.setAttr(shape + '.overrideColor', 30)
        elif radio == 9:
            pm.setAttr(shape + '.overrideColor', 13)
        elif radio == 10:
            pm.setAttr(shape + '.overrideColor', 20)
        elif radio == 11:
            pm.setAttr(shape + '.overrideColor', 31)

def main():
    window = OptionWidget(qt.getMayaWindow())
    window.setWindowFlags(QtCore.Qt.Window)
    window.show()
