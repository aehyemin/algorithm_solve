#include <stdio.h>

int main () {
    int n=0, m=0,k=0,l=0;
    scanf("%d %d", &n, &m);
    int basket[n];

    for(int i=0; i<n; i++) {
        basket[i] = i+1;
    }

    for(int j=0; j<m; j++) {
        scanf("%d %d", &k, &l);
        k--;
        l--;
        while (k<l) {
            int tmp = basket[k];
            basket[k] = basket[l];
            basket[l] = tmp;
            k++;
            l--;
        }
        
    }

    for(int o=0; o<n; o++) {
        printf("%d ", basket[o]);
    }
}