#include <stdio.h>

int main() {
    //총금액x, 종류n, 물건가격 a와 개수b
    int a=0, b=0, x=0, n=0, ans=0;
    scanf("%d", &x);
    scanf("%d", &n);
    for(int i=0; i<n; i++) {
        scanf("%d %d", &a,&b);
        ans += a*b;
    }
    if (x == ans) {
        printf("Yes");
    } else {
        printf("No");
    }
}