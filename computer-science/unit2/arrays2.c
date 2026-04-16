#include <stdio.h>

int main(void) {

    int myNums[10] = {2,3,4,5,77};
    // printf("%i\n", myNums[3])
    int totalMem = sizeof(myNums);
    int elemMem = sizeof(myNums[0]);
    int numberofthings = totalMem/elemMem;
    // printf("%i\n", numberofthings);

    int i = 0;

    while(i<numberofthings){
        if (i<(numberofthings - 1)){
            printf("%i,", myNums[i]);
        }
        else {
            printf("%i\n", myNums[i]);
        }
        i = i + 1;
    }
}
