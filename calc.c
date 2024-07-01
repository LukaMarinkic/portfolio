#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <ctype.h>

int main()
{
    char opp;
    short operator;
    double num1;
    double num2;
    double result;

    // Get num1
    printf("First number: ");
    scanf("%lf", &num1);

    // Get Operator
    printf("\nOperator: ");
    scanf(" %c", &opp);
    if (opp == '+')
    {
        operator = 1;
    }
    else if (opp == '-')
    {
        operator = 2;
    }
    else if (opp == '*')
    {
        operator = 3;
    }
    else if (opp == '/')
    {
        operator = 4;
    }
    
    switch (operator)
    {
    case 1:
        printf("Num2 than enter: \n%.2lf ", num1);
        printf("%c ", opp);
        scanf("%lf", &num2);
        result = num1 + num2;
        printf("= %lf", result);
        break;
    
    case 2:
        printf("Num2 than enter: \n%.2lf ", num1);
        printf("%c ", opp);
        scanf("%lf", &num2);
        result = num1 - num2;
        printf("= %lf", result);
        break;
    
    case 3:
        printf("Num2 than enter: \n%.2lf ", num1);
        printf("%c ", opp);
        scanf("%lf", &num2);
        result = num1 * num2;
        printf("= %lf", result);
        break;
    
    case 4:
        printf("Num2 than enter: \n%.2lf ", num1);
        printf("%c ", opp);
        scanf("%lf", &num2);
        result = num1 / num2;
        printf("= %lf", result);
        break;
    
    default:
        printf("Invalid input!");
        break;
    }

    return 0;
}
