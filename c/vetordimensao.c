#include "stdio.h"
#include <stdlib.h>

int * criar(int n){
    int *v;
    v = malloc(n*sizeof(int));
    return v;
}

int * vetor( int v[],int n){
    for (int l = 0; l<n; l++) {
        printf("Digite Valores: ",n);
        scanf("%d",&v[l]);
    }
    return v;
}

int * soma(int *v1,int *v2,int n){
    int sun = 0,*s; 
    for (int i= 0; i<n ; i++) {
        sun = v1[i] + v2[i]+ sun;
    }
    printf("a soma é essa %d\n",sun);
    s = &sun;
    return s;
}

int * aloca(int n){
    int *v1,*v2,*saida;
    v1 = vetor(criar(n), n);
    v2 = vetor(criar(n), n);
    saida = soma(v1,v2,n);

    return saida;

}

int main(){

    int n;
    int v;

    scanf("%d",&n);

    v = *aloca(n);



    return 0;
}

