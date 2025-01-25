#include <stdio.h>
#include <string.h>
int main () {
    char a[15];
    int time = 0;
    scanf("%s", a);

    for(int i=0; a[i]!='\0'; i++) {
        if (a[i] >='A'  && a[i]<='Z') {
            time += (a[i] - 'A')/3 + 3;
            if (a[i] == 'S' || a[i] == 'X' || a[i] == 'Y' || a[i] == 'Z') {
                time -= 1;
            }
        }
    }
    printf("%d\n", time);
}