def Biodata(thn, nm, asl):
    tahun_sekarang = 2020
    print("\nPerkenalkan Nama Saya :", nm)
    print("Umur Saya :", tahun_sekarang - thn)
    print("Saya adalah Angkatan:", tahun_sekarang)
    print("Asal Saya dari :", asl)

for i in range(2):
    thn = int(input())
    nm = input()
    asl = input()
    Biodata(thn, nm, asl)
    print("\n")