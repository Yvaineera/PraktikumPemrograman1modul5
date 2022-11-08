def maksimal (maks, nilai):
    if(maks > nilai): 
        return maks
    else : 
        return nilai

def minimal (minim, nilai):
    if(minim < nilai) : 
        return minim
    else : 
        return nilai

for i in range(3):
    batas = 0 
    maks = -100000
    minim = 100000 
    bilangan = int(input())
    while batas < bilangan:
        nilai = map(int,input().split())
        for angka in nilai:
            maks = maksimal(maks, angka)
            minim = minimal(minim, angka)
            batas+=1
        print("%d %d\n"%(maks,minim));
