#include <stdio.h>

char my_strcat(char *s1,char *s2){}


int main(){

    char s1[100]= "Ola voce esta errado" ,s2[100]="Mas nem tanto";
    char *sres;

    sres = my_strcat(s1,s2);


    return 0;
}

my_strcat(char *s1,char *s2){
    char sres[200] = ;
    int tamanho = strlen(s1);
    int add = strlen(s2);   
    for(int i= 0;i<tamanho-1;i++){
        if(i<(tamanho-1)){
            sres[i] = s1[i];
        }
    }
    return sres;
}