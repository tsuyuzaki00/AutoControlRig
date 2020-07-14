from DL.modelChecker.src.modelChecker import history
from mainEdit.lookNodeType import checkNodeType
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
        self.resize(450,800)

        widget = OptionWidget()
        self.setCentralWidget(widget)

class SelectionRadio(QWidget):
    def __init__(self, *args, **kwargs):
        super(SelectionRadio,self).__init__(*args, **kwargs)

        selectionLayout = QHBoxLayout(self)

        self.selectRadio = QRadioButton('Select', self)
        self.hierarchyRadio = QRadioButton('Hierarchy', self)
        self.allRadio = QRadioButton('All', self)
        self.selectRadio.setChecked(True)

        selectionLayout.addWidget(self.selectRadio, True)
        selectionLayout.addWidget(self.hierarchyRadio, True)
        selectionLayout.addWidget(self.allRadio, True)

        self.__selectionLayout = QButtonGroup(self)
        self.__selectionLayout.addButton(self.selectRadio, 0)
        self.__selectionLayout.addButton(self.hierarchyRadio, 1)
        self.__selectionLayout.addButton(self.allRadio, 2)

        if self.sender() == self.selectRadio:
            sels = cmds.ls(sl = True)
            return sels
        elif self.sender() == self.hierarchyRadio:
            sels = cmds.ls(sl = True, dag = True, tr = True)
            return sels
        elif self.sender() == self.allRadio:
            sels = cmds.ls(tr = True, v = True)
            return sels

class Container(QWidget):
    def __init__(self, checkName, *args, **kwargs):
        super(Container, self).__init__(*args, **kwargs)
        self.checkName = checkName

        containerLayout = QHBoxLayout(self)

        hideButton = QPushButton(self.checkName, self)
        hideButton.setCheckable(True)
        containerLayout.addWidget(hideButton, True)

        checkAllButton = QPushButton('Check\n' + self.checkName, self)
        checkAllButton.setChecked(True)
        containerLayout.addWidget(checkAllButton, True)
        
        unCheckAllButton = QPushButton('unCheck\n' + self.checkName, self)
        unCheckAllButton.setChecked(True)
        containerLayout.addWidget(unCheckAllButton, True)

class CheckBox(QWidget):
    def __init__(self, checkType, *args, **kwargs):
        super(CheckBox, self).__init__(*args, **kwargs)
        self.checkType = checkType
        checkBoxLayout = QHBoxLayout(self)

        self.getCheckBox(checkBoxLayout)
        self.getRunButton(checkBoxLayout)

    def getCheckBox(self,checkBoxLayout):
        checkBox = QCheckBox(self.checkType, self)
        checkBox.setChecked(True)
        checkBoxLayout.addWidget(checkBox, True)

    def getRunButton(self,checkBoxLayout):
        runButton = QPushButton('Run', self)
        runButton.setChecked(True)
        checkBoxLayout.addWidget(runButton, True)
        runButton.clicked.connect(self.setRunButton)

    def setRunButton(self):
        print 'test'

class ScrollBar(QWidget):
    def __init__(self, *args, **kwargs):
        super(ScrollBar, self).__init__(*args, **kwargs)
        mainLayout = QHBoxLayout(self)
         
        scrollArea = QScrollArea(self)
        scrollArea.setWidgetResizable(True)
        scrollArea.setMinimumWidth(250)
        mainLayout.addWidget(scrollArea)

        _checkGrp = CheckGrp(self)
        scrollArea.setWidget(_checkGrp)

class CheckGrp(QWidget):
    def __init__(self, *args, **kwargs):
        super(CheckGrp, self).__init__(*args, **kwargs)
        scrollLayout = QVBoxLayout(self)

        _object = Container('Object')
        scrollLayout.addWidget(_object)
        
        _frozenBox = CheckBox('FrozenTransform')
        scrollLayout.addWidget(_frozenBox)

        _objectBox = CheckBox('UnCenteredPivots')
        scrollLayout.addWidget(_objectBox)

        _objectBox = CheckBox('HiddenObject')
        scrollLayout.addWidget(_objectBox)


        _connect = Container('Connect')
        scrollLayout.addWidget(_connect)
        connectLists = [
                        'History',
                        'Layer',
                        'KeyedObject',
                        'Constraint',
                        'Expression',
                        ]
        for connectList in connectLists:
            _connectBox = CheckBox(connectList)
            scrollLayout.addWidget(_connectBox)

        _naming = Container('Naming')
        scrollLayout.addWidget(_naming)
        namingLists = [
                        'DefaultName',
                        'SameName',
                        'NameSpaces',
                        ]
        for namingList in namingLists:
            _namingBox = CheckBox(namingList)
            scrollLayout.addWidget(_namingBox)

        _hierarchy = Container('Hierarchy')
        scrollLayout.addWidget(_hierarchy)
        hierarchyLists = [
                        'ParentGeometry',
                        'ChildNull',
                        ]
        for hierarchyList in hierarchyLists:
            _hierarchyBox = CheckBox(hierarchyList)
            scrollLayout.addWidget(_hierarchyBox)

        _geometry = Container('Geometry')
        scrollLayout.addWidget(_geometry)
        geometryLists = [
                        'N-Gons',
                        'LaminaFace',
                        'ConcaveFaces',
                        'ZeroEdgeLength',
                        'LockedNormals',
                        ]
        for geometryList in geometryLists:
            _geometryBox = CheckBox(geometryList)
            scrollLayout.addWidget(_geometryBox)

        _uv = Container('UV')
        scrollLayout.addWidget(_uv)
        uvLists = [
                        'Legal UV',
                        'PenetratingUV',
                        'InversUV',
                        'No UV',
                        ]
        for uvList in uvLists:
            _uvBox = CheckBox(uvList)
            scrollLayout.addWidget(_uvBox)

        _matrial = Container('Matrial')
        scrollLayout.addWidget(_matrial)
        matrialLists = [
                        'DefaultMaterial',
                        ]
        for matrialList in matrialLists:
            _matrialBox = CheckBox(matrialList)
            scrollLayout.addWidget(_matrialBox)

    def button(self):
        print 'test'

class ListTree(QWidget):
    def __init__(self, *args, **kwargs):
        super(ListTree, self).__init__(*args, **kwargs)
        listTreeLayout = QVBoxLayout(self)

        OKobject = ['OKType']
        OKlist = ['OKobject']
        listTreeLayout.addWidget(QLabel('OK'))
        OKWidget = QTreeWidget()
        OKItem = QTreeWidgetItem(OKobject)
        OKWidget.addTopLevelItem(OKItem)
        QTreeWidgetItem(OKItem, OKlist)
        OKWidget.setSelectionMode(QAbstractItemView.ContiguousSelection)
        listTreeLayout.addWidget(OKWidget)
        
        NGobject = ['NGtype']
        NGlist = ['NGobject']
        listTreeLayout.addWidget(QLabel('NG'))
        NGWidget = QTreeWidget()
        NGItem = QTreeWidgetItem(NGobject)
        NGWidget.addTopLevelItem(NGItem)
        QTreeWidgetItem(NGItem, NGlist)
        NGWidget.setSelectionMode(QAbstractItemView.ContiguousSelection)
        listTreeLayout.addWidget(NGWidget)

    def OKItem(self, parameter_list):
        pass

    def NGItem(self, parameter_list):
        pass

class RunButton(QWidget):
    def __init__(self, *args, **kwargs):
        super(RunButton, self).__init__(*args, **kwargs)
        runLayout = QHBoxLayout(self)

        checkAllButton = QPushButton('checkAll', self)
        checkAllButton.setChecked(True)
        runLayout.addWidget(checkAllButton)
        checkAllButton.clicked.connect(self.setCheckAll)

        checkUnAllButton = QPushButton('checkUnAll', self)
        checkUnAllButton.setChecked(True)
        runLayout.addWidget(checkUnAllButton)
        checkUnAllButton.clicked.connect(self.setCheckUnAll)

        runButton = QPushButton('checkRun', self)
        runButton.setChecked(True)
        runLayout.addWidget(runButton)
        runButton.clicked.connect(self.setCheckRun)
        
        allRunButton = QPushButton('allRun', self)
        allRunButton.setChecked(True)
        runLayout.addWidget(allRunButton)
        allRunButton.clicked.connect(self.setAllRun)

    def setCheckAll(self):
        _run = Run()
        _run.history()

    def setCheckUnAll(self,runLayout):
        _run = Run()
        _run.history()

    def setCheckRun(self,runLayout):
        _run = Run()
        _run.history()

    def setAllRun(self,runLayout):
        _run = Run()
        _run.history()

class OptionWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super(OptionWidget, self).__init__(*args, **kwargs)

        optionLayout = QGridLayout(self)

        _selectionRadio = SelectionRadio()
        print _selectionRadio
        _scrollBar = ScrollBar()
        _listTree = ListTree()
        _run = RunButton()

        optionLayout.addWidget(_selectionRadio,0,0,1,0)
        optionLayout.addWidget(_scrollBar, 1, 0)
        optionLayout.addWidget(_listTree, 1, 1)
        optionLayout.addWidget(_run, 2, 0, 2, 2)

class Run():
    def __init__(self, *args, **kwargs):
        pass

    def history(self):
        print 'hoge'


def main():
    _run = Run()
    window = MainWindow(qt.getMayaWindow())
    window.show()