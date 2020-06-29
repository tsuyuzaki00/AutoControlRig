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

        baseCenter = QtWidgets.QRadioButton('Base Yellow', self)
        secondCenter = QtWidgets.QRadioButton('Second Green', self)
        autoCenter = QtWidgets.QRadioButton('AutoSupport Green', self)
        baseLeft = QtWidgets.QRadioButton('Base Blue', self)
        secondLeft = QtWidgets.QRadioButton('Second Cyan', self)
        autoLeft = QtWidgets.QRadioButton('AutoSupport Purple', self)
        baseRight = QtWidgets.QRadioButton('Base Red', self)
        secondRight = QtWidgets.QRadioButton('Second Pink', self)
        autoRight = QtWidgets.QRadioButton('AutoSupport Magenta', self)
        baseCenter.setChecked(True)
        baseLeft.setChecked(True)
        baseRight.setChecked(True)

        acrossLayout = QtWidgets.QHBoxLayout(self)
        acrossLayout.addWidget(baseCenter, True)
        acrossLayout.addWidget(secondCenter, True)
        acrossLayout.addWidget(autoCenter, True)
        mainLayout.addRow('Center Color', acrossLayout)

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
        self.__across.addButton(baseCenter, 0)
        self.__across.addButton(secondCenter, 1)
        self.__across.addButton(autoCenter, 2)
        self.__across.addButton(baseLeft, 3)
        self.__across.addButton(secondLeft, 4)
        self.__across.addButton(autoLeft, 5)
        self.__across.addButton(baseRight, 6)
        self.__across.addButton(secondRight, 7)
        self.__across.addButton(autoRight, 8)

        self.num = self.__across.checkedId()
'''
        dialog = QtWidgets.QColorDialog(qt.getMayaWindow())
        result = dialog.exec_()
        if result:
	        print dialog.selectedColor()
        mainLayout.addRow(dialog)
'''
def main():
    window = OptionWidget(qt.getMayaWindow())
    window.setWindowFlags(QtCore.Qt.Window)
    window.show()
