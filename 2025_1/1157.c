#include <stdio.h>
#include <ctype.h>
int main ( ) {
    char a[1000000];
    scanf("%s", a);
    int al[26] = {0};
    char max;
    for(int i=0; a[i]!='\0'; i++) {
        char ch = toupper(a[i]);
        al[ch - 'A']++;
    }
    int cnt = 0, num = -1;
    int check =0;
    for (int j=0; j<26; j++) {
        if (al[j] > cnt) {
            cnt = al[j];
            num = j;
            check = 0;
        } else if (al[j] == cnt) {
            check = 1;
        }
    }

    if (check) {
        printf("?\n");
    } else {
        printf("%c\n", num + 'A');
    }

    //대문자로 출력력
}