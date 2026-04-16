#include <stdio.h>
#include <cs50.h>

int adder(int a, int b);

int main(void) {
    int x = get_int("Provide an integer ");
    int y = get_int("Provide an integer ");

    int sum = adder(x,y);
    printf("%d\n", sum);
}

int adder(int a, int b) {
    return a+b;
}
