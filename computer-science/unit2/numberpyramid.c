#include <stdio.h>
#include <cs50.h>

int main(void) {
    int x;
    do {
        printf("Enter an integer between 3 and 20: ");
        scanf("%d", &x);
    } while(x < 3 || x > 20);

    int array[x];

    for (int i = 0; i < x; i++) {
        array[i] = i + 1;
    }
    printf("Final array: ");
    for (int i = 0; i < x; i++) {
        printf("%d ", array[i]);
    }

    return 0;
}
