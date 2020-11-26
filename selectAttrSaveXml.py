import pymel.core as pm
import xml.etree.ElementTree as ET

def writeXml(xmlRoot, path):
    import xml.dom.minidom as md
    encode = "utf-8"
    xmlFile = open(path, "w")
    document = md.parseString(ET.tostring(xmlRoot, encode))
    document.writexml(
        xmlFile,
        encoding = encode,
        newl = "\n",
        indent = "",
        addindent = "\t"
    )

def objAttrExportXml(filePass = ''):
    sels = pm.selected()
    title = ET.Element('object')
    for sel in sels:
        node = ET.SubElement(title, 'node', { 'name' : str(sel) })
        pm.select(sel)
        selLists = pm.listAttr(k=True)
        for selList in selLists:
            selAttr = pm.getAttr(sel + '.' + selList)
            attribute = ET.SubElement(node, 'attribute', { 'string' : str(selList), 'value' : str(round(selAttr, 3))})
    
    ET.dump(title) 
    writeXml(title, filePass)
 
def objAttrImportXml(filePass = ''):
    inFile = filePass
    tree = ET.parse(inFile) 
    root = tree.getroot()

    '''
    for node in root.iter('attribute'):
        attrs = node.findall('node')
        attrName = node.get('string')
        attrValue = node.get('value')
        print (attrs, attrName, attrValue)
    '''

    for node in root:
        objName = node.attrib
        for child in root.iter('attribute'):
            attrs = child.attrib
            print (objName, attrs)

            pm.select(objName['name'])
            pm.setAttr(objName['name'] + '.' + attrs['string'], float(attrs['value']))
        

def main():
    filePass = 'D:/Maya/scripts/testScripts/output.xml'
    objAttrExportXml(filePass = filePass)
    objAttrImportXml(filePass = filePass)

filePass = 'C:/Users/tsuyuzaki.tatsuya/Desktop/test/output.xml'
#objAttrExportXml(filePass = filePass)
objAttrImportXml(filePass = filePass)