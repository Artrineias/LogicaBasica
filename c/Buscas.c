#include <stdio.h>
int lista[10] = {1,2,3,3,2,1,5,6,7,4};
int posicoes[10];

int ordenacao(){
    int aux = 0;
    for(int i = 0; i < 10; i++){
        for(int j = 0; j < 10; j++){
            if(lista[i]<lista[j]){
                aux = lista[j];
                lista[j] = lista[i];
                lista[i] = aux;
            }
        }
    }
    for(int i = 0;i<10;i++){
        printf("%d",lista[i]);
    }
}

int buscabinaria(){

}

int sequencial(){

}


int main(){

    ordenacao();


    return 0;
}