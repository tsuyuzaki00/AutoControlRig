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
        self.resize(200,400)

        widget = OptionWidget()
        self.setCentralWidget(widget)

class SelectionRadio(QWidget):
    def __init__(self, *args, **kwargs):
        super(SelectionRadio,self).__init__(*args, **kwargs)

        self.selectRadio = QRadioButton('Select', self)
        self.hierarchyRadio = QRadioButton('Hierarchy', self)
        self.allRadio = QRadioButton('All', self)
        self.selectRadio.setChecked(True)

        acrossLayout = QHBoxLayout(self)
        acrossLayout.addWidget(self.selectRadio)
        acrossLayout.addWidget(self.hierarchyRadio)
        acrossLayout.addWidget(self.allRadio)

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

        checkBox = QCheckBox(self.checkType, self)
        checkBox.setChecked(True)
        checkBoxLayout.addWidget(checkBox, True)
        runButton = QPushButton('Run', self)
        runButton.setChecked(True)
        checkBoxLayout.addWidget(runButton, True)

class ScrollBar(QWidget):
    def __init__(self, *args, **kwargs):
        super(ScrollBar, self).__init__(*args, **kwargs)
        scrollLayout = QVBoxLayout(self)

        _container = Container('test')
        _checkBox = CheckBox('test')

        scrollLayout.addWidget(_container)
        scrollLayout.addWidget(_checkBox)
        

class ListTree(QWidget):
    def __init__(self, *args, **kwargs):
        super(ListTree, self).__init__(*args, **kwargs)
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

    def OKItem(self, parameter_list):
        pass

    def NGItem(self, parameter_list):
        pass

class Run(QWidget):
    def __init__(self, *args, **kwargs):
        super(Run, self).__init__(*args, **kwargs)
        runLayout = QHBoxLayout(self)

        checkAllButton = QPushButton('checkUnAll', self)
        checkAllButton.setChecked(True)
        runLayout.addWidget(checkAllButton)
        checkUnAllButton = QPushButton('checkAll', self)
        checkUnAllButton.setChecked(True)
        runLayout.addWidget(checkUnAllButton)
        runButton = QPushButton('checkRun', self)
        runButton.setChecked(True)
        runLayout.addWidget(runButton)
        allRunButton = QPushButton('allRun', self)
        allRunButton.setChecked(True)
        runLayout.addWidget(allRunButton)

class OptionWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super(OptionWidget, self).__init__(*args, **kwargs)

        optionLayout = QVBoxLayout(self)

        _selectionRadio = SelectionRadio()
        _scrollBar = ScrollBar()
        _listTree = ListTree()
        _run = Run()

        optionLayout.addWidget(_selectionRadio)
        optionLayout.addWidget(_scrollBar)
        optionLayout.addWidget(_listTree)
        optionLayout.addWidget(_run)
        

def main():
    window = MainWindow(qt.getMayaWindow())
    window.show()