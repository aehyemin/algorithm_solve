#include <stdio.h>

int main ( ) {
    int n=0;
    scanf("%d", &n);

    for(int i=0; i<2*n-1; i++) {
        for(int j=0; j<n-1; j++) {
            printf(" "); //공백개수 
        }
    }
}