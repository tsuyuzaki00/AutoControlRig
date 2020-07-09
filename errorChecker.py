import os
from mainEdit import qt
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
import maya.cmds as cmds
import maya.api.OpenMaya as om

class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle('errorChecker')
        self.resize(90,200)
        widget = OptionWidget()
        self.setCentralWidget(widget)

class OptionWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super(OptionWidget, self).__init__(*args, **kwargs)
        mainLayout = QFormLayout(self)

        selectRadio = QRadioButton('Select', self)
        hierarchyRadio = QRadioButton('Hierarchy', self)
        allRadio = QRadioButton('All', self)
        selectRadio.setChecked(True)

        acrossLayout = QHBoxLayout(self)
        acrossLayout.addWidget(selectRadio, True)
        acrossLayout.addWidget(hierarchyRadio, True)
        acrossLayout.addWidget(allRadio, True)
        mainLayout.addRow(acrossLayout)

        #Object
        objectButton = QPushButton('Object', self)
        objectButton.setCheckable(True)
        '''objectButtonA = QPushButton('CheckAll ', self)
        objectButtonA.setChecked(True)
        objectButtonU = QPushButton('unCheckAll', self)
        objectButtonU.setChecked(True)'''
        frozenCheck = QCheckBox('FrozenTransform', self)
        frozenCheck.setChecked(True)
        pivotsCheck = QCheckBox('UnCenteredPivots', self)
        pivotsCheck.setChecked(True)
        hiddenCheck = QCheckBox('HiddenObject', self)
        hiddenCheck.setChecked(True)

        #Connect
        connectButton = QPushButton('Connect', self)
        connectButton.setCheckable(True)
        '''connectButtonA = QPushButton('CheckAll ', self)
        connectButtonA.setChecked(True)
        connectButtonU = QPushButton('unCheckAll', self)
        connectButtonU.setChecked(True)'''
        historyCheck = QCheckBox('History', self)
        historyCheck.setChecked(True)
        layerCheck = QCheckBox('Layer', self)
        layerCheck.setChecked(True)
        keyCheck = QCheckBox('KeyedObject', self)
        keyCheck.setChecked(True)
        constraintCheck = QCheckBox('Constraint', self)
        constraintCheck.setChecked(True)
        expressionCheck = QCheckBox('Expression', self)
        expressionCheck.setChecked(True)

        #Hierarchy
        hierarchyButton = QPushButton('Hierarchy', self)
        hierarchyButton.setCheckable(True)
        '''hierarchyButtonA = QPushButton('CheckAll ', self)
        hierarchyButtonA.setChecked(True)
        hierarchyButtonU = QPushButton('unCheckAll', self)
        hierarchyButtonU.setChecked(True)'''
        parentGeometryCheck = QCheckBox('ParentGeometry', self)
        parentGeometryCheck.setChecked(True)
        childNullCheck = QCheckBox('ChildNull', self)
        childNullCheck.setChecked(True)

        #Naming
        namingButton = QPushButton('Naming', self)
        namingButton.setCheckable(True)
        '''namingButtonA = QPushButton('CheckAll ', self)
        namingButtonA.setChecked(True)
        namingButtonU = QPushButton('unCheckAll', self)
        namingButtonU.setChecked(True)'''
        defaultNameCheck = QCheckBox('DefaultName', self)
        defaultNameCheck.setChecked(True)
        sameNameCheck = QCheckBox('SameName', self)
        sameNameCheck.setChecked(True)
        nameSpacesCheck = QCheckBox('NameSpaces', self)
        nameSpacesCheck.setChecked(True)

        #geometry
        geometryButton = QPushButton('Geometry', self)
        geometryButton.setCheckable(True)
        '''geometryButtonA = QPushButton('CheckAll ', self)
        geometryButtonA.setChecked(True)
        geometryButtonU = QPushButton('unCheckAll', self)
        geometryButtonU.setChecked(True)'''
        ngonCheck = QCheckBox('N-Gons', self)
        ngonCheck.setChecked(True)
        laminaCheck = QCheckBox('LaminaFace', self)
        laminaCheck.setChecked(True)
        concaveCheck = QCheckBox('ConcaveFaces', self)
        concaveCheck.setChecked(True)
        zeroEdgeCheck = QCheckBox('ZeroEdgeLength', self)
        zeroEdgeCheck.setChecked(True)
        LockedNormalsCheck = QCheckBox('LockedNormals', self)
        LockedNormalsCheck.setChecked(True)

        #UV
        uvButton = QPushButton('UV', self)
        uvButton.setCheckable(True)
        '''uvButtonA = QPushButton('CheckAll ', self)
        uvButtonA.setChecked(True)
        uvButtonU = QPushButton('unCheckAll', self)
        uvButtonU.setChecked(True)'''
        legalUV = QCheckBox('Legal UV', self)
        legalUV.setChecked(True)
        noUV = QCheckBox('No UV', self)
        noUV.setChecked(True)
        inversUV = QCheckBox('InversUV', self)
        inversUV.setChecked(True)
        penetratingUV = QCheckBox('PenetratingUV', self)
        penetratingUV.setChecked(True)

        #Matrial
        materialButton = QPushButton('Matrial', self)
        materialButton.setCheckable(True)
        '''materialButtonA = QPushButton('CheckAll ', self)
        materialButtonA.setChecked(True)
        materialButtonU = QPushButton('unCheckAll', self)
        materialButtonU.setChecked(True)'''
        defaultMat = QCheckBox('DefaultMatrial', self)
        defaultMat.setChecked(True)



        #leftLayoutSetting
        leftLayout = QVBoxLayout(self)
        leftLayout.addWidget(objectButton, True)
        '''leftLayout.addWidget(objectButtonA, True)
        leftLayout.addWidget(objectButtonU, True)'''
        leftLayout.addWidget(frozenCheck, True)
        leftLayout.addWidget(pivotsCheck, True)
        leftLayout.addWidget(hiddenCheck, True)

        leftLayout.addWidget(connectButton, True)
        '''leftLayout.addWidget(connectButtonA, True)
        leftLayout.addWidget(connectButtonU, True)'''
        leftLayout.addWidget(historyCheck, True)
        leftLayout.addWidget(layerCheck, True)
        leftLayout.addWidget(keyCheck, True)
        leftLayout.addWidget(constraintCheck, True)
        leftLayout.addWidget(expressionCheck, True)

        leftLayout.addWidget(namingButton, True)
        '''leftLayout.addWidget(namingButtonA, True)
        leftLayout.addWidget(namingButtonU, True)'''
        leftLayout.addWidget(defaultNameCheck, True)
        leftLayout.addWidget(sameNameCheck, True)
        leftLayout.addWidget(nameSpacesCheck, True)

        leftLayout.addWidget(hierarchyButton, True)
        '''leftLayout.addWidget(hierarchyButtonA, True)
        leftLayout.addWidget(hierarchyButtonU, True)'''
        leftLayout.addWidget(parentGeometryCheck, True)
        leftLayout.addWidget(childNullCheck, True)

        leftLayout.addWidget(geometryButton, True)
        '''leftLayout.addWidget(geometryButtonA, True)
        leftLayout.addWidget(geometryButtonU, True)'''
        leftLayout.addWidget(ngonCheck, True)
        leftLayout.addWidget(laminaCheck, True)
        leftLayout.addWidget(concaveCheck, True)
        leftLayout.addWidget(zeroEdgeCheck, True)
        leftLayout.addWidget(LockedNormalsCheck, True)

        leftLayout.addWidget(uvButton, True)
        '''leftLayout.addWidget(uvButtonA, True)
        leftLayout.addWidget(uvButtonU, True)'''
        leftLayout.addWidget(legalUV, True)
        leftLayout.addWidget(noUV, True)
        leftLayout.addWidget(inversUV, True)
        leftLayout.addWidget(penetratingUV, True)

        leftLayout.addWidget(materialButton, True)
        '''leftLayout.addWidget(materialButtonA, True)
        leftLayout.addWidget(materialButtonU, True)'''
        leftLayout.addWidget(defaultMat, True)


        mainLayout.addRow(leftLayout)
        
        #rightLayoutSetting
        rightLayout = QVBoxLayout(self)
        rightLayout.addWidget(QLabel('OK'))
        rightLayout.addWidget(QTreeView())
        rightLayout.addWidget(QLabel('NG'))
        rightLayout.addWidget(QTreeView())
        mainLayout.addRow(rightLayout)

        #backLayoutSetting
        backLayout = QHBoxLayout(self)
        runButton = QPushButton('checkRun', self)
        runButton.setCheckable(True)
        allRunButton = QPushButton('checkAllRun', self)
        allRunButton.setCheckable(True)
        backLayout.addWidget(runButton, True)
        backLayout.addWidget(allRunButton, True)
        mainLayout.addRow(backLayout)





        




def main():
    window = MainWindow(qt.getMayaWindow())
    window.setWindowFlags(Qt.Window)
    window.show()