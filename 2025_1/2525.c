#include <stdio.h>

int main(void) {
    int a=0, b=0, c=0, goal=0, goal_m=0, hour=0;

    scanf("%d %d", &a, &b);
    scanf("%d", &c);

    goal = (a * 60 + b + c);
    goal = goal % (24 * 60);
  
    // 2일이면 2880분이다
    hour = goal / 60;
    goal_m = goal % 60;


    printf("%d %d\n", hour, goal_m);

    return 0;
}