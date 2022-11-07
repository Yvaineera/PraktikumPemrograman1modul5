#include <stdio.h>

void Biodata(int thn, char *nm[20], char *as[15]){
    int tahun_sekarang = 2020;
    printf("\nPerkenalkan Nama Saya : %s\n", nm);
    printf("Umur Saya : %d\n", tahun_sekarang - thn);
    printf("Saya adalah Angkatan : %d\n", tahun_sekarang);
    printf("Asal Saya dari : %s", as);
}

int main(){
    int tahunLahir;
        char Namaku[20], Asal[15];
        scanf(" %d",&tahunLahir); 
        scanf(" %[^\n]%*c",&Namaku);
        scanf(" %[^\n]%*c",&Asal); 
    Biodata(tahunLahir, Namaku, Asal); 
    return 0;
}