#include <stdio.h>
// i번 바구니부터 j번 바구니까지 k번 번호가 적혀져 있는 공을 넣는다
int main () {
    int n=0, m=0, i=0, j=0, k=0;
    scanf("%d %d", &n, &m);
    int basket[n];

    for (int i=0; i<n; i++) {
        basket[i] = 0;
    }

    for (int i=0; i<m; i++) {
        int start, end, ball;
        scanf("%d %d %d", &start, &end, &ball);

         for (int j = start -1; j<end; j++){
            basket[j] = ball;
        }
    }

    for (int k=0; k<n; k++) {
        printf("%d ", basket[k]);
    }
}