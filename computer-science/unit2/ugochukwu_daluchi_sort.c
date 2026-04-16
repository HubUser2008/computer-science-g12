#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <cs50.h>
#include "cs3u.h"

int main(void) {
    int arrSize = 50;
    int myArr[arrSize];
    randomArray(myArr, arrSize, 0, 100);
    printArr(myArr, arrSize);

    int lowest=findLowest(myArr, arrSize);
    int highest=findHighest(myArr, arrSize);
    printf("The lowest value of the array is: %d\n", lowest);

    int newArrSize = 0;
    for (int i = 0; i < arrSize; i++) {
        if (myArr[i] != lowest) {
            myArr[newArrSize++] = myArr[i];
        }
    }
    printf("\nThe array after removing the lowest value/s from the original array:\n");
    printArr(myArr, newArrSize);

    int randomNumber = rand() % (highest - lowest + 1) + lowest;
    myArr[2] += randomNumber;

    printf("\nThe random number added to the 2nd index of the array: %d\n", randomNumber);

    printf("\nThe array after adding the random number to the 3rd index of the array:\n");
    printArr(myArr, arrSize);

    int sortArray=insertionSort(myArr, arrSize); // Sorts the array using insertion sort
    printf("\nSorted version of the array from lowest to highest, using insertion sort method:\n");
    printArr(myArr, arrSize);

    int mean=findAvg(myArr, arrSize);
    printf("The mean of the array is: %d\n", mean);

    int median=findMedian(myArr, arrSize);
    printf("The median of the array is: %d\n", median);

    int mostOccurringNumber=findMode(myArr, arrSize);
    printf("The mode of the array is %d\n", mostOccurringNumber);

    return 0;
}
