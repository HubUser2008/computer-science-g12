#include <stdio.h>
#include <cs50.h>
// '\n' stands for "new line", which tells the computer to go to a new line. '\n' tells the computer to go to a new line after what's printed

int main(void) {
// An array is a list of multiple values. In this case, this is an array called "grades", with "grades" being the integer
// int grades[] = {77, 99, 87, 65};
    int wholeNums[] = {77, 99, 87, 65, 34};
    int size1 = sizeof(wholeNums); // The size of the entire array
    int size2 = sizeof(wholeNums[0]); // The size of the JUST THE FIRST NUMBER of the array
    // Print out '99' by using the index number that represents each other. The index number '1' represents the number '99' in the array
    printf("%i, %i\n", size1, size2);

    double realNums[]={77, 99, 87, 65};
    int size3 = sizeof(realNums);
    int size4 = sizeof(realNums[0]);
    printf("doubles: %i, %i\n", size3, size4);

    int lenArray = sizeof(realNums) / sizeof(realNums[0]);
    printf("The real nums array is %i units long\n", lenArray);

}
