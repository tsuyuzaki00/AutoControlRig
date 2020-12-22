import maya.cmds as cmds
import maya.app.renderSetup.model.override as override
import maya.app.renderSetup.model.selector as selector
import maya.app.renderSetup.model.collection as collection
import maya.app.renderSetup.model.renderLayer as renderLayer
import maya.app.renderSetup.model.renderSetup as renderSetup

def shotImages():
    cmds.setAttr("defaultRenderGlobals.imageFormat", 32)
    fileName = "C:/Users/tsuyuzaki.tatsuya/Desktop/test.png"
    editor = "renderView"
    cmds.renderWindowEditor( editor, e = True, wi = fileName)

def main():
    shotImages()