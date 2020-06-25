import os, json
from PySide2 import QtWidgets, QtGui
from mainEdit import qtTest as qt
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
		
	def reset(self):
		self.guide = True

	def save(self):
		saveData = { 
                    'guide':self.guide
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
			
    def apply(self):
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

        #toolWidget.setActionName("hogehoge")
		toolWidget.applied.connect(qt.Callback(optionWidget.apply))
		toolWidget.closed.connect(self.close)
		
def layerSetting(guide = True):
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


    if guide == True:
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


def option():
    window = MainWindow(qt.getMayaWindow())
    window.show()
    
def main():
	layerSetting(settings.guide)