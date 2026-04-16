#include <stdio.h>

int main(void) {

    int myNumbers[] = {478,23,731,498,31}; // Initial array

    myNumbers[1] = 210; // Changing an individual element of an array is possible using this sort of format
    myNumbers[4] = 99;

    int highest = myNumbers[0];
    int secondHighest;
    int indexHigh = 0;
    int indexSecond = 0;

    for(int i = 0; i<5; i++) {
        if(highest<myNumbers[i]){
            secondHighest = highest;
            indexSecond = indexHigh;
            highest = myNumbers[i];
            indexHigh = i;
        }
    else if(secondHighest<myNumbers[i] && myNumbers[i]!=highest){
        secondHighest = myNumbers[i];
        indexSecond = i;
    }

    }
    printf("%i is the second highest number in the array\n", myNumbers[indexSecond]);

/*
    for (int i = 0; i<5; i++) {
        if(lowest>myNumbers[i]) {
            index = i; // Save the index when a new lowest number in the array is found
        }
        else if (secondHighest<myNumbers[i])  {
            index2 = i;
        }
    }
    printf("%d is the lowest number in the array\n", myNumbers[index]);
    printf("%d is the second highest number in the array\n", myNumbers[index2]);


    for(int i = 0; i<5; i++) {
        printf("%i, ", myNumbers[i]);
    }
}
*/
}
