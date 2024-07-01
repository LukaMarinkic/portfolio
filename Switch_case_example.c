#include <stdio.h>
#include <stdlib.h>

int Switch_case_example(){
    char grade = 'B';

    switch (grade)
    {
    case 'A':
        printf("Little bit tryhardy!");
        break;
    
    case 'B':
        printf("W");
        break;

    case 'C':
        printf("Lil lazy");
        break;

    case 'D':
        printf("stupid!");
        break;
    case 'F':
        printf("Failure!");
        break;

    default:
        break;
    }

    

    return 0;
}