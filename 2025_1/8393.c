#include <stdio.h>

int main () {
    int n=0, ans=0;
    scanf("%d", &n);

    for(int i=0; i<=n; i++) {
        ans += i;
    }
    printf("%d", ans);
    return 0;
}