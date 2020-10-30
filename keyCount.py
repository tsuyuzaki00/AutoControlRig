import pymel.core as pm

def countKey(interval = 10, threeKeys = 1, sels = ''):
    for sel in sels:
        pm.select(sel)
        num = 1 + 2 * threeKeys
        nowKey = pm.currentTime( query=True )
        for loopNum in range(num):
            pm.currentTime( nowKey )
            pm.setKeyframe()
            nowKey += interval

def main():
    sels = pm.selected()
    countKey(interval = 10, threeKeys = 2, sels = sels)

