#include <stdio.h>
void meow(int n); // Pre-defining this 'meow' function. This line of code is not needed but it is something that could be done ahead of time
// to make the coding program understand that this function will be used later on in the code
// this line of code is sort of like a prototype, where you're telling the code program that you're going to use this function later in your
// code but it's going to be

int main(void) {
    meow(10); // The number in the brackets must have an integer input since "meow" has to have 1 input for each meow
}

void meow(int n){
    int i = 0;
    n = 10;
    while(i < n){
    i++;
    printf("meow\n");
    }

}
