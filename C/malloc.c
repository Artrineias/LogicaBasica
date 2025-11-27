#include "stdlib.h"
#include "stdio.h"

int main(){
    int *p,i;

    p = malloc(100*sizeof(int));

    for(i=0;i<100;i++){
        p[i]= i;
    }


    for(i=0;i<100;i++){
        printf("%d\n",p[i]);
    }
    free(p);

    return 0;
}