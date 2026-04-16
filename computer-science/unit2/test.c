#include <stdio.h>
#include "cs3u.h"

int main(void) {
    int arrSize;
    printf("Please enter an integer number of array elements you would like: \n");
    scanf("%d",&arrSize);
    int myArr[arrSize];

    randomArray(myArr, arrSize,0,100);
    int highest=findHighest(myArr, arrSize);

    int lowest=findLowest(myArr, arrSize);

    printArr(myArr, arrSize);
    int average=findAvg(myArr, arrSize);{
    printf("The average of the array is %d\n", average);

    printf("highest=%d\nlowest=%d\n", highest, lowest);
    return 0;

    addOne(myArr, arrSize);
    printArr(myArr, arrSize);
    return 0;
    }
}
