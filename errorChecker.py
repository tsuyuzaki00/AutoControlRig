import os
from os import name
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

class ContainerButtons():
    def __init__(self, parent = None):
        super(ContainerButtons, self).__init__(*args, **kwargs)

        containerLayout = QHBoxLayout(self)

        hideButton = QPushButton(name, self)
        hideButton.setCheckable(True)
        containerLayout.addWidget(hideButton, True)

        checkAllButton = QPushButton('CheckAll ', self)
        checkAllButton.setChecked(True)
        containerLayout.addWidget(checkAllButton, True)
        
        unCheckAllButton = QPushButton('unCheckAll', self)
        unCheckAllButton.setChecked(True)
        containerLayout.addWidget(unCheckAllButton, True)

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

        useLayout = QHBoxLayout(self)
        mainLayout.addRow(useLayout)

        leftLayout = QVBoxLayout(self)

        #Object
        hiddenObjectLayout = QHBoxLayout(self)
        objectButton = QPushButton('Object', self)
        objectButton.setCheckable(True)
        hiddenObjectLayout.addWidget(objectButton, True)
        objectButtonA = QPushButton('CheckAll ', self)
        objectButtonA.setChecked(True)
        hiddenObjectLayout.addWidget(objectButtonA, True)
        objectButtonU = QPushButton('unCheckAll', self)
        objectButtonU.setChecked(True)
        hiddenObjectLayout.addWidget(objectButtonU, True)
        mainLayout.addRow(hiddenObjectLayout)

        checkBoxfrozenLayout = QHBoxLayout(self)
        frozenCheck = QCheckBox('FrozenTransform', self)
        frozenCheck.setChecked(True)
        checkBoxfrozenLayout.addWidget(frozenCheck, True)
        frozenRunButton = QPushButton('Run', self)
        frozenRunButton.setChecked(True)
        checkBoxfrozenLayout.addWidget(frozenRunButton, True)
        mainLayout.addRow(checkBoxfrozenLayout)

        checkBoxPivotsLayout = QHBoxLayout(self)
        pivotsCheck = QCheckBox('UnCenteredPivots', self)
        pivotsCheck.setChecked(True)
        checkBoxPivotsLayout.addWidget(pivotsCheck, True)
        pivotsRunButton = QPushButton('Run', self)
        pivotsRunButton.setChecked(True)
        checkBoxPivotsLayout.addWidget(pivotsRunButton, True)
        mainLayout.addRow(checkBoxPivotsLayout)
        
        checkBoxHiddenLayout = QHBoxLayout(self)
        hiddenCheck = QCheckBox('HiddenObject', self)
        hiddenCheck.setChecked(True)
        checkBoxHiddenLayout.addWidget(hiddenCheck, True)
        hiddenRunButton = QPushButton('Run', self)
        hiddenRunButton.setChecked(True)
        checkBoxHiddenLayout.addWidget(hiddenRunButton, True)
        mainLayout.addRow(checkBoxHiddenLayout)

        #Connect
        hiddenConnectLayout = QHBoxLayout(self)
        connectButton = QPushButton('Connect', self)
        connectButton.setCheckable(True)
        hiddenConnectLayout.addWidget(connectButton, True)
        connectButtonA = QPushButton('CheckAll ', self)
        connectButtonA.setChecked(True)
        hiddenConnectLayout.addWidget(connectButtonA, True)
        connectButtonU = QPushButton('unCheckAll', self)
        connectButtonU.setChecked(True)
        hiddenConnectLayout.addWidget(connectButtonU, True)
        mainLayout.addRow(hiddenConnectLayout)

        checkBoxHistoryLayout = QHBoxLayout(self)
        historyCheck = QCheckBox('History', self)
        historyCheck.setChecked(True)
        checkBoxHistoryLayout.addWidget(historyCheck, True)
        historyRunButton = QPushButton('Run', self)
        historyRunButton.setChecked(True)
        #historyRunButton.clicked.connect(self._setHistory)
        checkBoxHistoryLayout.addWidget(historyRunButton, True)
        mainLayout.addRow(checkBoxHistoryLayout)

        #rightLayoutSetting
        #rightLayout = QVBoxLayout(self)
        #useLayout.addWidget(rightLayout)
        
        #listTreeLayoutSetting
        listTreeLayout = QVBoxLayout(self)

        OKobject = 'OKobject'
        listTreeLayout.addWidget(QLabel('OK'))
        OKWidget = QListWidget()
        OKItem = QLineEdit(OKobject)
        OKWidget.addItem(OKItem.text())
        listTreeLayout.addWidget(OKWidget)
        
        NGobject = ['NGobject']
        NGlist = ['NGlist']
        listTreeLayout.addWidget(QLabel('NG'))
        NGWidget = QTreeWidget()
        NGItem = QTreeWidgetItem(NGobject)
        NGWidget.addTopLevelItem(NGItem)
        QTreeWidgetItem(NGItem, NGlist)
        NGWidget.setSelectionMode(QAbstractItemView.ContiguousSelection)
        listTreeLayout.addWidget(NGWidget)

        mainLayout.addRow(listTreeLayout)

        #runLayoutSetting
        runLayout = QHBoxLayout(self)

        runButton = QPushButton('checkRun', self)
        runButton.setChecked(True)
        allRunButton = QPushButton('allRun', self)
        allRunButton.setChecked(True)
        runLayout.addWidget(runButton, True)
        runLayout.addWidget(allRunButton, True)
        mainLayout.addRow(runLayout)

        def _setHistory(self):
            print 'his'

def history(self, list):
    history = []
    for obj in list:
        shape = cmds.listRelatives(obj, shapes = True, fullPath = True)
        if shape is not None:
            if cmds.nodeType(shape[0]) == 'mesh':
                historySize = len(cmds.listHistory(shape))
                if historySize > 1:
                    history.append(obj)
    return history

def history_objects(self,*args):
    ## find all history information
    historyList=[]
    shadingGroupList=[]
    
    totalObjects = len(self.uniqueGeometryList)
    percentage = 100.0 / totalObjects
    iteration = 1;
    self.currentWorkingItem.setText('History')
    for i in self.uniqueGeometryList:
        history = cmds.listHistory(i)
        shapeNode = cmds.listRelatives(i,ad=True, s=True)
        for shape in shapeNode:
            if not cmds.objExists(shape + '.instObjGroups[0]'):
                continue
            shadingGroup = cmds.listConnections(shape + '.instObjGroups[0]')
            if not shadingGroup == None:
                shadingGroupList.append(shadingGroup[0])
            objGroup = cmds.listConnections(shape + '.instObjGroups[0]')
            if not objGroup == None:
                shadingGroupList.append(objGroup[0])
        for j in history:
            if not j in self.allShapes and not j in shadingGroupList:
                if not 'groupId' in j and not 'lambert2SG' in j:
                    if not 'initialShadingGroup' in j and not 'doneUV' in j:
                        historyList.append(i)
        self.CurrentTool_progressBar.setValue(percentage*iteration)
        qApp.processEvents()
        iteration+=1;

def main():
    window = MainWindow(qt.getMayaWindow())
    window.setWindowFlags(Qt.Window)
    window.show()