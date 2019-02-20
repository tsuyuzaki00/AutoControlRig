import pymel.core as pm

sel = pm.selected()[0]
grpName = sel.name()

checkStr = '_grp'
if grpName.endswith(checkStr):
    grpName = grpName[:-len(checkStr)]

targetList = []
for obj in sel.getChildren():
    if obj.getShape().type() == 'mesh':
        targetList.append( obj )

suffix = 'geo'

for num,obj in enumerate( targetList , 1):
    numStr = str(num).zfill(2)
    obj.rename( '_'.join([grpName,suffix,numStr]) )

print 'sel:',sel
print 'grpName:',grpName
