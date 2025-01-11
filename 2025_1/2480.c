#include <stdio.h>
#define MAX(x,y) ((x) > (y) ? (x):(y))
int main(void) {
    int a=0, b=0, c=0, money=0, max = 0;
    scanf("%d %d %d", &a,&b,&c);

    if (a == b && b== c && a==c)  {
        money = 10000 + a*1000;
    } else if (a == b) {
        money = 1000 + a*100;
    } else if (a==c) {
        money = 1000 + a*100;
    } else if (b==c) {
        money = 1000 + b*100;
    } else if (a!=b || b!=c || a!=c) {
        max = MAX(a,b);
        max = MAX(c,max);
        money = max*100;
    }
    
    printf("%d\n", money);

}