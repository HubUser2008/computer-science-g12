#include <stdio.h>
#include <cs50.h>
#include <math.h>

int main (void){

    int x, y;
    x = get_int("provide an integer: ");
    y = get_int("provide an integer: ");

    if(x < y) {
        printf("y is bigger than x\n");
    }
    else if (x > y) {
        printf("x is bigger than y\n");
    }
    else {
        printf("x is equal to y\n");
    }

    int remain;
    remain = 0;
    remain = remain + x && y % 2;

    if (x && y==0) {
        printf("x and y are both even\n");
    }
    else if (x && y<0) {
        printf("x and y are either even or odd, but neither one of them are both even and odd\n");
    }
    else {
        printf("x and y are both odd\n");
    }


/*
    int x = get_int("please provide an integer: ");
    int y = get_int("please provide an integer: ");

    if(x+y>90) {
        printf("wow, what a big number!\n");
    }
    else if (x+y==69) {
        printf("AMAZING that the first number whose square and cube has all singular digits from 1-9\n");
    }
    else {
        printf("that's a terrible number. Try again >:(\n");
    }
*/
/*
    int counter = 0;

    counter = counter + 1;
    counter++;
    counter+=1;

    if(counter<4){
        printf("counter is less than 4\n");
            }
*/
}

