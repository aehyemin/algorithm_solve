#include <stdio.h>

int main(void) {
    int t=0, a=0, b=0;

    scanf("%d", &t);
    for(int i=0; i<t; i++) {
        scanf("%d %d", &a,&b);
        printf("%d\n", a+b);
    }

}