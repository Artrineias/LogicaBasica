#include <stdio.h>

int len(char string[]){
    int i = 0;
    while(string[i]!='\0'){
        i++;
    }
    return i;
}

void escrita(int i,char resultado[],char base[]){
    int j = 0;
    while (base[j]!='\0') {
        resultado[i] = base[j];
        j++;
        i++;
    }
    resultado[i] = '\0';
}

void my_strcat(char resultado[],char add[],char inicial[]){
    escrita(0,resultado,inicial);
    escrita(len(inicial), resultado, add);
    
}





int main(){

    char s1[100]= "Ola eu posso esta errado,";
    char s2[100]= "mas to tentando viver.";
    char sres[200];
    my_strcat(sres,s2,s1);
    printf("%s\n",sres);


    return 0;
}

