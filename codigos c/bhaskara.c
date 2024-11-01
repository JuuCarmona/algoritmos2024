
#include <stdio.h>
#include <math.h>

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

    float r1;
    float r2;
    printf("digite o valor de A:");
    scanf("%f",&A);
    printf("digite o valor de B:");
    scanf("%f",&B);
    printf("digite o valor de C:");
    scanf("%f",&C);
    
     Delta = B * B - 4*A*C;
// Se o delta for menor que 0 não tem raiz
    if (Delta < 0){
        printf("Não possui raíz.");
    }
// Se o delta for igual a 0 possui uma raiz.
    else if(Delta == 0){
        r1 = - B / 2*A;
        printf("%f",r1);
    }
// Se o delta for maior que 0 possui duas raizes.
    else{
        r1 = (- B + sqrt(Delta))/(2*A);
        r2 = (- B - sqrt(Delta))/(2*A);
        printf("%.2f \n %.2f",r1, r2 );
    }
}
