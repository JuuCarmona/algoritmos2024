#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int main()
{
// Peça o valor de A.
    float A;
// Peça o valor de B.
    float B;
// Peça o valor de C.
    float C;
// Ache o valor de delta.
    float Delta;

    float i;
    float r;
    float X;
    printf("digite o valor de A:");
    scanf("%f",&A);
    printf("digite o valor de B:");
    scanf("%f",&B);
    printf("digite o valor de C:");
    scanf("%f",&C);

     // inicia contador com 0
     i = 0;
    // repete
    while (i < 100000){
         // sorteia x
        X = rand() % 100;
        printf("%.2f ",X);
        // incrementa o contador
        i = i + 1;
        // calcula a * x*x +b *x+c 
        r = A* X*X + B *X +C;
        // se o resultado for 0
        if(r == 0){
           // mostre o x 
           printf("================ %f\n",X);
           // sai do loop
           break;
        }
    }
}
