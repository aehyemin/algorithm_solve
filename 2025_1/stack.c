#include <stdio.h>

#define MAX_SIZE 100

typedef int element;

typedef struct {
    element data[MAX_SIZE];
    int top;
} Stack;


void init(Stack *stk) {
    stk->top = -1;
}

void push(Stack *stk, element value){
    if (stk->top == MAX_SIZE -1) {
        printf("stack is full\n");
    } else {
        stk->data[++(stk->top)] = value;
    }
}

void pop(Stack *stk, element *value){
    if (stk->top == -1) {
        printf("stack is empty\n");
    } else {
        *value = stk->data[(stk->top)--];
    }
}


void isEmpty (Stack *stk) {
    if (stk->top == -1) {
        printf("stack is empty\n");
    }
}

void isFull (Stack *stk) {
    if (stk->top == MAX_SIZE -1) {
        printf("stack is full\n");
    }
}


void display(Stack *stk) {
    if (stk->top == -1) {
        printf("stack is empty\n");
    } 
    for (int i=0; i<=stk->top; i++) {
        printf("%d", stk->data[i]);
    }
    printf("\n");
}