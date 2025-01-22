#include <stdio.h>

int main () {
    int n=0, max=0;
    scanf("%d", &n);
    int score[n];
    float avg=0;

    for (int i=0; i<n; i++) {
        scanf("%d", &score[i]);
        if (max < score[i]) {
            max = score[i];
        }
    }

    for(int j=0; j<n; j++) {
        avg += ((float)score[j]/max)*100;
    }

    printf("%f\n", avg/n);


}