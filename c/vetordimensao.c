#include "stdio.h"
#include <stdlib.h>

double * criar(int n){
    double *v;
    v = malloc(n*sizeof(double));
    return v;
}

double * vetor( double v[],int n){
    printf("Digite %d Valores: ",n);
    for (int l; l<n; l++) {
        fgets(v, n,stdin);
    }
    return v;
}

double * soma(double *v1,double *v2,int n){
    double *soma; 
    for (int i= 0; i<n ; i++) {
        
    }
    
    return soma;
}

double * aloca(int n){
    double *v1,*v2,*saida;
    v1 = vetor(criar(n), n);
    v2 = vetor(criar(n), n);
    saida = soma(v1,v2);


}

int main(){

    int n;
    double *v1,*v2;

    scanf("%d",&n);

    aloca(n);



    return 0;
}

