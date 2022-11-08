#include <stdio.h>

int MaxBilangan (int c, int a, int s, int e){
    if(c > a && c > s && c > e){
        return c;}
    else if(a > c && a > s && a > e){
        return a;}
    else if(s > c && s > a && s > e){
        return s;}
    else{
        return e;}
}

int main(){
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d); 
    int hasil = MaxBilangan(a, b, c, d); 
    printf("%d", hasil);
    return 0;
}
