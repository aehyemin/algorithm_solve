#include <stdio.h>

int main () {
    int n=0, m=0,k=0,l=0;
    scanf("%d %d", &n, &m);
    int basket[n];

    for(int i=1; i<n+1; i++) {
        basket[i] = i;
    }

    for(int j=1; j<m+1; j++) {
        scanf("%d %d", &k, &l);
        for (int h=)
        int tmp = basket[k];
        basket[k] = basket[l];
        basket[l] = tmp;
        l--;
    }

    for(int o=0; o<n; o++) {
        printf("%d", basket[o]);
    }
}