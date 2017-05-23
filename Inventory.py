import pprint
def displayInventar(inventar):
    cnt=0
    for key,value in inventar.items():
        print(str(value)+' '+key)
        cnt+=int(value)
    print('Count = '+str(cnt))

def addToInventory(inventar, addedItems):
    for vl in addedItems:
        if(not inventar.has_key(vl)):
            inventar.setdefault(vl, 0)
        inventar[vl] += 1


inv={'rope':1,'torch':2,'gold coin':3}
dragonLoot=['gold coin','dagger', 'gold coin','rope']
addToInventory(inv,dragonLoot)

displayInventar(inv)
