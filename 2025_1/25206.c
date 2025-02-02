#include <stdio.h>

int main () {
    // 전공평점 = 학점 * 과목평점의 합을 / 학점의 총합
    char name[55];
    float grade;
    char al[3];
    for(int i=0; i<20; i++){
    scanf("%s %lf %s", name, &grade, al );
    printf("%s", name);
    }
}