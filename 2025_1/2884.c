#include <stdio.h>

int main(void) {
    int h,m, total, goal, goal_two;

    scanf("%d %d", &h, &m);
   
    
    total = h * 60 + m-45;
    if (total < 0) {
        total = 24 * 60 + m- 45;
    }
    goal = total / 60;
    goal_two = total % 60;

    printf("%d %d\n", goal, goal_two);
    return 0;

}