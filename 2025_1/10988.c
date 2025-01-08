#include <stdio.h>
#include <string.h>

int main(void) {
    char a[101], r_a[101];
    int k = 1;
    int cnt = 0;
    
    scanf("%s", a);

    while (a[cnt] != '\0'){
        cnt ++;
    }

    for (int i=0; i<=cnt/2; i++){
        if (a[i] != a[cnt-i-1]){
            k=0;
            break;
        }
    }





    // for (int i=0; i<=strlen(a)-1; i++) {
    //     if (a[i] != a[strlen(a)-1-i]) {
    //         k=0;
    //         break;
            
    //     }
    // }
    printf("%d", k);
    return 0;
}