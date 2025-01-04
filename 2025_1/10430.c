#include <stdio.h>

int main(void) {
    char A, B, C;

    scanf("%s %s %s", &A, &B, &C);
    printf("%s\n%d\n%d\n%d\n ",(A+B)%C, ((A%C) + (B%C))%C, (A*B)%C,((A%C)*(B%C))%C );


}