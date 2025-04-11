#include <stdio.h>


int main(){
    int vetor[5] = {5,2,3,6,5};
    int anterior ;
    
    for (int i = 0; i < 4; i++){
        for(int j = 0; j <4;j++){
            if(vetor[i]<vetor[j]){
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
