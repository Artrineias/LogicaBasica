#include <stdio.h>


int main(){
    int vetor[5] = {1,5,4,7,3};
    int anterior ;
    
    for (int i = 0; i < 5; i++){
        for(int j = 0; j <5;j++){
            if(vetor[i]>vetor[j]){
                anterior = vetor[j];
                vetor[j] = vetor[i];
                vetor[i] = anterior;
                
            }
            
        }
    }

    for(int i = 0;i<5;i++){
        printf("%d",vetor[i]);
    }
}
