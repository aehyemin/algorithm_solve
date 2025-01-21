#include <stdio.h>

int main() {
    int a=0,b=0,n=0, ans=0;
    int num[10];

    for(int i=0; i<10; i++)  {
        scanf("%d", &n);
        num[i] = n%42;
    }
   
    

    for(int j=0; j<10; j++) {
        int cnt = 0;
    
        for(int k=0; k<j; k++) {
            if (num[j] == num[k])  {
                cnt ++;
            }
        }
        if (cnt == 0) {
            ans++;
        }
    
    }
    printf("%d\n", ans);
}