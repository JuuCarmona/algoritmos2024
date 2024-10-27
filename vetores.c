#include <stdio.h>
#include <stdlib.h>

int main()
{
    // inicia o vetor
    int vetor[10];
    // inicia o indicie
     int i = 0;
     int x;
     int achou;
     // repete até ter 10 elementos
    while(i<10){    
        // escolhe um número aleatório (x)
        x = rand() % 1000;
        
        // sinaliza que não achou o x
        achou = 0;
        //percorre o vetor
        for(int y =0; y<i;y++){
            // o elemento atual é igual a x?achou o x?!
            if (vetor[i] == x){
                // sinaliza que achou o x
                achou = 1;
                //interrompe a busca
                break;
            }
        }
        // NÃO achou o x?
        if(achou==0){
             // coloca x no vetor 
             vetor[i] = x;
             printf("%d\n", x);
             //avança o índicie
             i = i + 1;
        }
    }
    
}
