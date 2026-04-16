#include <stdio.h>
#include <cs50.h>

int main(void) {

    int i = 0;
    int sum = 0;
    int remain = 0;

    while(i < 50) {
        i = i + 1;
        sum += i;
    if (i%3==0) {
        printf("fizz\n");
    }
    else if (i%5==0) {
        printf("buzz\n");
    }
    else if (i%15==0) {
        printf("FizzBuzz\n");
    }
    else {
        printf("%i\n", i);
    }
    }
}
