#include <stdio.h>

int main ( ) {
    int n=0;
    scanf("%d", &n);

    for(int i=0; i<n; i++) {

        for(int j=0; j<n-i-1; j++) {
            printf(" "); //공백개수 
        }
        
        for(int k=0; k<2*i+1; k++) {
            printf("*");
        }

        // for(int j=0; j<n-1; j++) {
        //     printf(" "); //공백개수 
        // }
        printf("\n");
    }

    for(int i=0; i<n-1; i++) {

        for(int j=n; j>n-i-1; j--) {
            printf(" "); //공백개수 
        }

        for(int k=2*n-1; k>2*(i+1); k--) {
            printf("*");
        }

        // for(int j=0; j<n-1; j++) {
        //     printf(" "); //공백개수 
        // }
        printf("\n");
    }
}