#include "stdio.h"

int len(char palavra[]){
    int tamanho = 0;

    while (palavra[tamanho]!='\0') {
        tamanho++;
    }
    
    return tamanho;
}

int main(){

    char *p1,*p2,*completa;
    int tamanho;
    
    printf("Digite uma frase:");
    scanf("%s",p1);
    printf("Digite uma frase:");
    scanf("%s",p2);

    tamanho = len(p2)+len(p1);

    return 0;
}

