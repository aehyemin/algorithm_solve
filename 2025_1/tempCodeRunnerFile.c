#include <stdio.h>

int main () {
    int num[30] = {0}, n;
    int ans[2];

    for(int i=0; i<28; i++) {
        scanf("%d", &n);
        num[n-1] = 1;
    }

    for(int j=0; j<30; j++) {
        if (num[j] == 0) {
            printf("%d\n", j+1);
        }
    }
}