#include <stdio.h>

int main() {
    int n=0, min, max;
    scanf("%d", &n);
    int arr[n];


    for(int j=0; j<n; j++) {
        scanf("%d", &arr[j]);
    }

    min = arr[0];
    max = arr[0];
    for(int i=0; i<n; i++) {
        if (max < arr[i]) {
            max = arr[i];
        }

        if (min > arr[i]) {
            min = arr[i];
        }
    }

    printf("%d %d", min, max);
    
}