#include "stdio.h"
#include "stdlib.h"


double FatorialInvetido(int quantidade){
    double Fatorial;

    if (1==quantidade) {
        return 1;
    }else{
        
        Fatorial = FatorialInvetido(quantidade-1)*quantidade;
        printf("%lf \n",Fatorial);
    }
    
    return Fatorial;

}


int main(){


    FatorialInvetido(8 );

    return 0;
}