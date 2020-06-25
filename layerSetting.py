import os, json
from PySide2 import QtWidgets, QtGui
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
                self.guide = saveData['guide']
                #self.geometry = saveData['geometry']
    
    def reset(self):
        self.guide = True
        self.geometry = True
        
    def save(self):
        saveData = { 'guide':self.guide,
                    #'geometry':self.geometry
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

        self.__guide = QtWidgets.QCheckBox('guide',self)
        mainLayout.addRow('', self.__guide)

        self.__geometry = QtWidgets.QCheckBox('geometry',self)
        mainLayout.addRow('', self.__geometry)

        self.initialize()

    def initialize(self):
        self.__guide.setChecked(settings.guide)
        self.__geometry.setChecked(settings.geometry)

    def resetSettings(self):
        settings.reset()
        self.initialize()

    def saveSettings(self):
        settings.guide = self.__guide.isChecked()
        settings.geometry = self.__geometry.isChecked()
        settings.save()

    def apply(self):
        self.saveSettings()
        main()

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle('layerSetting')
        self.resize(400, 200)

        toolWidget = qt.ToolWidget(self)
        self.setCentralWidget(toolWidget)

        optionWidget = OptionWidget(self)
        toolWidget.setOptionWidget(optionWidget)

        toolWidget.setActionName(self.windowTitle())
        toolWidget.applied.connect(qt.Callback(optionWidget.apply))
        toolWidget.closed.connect(self.close)

        menuBar = self.menuBar()
        menu = menuBar.addMenu('File')
        action = menu.addAction('Save Settings')
        action.triggered.connect(optionWidget.saveSettings)

        action = menu.addAction('Reset Settings')
        action.triggered.connect(optionWidget.resetSettings)
		
def layerSetting(guide = True, geometry = True):
    sceneName = pm.sceneName().basename()
    part = sceneName.split("_")
    
    if pm.objExists(part[0]) or pm.objExists('scene'):
        pm.error('Group name already exists')
    
    if part[0].endswith('.ma') or part[0].endswith('.mb'):
        name = part[0][:-3]
    elif part[0] == '':
        name = 'scene'
    else:
        name = part[0]

    pm.select(all = True)
    layers = pm.selected(type='displayLayer')
    pm.select(cl = True)

    if guide == True or geometry == True:
        allGrp = pm.createNode('transform', n = name)

        if guide:
            guideGrp = pm.createNode('transform', n = '_'.join( ['grp','guide',name] ))
            pm.parent(guideGrp, allGrp)
            if layers == []:
                guideLayer = pm.createDisplayLayer(n = '_'.join( ['guide',name,'layer'] ))
                pm.editDisplayLayerMembers(guideLayer, guideGrp)
            for i in layers:
                if i == 'guide_' + name + '_layer':
                    guideLayer = 'guide_' + name + '_layer'
                    pm.editDisplayLayerMembers(guideLayer, guideGrp)
        
        if geometry:
            geometryGrp = pm.createNode('transform', n = '_'.join( ['grp','geometry',name] ))
            pm.parent(geometryGrp, allGrp)
            if layers == []:
                geometryLayer = pm.createDisplayLayer(n = '_'.join(['geometry',name,'layer'] ))
                pm.editDisplayLayerMembers(geometryLayer, geometryGrp)
            for i in layers:
                if i == 'geometry_' + name + '_layer':
                    geometryLayer = 'geometry_' + name + '_layer'
                    pm.editDisplayLayerMembers(geometryLayer, geometryGrp)


def option():
    window = MainWindow(qt.getMayaWindow())
    window.show()
    
def main():
	layerSetting(
        settings.guide,
        settings.geometry
        )