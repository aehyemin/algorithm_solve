#include <stdio.h>

int main () {
    int n=0, v=0, num=0;
    int a[101];

    scanf("%d", &n);
    for(int i=0; i<n; i++) {
        scanf("%d", &a[i]);
    }

    scanf("%d", &v);
    
    for(int j=0; j<n; j++) {
        if (a[j] == v) {
            num += 1;
        }
    }

    printf("%d", num);
}