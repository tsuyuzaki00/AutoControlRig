import pymel.core as pm

def main():
    countKey(15,1)

def countKey(interval,rotate):
    num = 1 + 2 * rotate
    nowKey = pm.currentTime( query=True )
    for loopNum in range(num):
        pm.currentTime( nowKey )
        pm.setKeyframe()
        nowKey += interval

main()
'''
startKey = 0
finalTime = 150
while nowKey <= finalTime:
    pm.currentTime( nowKey )
    pm.setKeyframe()
    nowKey += interval
    '''