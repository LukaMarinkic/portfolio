#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int Pytha(){
    double Kath1;
    double Kath2;
    double Hypo;

    printf("This programm calculates the hypotenuse of a right triangle\nFirst Kathe: ");
    scanf("%lf", &Kath1);
    printf("\nSecond Kath: ");
    scanf("%lf", &Kath2);

    Hypo = sqrt(pow(Kath1,2)+ pow(Kath2,2));
    printf("\nHypotenuse: %lf", Hypo);

    return 0;
}
