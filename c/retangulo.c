#include <stdio.h>
// para desenhar o retangulo
void retangulo(int altura, int largura) {
    for (int i = 0; i < altura; i++) {
        for (int j = 0; j < largura; j++) {
            if (i == 0 || i == altura - 1) {
                if (j == 0 || j == largura - 1) {
                    printf("+");
                } else {
                    printf("-");
                }
            } else {
                if (j == 0 || j == largura - 1) {
                    printf("|");
                } else {
                    printf(" ");
                }
            }
        }
        printf("\n");
    }
}

int main() {
    int altura, largura;
    // peça a altura e largura
    printf("Digite a altura do retângulo: ");
    scanf("%d", &altura);
    printf("Digite a largura do retângulo: ");
    scanf("%d", &largura);
    // mostra o retangulo
    retangulo(altura, largura);

    return 0;
}
