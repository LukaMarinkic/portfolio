#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int fibbo(){

    short i = 0;
    short int k = 0;
    short int j = 0;
    short l = 0;
    while(l<=10000){

        printf("\nfib(%d)= ",i);
        printf("%d",l);

        if (j==0){
            l = 1;
        }
        else{
            l = k + j;
        }

        k = j;
        j = l;
        i ++;

    }

    return 0;
}