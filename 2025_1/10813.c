#include <stdio.h>
// i번 바구니 j번 바구니 공을 교환
int main () {
    int n=0, m=0, i=0, j=0, k=0, a=0, b=0;
    scanf("%d %d", &n, &m);
    int basket[n];

    for (int i=0; i<n; i++) {
        basket[i] = i+1;
    }

    for (int j=0; j<m; j++) {
        int start, end;
        scanf("%d %d", &start, &end);

            a = basket[start-1];
            b = basket[end-1];
            basket[end-1] = a;
            basket[start-1] = b;

        }

    

    for (int k=0; k<n; k++) {
        printf("%d ", basket[k]);
    }
}