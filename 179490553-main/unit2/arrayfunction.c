#include <stdio.h>
#include <time.h>
#include <stdlib.h>

int randomArray(int size);

int randomArray(int size) {
    srand(time(NULL)); // Start at a different seed (so that you don't get the same random number each time, hence the use of "NULL")
    int newarray[size];

    for(int i = 0; i<size; i++) {
        newarray[i] = rand()%11;
        printf("%d ", newarray[i]);
    }
    return newarray;
}

int main(void) {
    int array1[20] = randomArray(20);
}
