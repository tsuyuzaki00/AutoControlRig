import maya.cmds as cmds

width = 1920
height = 1080
cameras = [["camera1", (0,0,5), (0,0,0)], ["camera2", (5,0,0), (0,90,0)]]
fileName = "testScriptRender"
image = "png"
path = "D:/Maya/images/"
using = "arnold"
cameraName = 'front'

def createPhotographSet(name = 'image_000', trs = (0, 0, 5), rot = (0,0,0)):
    camShapes = cmds.camera()
    litShape = cmds.spotLight()
    litParent = cmds.listRelatives(litShape, p = True)
    cam = cmds.rename(camShapes[0], "shotCam_" + name)
    lit = cmds.rename(litParent, "shotLit_" + name)
    cmds.setAttr(cam + ".translate", trs[0], trs[1], trs[2], type = "double3")
    cmds.setAttr(cam + ".rotate", rot[0], rot[1], rot[2], type = "double3")
    cmds.setAttr(lit + ".translate", trs[0], trs[1], trs[2], type = "double3")
    cmds.setAttr(lit + ".rotate", rot[0], rot[1], rot[2], type = "double3")
    cmds.parent(lit, cam)
    return cam

def shotImages(cam = '', width = 1920, height = 1080, imageFormat = 32, path = '', fileName = ''):
    cmds.setAttr("defaultResolution.width", width)
    cmds.setAttr("defaultResolution.height", height)
    cmds.setAttr("defaultRenderGlobals.imageFormat", imageFormat)
    fullPathName = path + fileName
    cmds.colorManagementPrefs(q = True , cmEnabled = True)
    cmds.renderWindowEditor("renderView", e = True, si = True, crg = cam, wi = fullPathName)

def save():
    createPhotographSet(name = cameraName, trs = (5.987, 3.484, 6.591), rot = (-16.311, 43.027, 0.0))
    cmds.file(save = True)

def delete():
    cmds.delete('shotCam_' + 'front')
    cmds.file(save = True)
