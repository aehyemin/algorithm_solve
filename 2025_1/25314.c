#include <stdio.h>

int main () {
    int n=0;
    scanf("%d", &n);

    while (n>4) {
        printf("long ");
        n -= 4;
    }
    printf("long int");
}