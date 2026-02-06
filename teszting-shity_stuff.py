import time

def dino():
    while True:
        print("dino")
        yield 0.5   # 0.5 masodperc mulva innen folytatjuk, addig a tobbiek futank (mint a time.sleep())

def kaktusz():
    while True:
        print("kaktusz")
        yield 0.3   # 0.3 masodperc mulva innen folytatjuk, addig a tobbiek futank (mint a time.sleep())

feladatok = { dino(): 0, kaktusz(): 0}

# utemezes
while True:
    most = time.time()
    
    for feladat, hatarido in list(feladatok.items()):       # menjunk vegig a futtathato feladatokon
        if most >= hatarido:                                # ha ideje futtani a feladatot
            feladatok[feladat] = most + next(feladat)       # akkor fusson es mentsuk el az uj hataridot

    time.sleep(min(feladatok.values()) - most)