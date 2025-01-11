#include <stdio.h>

int main (void) {
    int x, y;
    scanf("%d", &x);
    scanf("%d", &y);

    // 1
    if ( 0 < x &&  y > 0) {
        printf("1\n");
    }
    // 2
    else if ( 0 > x &&  y > 0) {
        printf("2\n");
    }
    // 3
    else if ( 0 > x &&  y < 0) {
        printf("3\n");
    }
    else {
        printf("4\n");
    }
    // 4


    return 0;
}