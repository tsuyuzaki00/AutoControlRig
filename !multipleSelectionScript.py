import pymel.core as pm

def main():
    sels = selected()
    for sel in sels:
        part = sel.split('_')
        kansuu(sel,part)

def kansuu(sel,part):
    