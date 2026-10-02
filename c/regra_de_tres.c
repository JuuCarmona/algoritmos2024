#include <stdio.h>

float regra_de_tres(float a, float b, float c) {
    if (a == 0) {
        printf("O valor de 'a' não pode ser zero.\n");
        return 0;
    }
    return (b * c) / a;
}

int main() {
    float a, b, c, d;

    printf("Digite o valor de a: ");
    scanf("%f", &a);
    printf("Digite o valor de b: ");
    scanf("%f", &b);
    printf("Digite o valor de c: ");
    scanf("%f", &c);

    d = regra_de_tres(a, b, c);

    if (a != 0) {
        printf("O valor de d é: %.2f\n", d);
    }

    return 0;
}
