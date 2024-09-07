#include <stdio.h>

int main()
{
    int c = 0;
    float i = 0;
    int n;
    float v;

    for(int x = 0; x < 10;x++) {
        printf("digite um numero:");
        scanf("%d",&n);
        i = i + n;
        c = c + 1;
        v = i / c;
        printf("A media e:%.2f\n",v);
    }
} 