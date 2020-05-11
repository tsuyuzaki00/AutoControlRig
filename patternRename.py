import pymel.core as pm

def main():
    sels = pm.selected()[0:]
    for sel in sels:
        selb = sel[:-1]
        part = selb.split("_")
        name = part[0] + '_' + part[1] + '_' + part[-1] + '_' + part[-2]
        pm.rename ( sel, name )
    
main()