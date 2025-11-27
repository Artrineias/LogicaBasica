#include <stdio.h>

typedef struct numeros {

    int vetor[3];
    int soma;

};

int entrada(){
    int saida;
    printf("Digite um valor: ");
    scanf("%d",&saida);
    return saida;
}

int somador(int n1, int n2,int n3){

    int saida;

    saida = n1 + n2 + n3;
    
    return saida;
}

void saida(int v1,int v2,int v3,int soma){
    int vetor[3] = {v1,v2,v3};
    for(int i = 1; i<=3 ;i++){
        printf("%d°Numero: %d\n",i,vetor[i-1]);
    }
    printf("soma: %d\n",soma);
}

int main() {

    struct numeros numero;
    numero.vetor[0] = entrada();
    numero.vetor[1] = entrada();
    numero.vetor[2] = entrada();
    
    numero.soma = somador(numero.vetor[0],numero.vetor[1],numero.vetor[2]);

    saida(numero.vetor[0],numero.vetor[1],numero.vetor[2],numero.soma);
    
    return 0;
}