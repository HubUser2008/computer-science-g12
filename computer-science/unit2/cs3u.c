#include <stdio.h> // Includes the standard input-output library, allowing the usage of functions like 'printf()' and 'scanf()'
#include <stdlib.h> // Includes the standard library, which provides functions for memory allocation, random number generation, and other
// utilities such as 'rand()' and 'srand()'
#include <time.h> // Includes the time library, allowing the usage of time-related functions, particularly for the usage of the random number
// generator
#include <string.h> // Includes the string library, which provides functions for manipulating C strings (although, it's not used in this code)
#include "cs3u.h" // Includes the local library of the function declarations that I personally made, which is called 'cs3u.h', which is a header
// file

int randomArray(int array[], int size, int min, int max) { // 'int randomArray' is a function definition for generating a random array. It takes
// an array, its size, and the minimum and maximum values for the random numbers that will be generated in the array
    srand(time(NULL)); // Seeds the random number generator using the current time, ensuring that you get different random numbers each time you
    // run the program
    for(int i=0; i<size; i++) { // A loop that goes through each index of the array
        array[i]=min+rand()%(max-min+1); // Assigns a random number to each element in the array. The expression generates a random number between
        // the minimum and maximum values of the array
    }
}

int findHighest(int array[], int size) { // 'int findHighest' is a function definition that finds and returns the highest value in the array
    int highest = array[0]; // Initializes the highest value of the array with the first element of the array
    for (int i = 1; i < size; i++) { // Loops through the array starting from the second element of the array
        if (array[i] > highest) { // Checks if the current element is greater than the current highest
            highest = array[i]; // Updates the 'highest' (which is the integer with the largest numerical value in the array) if a larger value
            // is found
        }
    }
    return highest; // Returns the highest value that is found within the array, meaning that it shows the highest value of the array. 'Return'
    // is used to show the user what the function did and to tell the C program that this function is completed
}

int findLowest(int array[], int size) { // 'int findLowest' is a function definition that finds and returns the lowest value of the array
    int lowest = array[0]; // Initializes the 'lowest' with the first element of the array
    for (int i = 1; i < size; i++) { // Loops through the array starting from the second element of the array
        if (array[i] < lowest) { // Checks if the current element is less than the current lowest element of the array
            lowest = array[i]; // Updates the 'lowest' value of the array if a smaller value is found
        }
    }
    return lowest; // Returns the lowest value that is found within the array
}


int printArr(int array[], int size){ // 'int printArr' is a function definition that prints the elements of the array which are the integers of
// the array
    printf("my array: "); // prints "my array" before showing the content of the array, which are the integers within the array
    for(int i=0;i<size;i++){ // Loops through each element of the array
        printf("%d ", array[i]); // Prints each element followed by a space for orginizational purposes (to make the array look cleaner)
    }
    printf("\n"); // Moves to the next line after printing the array
}

int bubbleSort(int array[], int size){

    return 0;
}

int findAvg(int array[], int size){ // 'int findAvg' is a function definition that calculates and returns the average of the array elements
    int sum=0; // Initializes a variable, recognized as 'sum', to calculate and determine the total of all the integers in the array
    for(int i=0; i<size; i++){ // Loops  through each element of the array
        sum += array[i]; // Adds each element of the array to the total numerical value of all the integers in the array added together, which
        // is recognized as the variable, 'sum'
    }
    return (sum/size); // Returns the average by dividing the sum by the number of elements in the array
}

int findMedian(int array[], int size) { // 'int findMedian' is a function definition that calculates and returns the median of the array. The
// 'median' of the array will be the middle number because median = the middle number
    if (size % 2 == 0) { // Checks if the number of elements within the array is even
        return (array[size / 2 - 1] + array[size / 2]) / 2.0; // For even sized arrays, it returns the average of the 2 middle numbers
    }
    else {
        return array[size / 2]; // Returns the median for arrays with an odd number of integers within the array (elements)
    }
}

int findMode(int array[], int size) { // 'int findMode' is a function definition that finds the mode of an array. A 'mode' is the most occurring
// number (e.g. [7, 9, 7, 8] -> 7 is the mode of this array because it's the integer that shows up the most within this array)
    int maxCount = 0, mode = array[0]; // Initializes the 'maxCount' (the number of times each integer shows up within the array) to track the
    // number with the highest occurrence and 'mode' is used to store the mode's numerical value (the integer that is the mode) which is
    // represented by the numerical value of the integer that corresponds with whatever the integer's index number in the array is
    for (int i = 0; i < size; i++) { // Goes through each element of the array
        int count = 0; // Initializes count as index number 0, so that each integer is accounted for as 'count'
        for (int j = 0; j < size; j++) { // Goes through the entire array again, using index 'j' to count the occurrences of each integer of the
        // array
            if (array[j] == array[i]) { // Checks if the current element in the inner 'for' loop (array[j]) is equal to the current element of the
            // array in the outer 'for' loop (array[i])
                count++; // Increases the 'count' variable by 1 each time a match is found, with the 'match' being if array[j] and array[i] are
                // the same which effectively counts how many times each integer of the array appears within the array
            }
        }
        if (count > maxCount) { // After counting occurrences of each element (integer) of the array, this conditional statement checks if the
        // current count exceeds the previous highest count represented as 'maxCount'
            maxCount = count; // If the condition is true, it updates the 'maxCount' to the current 'count'
            mode = array[i]; // If the condition is true, it also updates the mode to the current element which is represented as 'array[i]' since
            // 'array[i]' represents each element of the array, with 1 specific element of the array being the most frequently occurring element
            // of the array
        }
    }
    return mode; // Returns the mode of the array that's found
}

int addOne(int array[], int size) { // 'int addOne' is a function declaration that increases each element (integer) of the array by 1
    for(int i = 0; i<size; i++) { // Loops through each element of the array
        array[i]+=1; // Increases the value of THE SPECIFIC INDEX NUMBER OF MY CHOOSING by 1
    }
}

int insertionSort(int array[], int size) { // 'int insertionSort' is a function definition that implements the insertion sort method to sort the
// array from the lowest numerical values to the highest numerical values
    for (int i = 1; i < size; i++) { // Starts from the 2nd element (index 1), since the first element is already sorted, according to the
    // insertion sort method (insertion sort, sorts elements by checking to the left of them to see whether the elements need to be switched
    // with each other or not, but because the first index number doesn't have any number to the left of it, it's already marked as sorted,
    // therefore making us have to start at the 2nd element of the array, which is recognized as index number 1 since index numbers of an array
    // start from 0)
        int key = array[i]; // Stores the current element in order to be positioned correctly in the sorted part of the array
        int j = i - 1; // Initializes 'j' to point to the last element of the sorted part
        while (j >= 0 && array[j] > key) { // Shifts elements that are greater than 'key' to the right
            array[j + 1] = array[j]; // Moves the current element to the right
            j--; // Decreases 'j' to continue checking the previous elements
        }
        array[j + 1] = key; // Inserts 'key' into its correct position once the right spot in the array has been found and implemented onto the
        // integer of the array. 'key' represents the every element of the array while representing 1 element of the array at a time, which in
        // this case, is correctly sorted using the insertion sort method through C programming language code
}
}

int flipHorizontally(char art[][20], int rows) { // This line is the function definition for flipping the ASCII ART HORIZONTALLY. It has 2
// parameters: 'char art[][20]' and 'int rows.' 'char art[][20]' is a 2D array of characters that represents the ASCII art (since each row will
// be AT MOST, 20 characters long, causing there to be no errors when the C program tries compiling the code. The '20' could be less, but to make
// sure that no errors happen when I run the code, I just put it as 20 since my ASCII ART will definitely not have a row of up to 20 characters
// or more). 'int rows' is referring to the number of rows in the ASCII ART
    for (int i = 0; i < rows; i++) { // This for loop iterates (passes) through each row of the ASCII ART. The variable, 'i' represents the
    // specific row that is currently being processed, WHICH ALL OF THEM ARE GOING TO BE PROCESSED ONE BY ONE UNTIL ALL HAVE BEEN PROCESSED
        int len = strlen(art[i]); // Calculates the length of the current row which is represented with 'art[i]', using the 'strlen()' function
        // and stores it in the variable 'len'. It's necessary to know the length of each row in order to correctly horizontally flip each
        // character of each row of the ASCII ART.
        for (int j = 0; j < len / 2; j++) { // This nested for loop (a loop within another loop is a 'nested' loop) swaps characters in each row to
        // flip the row horizontally. The loop runs from the start of the row 'j = 0' to the middle of the row 'len / 2' (len represents the
        // entire row as defined earlier in the 1st 'for' loop, and if you divide len by 2, you get half of len, which is the middle of the entire
        // row). It swaps characters at position 'j' with the corresponding character from the other end of the row 'len - j - 1' (the entire row
        // minus j minus 1). 'j' represents each character of the array
            char temp = art[i][j]; // temporarily stores the character at whatever the character's position in the current row of the ASCII ART
            // array, which is represented as 'j'
            art[i][j] = art[i][len - j - 1]; // this line assigns the character from the opposite end of the row 'len - j - 1' to the current
            // position of the character in the ASCII ART row which is represented by 'j'
            art[i][len - j - 1] = temp; // This line places the character stored in 'temp' (original character from j) in the opposite position,
            // which effectively swaps the 2 characters
        }
    }
}

int flipVertically(char art[][20], int rows) { // This line is the function definition for VERTICALLY FLIPPING THE ORIGINAL ASCII ART. It also
// has 2 parameters: 'char art[][20]' and 'int rows.' 'char art[][20] is a 2D array that represents the ASCII ART while 'int rows' is the number
// of rows in the ASCII ART
    for (int i = 0; i < rows / 2; i++) { // This for loop iterates (passes) from the top row of the original ASCII art 'i = 0' (i = 0 represents
    // the 1st row of the ASCII ART, which is stored as index 0) to the middle row (rows / 2. 'rows' represents
    // every row of the original ASCII ART, and when that's divided by 2, that equals half of the rows of the original ASCII ART array, which is
    // just the middle). It swaps rows from the top half of the art with the corresponding rows from the bottom half to flip the image vertically
        char temp[20]; // This line creates a temporary array 'temp' to hold one row of the ASCII art while the others row are being swapped
        strcpy(temp, art[i]); // This copies the contents of the current row 'art[i]' into the temporary array 'temp'
        strcpy(art[i], art[rows - i - 1]); // This copies the row from the opposite side of the art 'art[rows - i - 1]' into the current row:
        // 'art[i]', which effectively moves from the bottom row to the top row
        strcpy(art[rows - i - 1], temp); // This copies the contents of the temporary array 'temp' ('temp' holds the original top row) into the
        // bottom row, completing the swap of the 2 rows
    }
}
