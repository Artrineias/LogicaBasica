#include <stdio.h>
#include <string.h>

void my_strcat(char resultado[],char add[]){
    strcat(resultado,add);
}


int main(){

    char s1[100]= "Ola eu posso esta errado,";
    char s2[100]= "mas to tentando viver.\n";
    my_strcat(s1,s2);
    printf("%s",s1);


    return 0;
}

