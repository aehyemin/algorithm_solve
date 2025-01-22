#include <stdio.h>
#include <string.h>

int main() {
    int t=0;
    char a[1000];
    scanf("%d", &t);

    for(int i=0; i<t; i++) {
        scanf("%s", a);
        printf("%c%c\n", a[0], a[strlen(a)-1]);
    }

}