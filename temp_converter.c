#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <ctype.h>

int main()
{
    char unit;
    float temp;
    
    printf("Are ya using \'F\' or \'C\', please type the Character then enter: ");
    scanf("%c",&unit);
    printf("Enter temperaure in %c: ", unit);
    scanf("%f", &temp);

    unit = toupper(unit);

    if(unit=='F'){
        temp = temp -32;
        temp = temp / (9/5);
        printf("That equals %.2f C", temp);
    }
    else if(unit=='C'){
        temp = temp * 9/5;
        temp = temp + 32;
        printf("That equals: %.2f F", temp);
    }
    return 0;
}