// This entire file "cs3u.h" is a header file which is used to declare functions that each perform different actions, so therefore, 'cs3u.h' is a
// header file that declares functions, with each function declaration performing different actions

#ifndef CS_3U_H // These 2 lines implement a header guard, which is a common practice in C programming, in order to prevent multiple inclusions
// of the same header file
// Checks if the macro, CS_3U_H has not been defined yet
#define CS_3U_H // If CS_3U_H is not defined, this line defines it. Now, if this file is included elsewhere, it won't be processed multiple
// times. This prevents errors from happening since it DOESN'T CARRY OUT MULTIPLE DECLARATIONS of functions or variables.

// Below, there are several function declarations listed. These tell the compiler about the existence of these functions, but the actual
// code that prints out return values for each function would be in the corresponding '.c' file in relation to this header file, which in this case
// is "cs3u.c"

int randomArray(int array[], int size, int min, int max); // Generates an array of random integers. 'int array[]' is the array to store the random
// numbers. 'int size' is the size of the array. 'int min' is the minimum numerical value of the random integers in the array. 'int max' is the
// maximum numerical value of the random integers in the array

int findHighest(int array[], int size); // Finds the highest value in an array. 'int array[]' is the specific array that will be evaluated to
// find the largest number in the array. 'int size' is the number of elements in the array. The intended return value for this function would be
// the highest value of the array. A return value is the output that a function gives after processing inputs

int findLowest(int array[], int size); // Finds the lowest value in an array. The intended return value of this function would be the display of
// the integer with the lowest numerical value of the array

int printArr(int array[], int size); // Prints out an array (prints out all the integers of an array). The intended return value of this function
// would be printing out the array in the terminal, showing the numerical content (all the integers) of the array

int bubbleSort(int array[], int size); // Sorts the array using the bubble sort algorithm. The intended return value of this function would be
// properly sorting the numbers of the array using the bubblesort method, from least to greatest

int findAvg(int array[], int size); // Calculates the average of all the values in the array. The intended return value of this function would be
// displaying the average value of the array as an integer (since it's as an integer, the average won't be a decimal, so the program will round
// the average to the nearest whole number)

int addOne(int array[], int size); // Adds 1 to each element (integer) of the array. The intended return value of this function would be each
// integer of the original array being increased by 1

int insertionSort(int array[], int size); // Sorts the array from lowest to highest, using the insertion sort method. The intended
// return value of this function is the array being sorted from the lowest numerical value to the highest numerical value

int findMedian(int array[], int size); // Finds the median (the integer in the middle) of the array. The intended return value of this
// function is the determination of the middle number (median) of the array

int findMode(int array[], int size); // Finds the mode (the most occurring integer) of the array. The intended return value of this
// function declaration is to determine the most occurring number (mode) of the array

int flipHorizontally(char art[][20], int rows); // Function declaration that HORIZONTALLY flips the original ascii art. 'char art[][20]' is
// referring to a 2D array of characters (not numbers in this case, because THIS IS ASCII ART AND NOT A NORMAL ARRAY OF INTEGERS) that
// represents the ASCII ART (the '[20]' represents the most amount of characters each row of the ASCII ART will have. I just decided to make it
// 20 just to make sure that the ASCII art won't result in an error since my ASCII ART will most definitely not be 20 characters long). 'int rows'
// represents the number of rows that the ASCII ART will have. The intended return value of this ASCII ART funtion declaration is for the
// original ASCII ART array which is provided at the beginning of 'ugochukwu_daluchi_asciiart' to be HORIZONTALLY FLIPPED

int flipVertically(char art[][20], int rows); // Function declaration that VERTICALLY flips the original ascii art. The intended return value
// of this ASCII ART function declaration is for the original ASCII ART array which is provided at the beginning of 'ugochukwu_daluchi_asciiart'
// to be VERTICALLY FLIPPED

#endif // This closes the '#ifndef' directive from the beginning, which marks the end of the header guard. This line of code ensures that the
// file isn't processed multiple times during compilation.

// Overall, this is a header file (identified as '.h') that declares various functions which are used for manipulating and analyzing arrays
// (such as generating random integers of an array, finding the highest/lowest integer of the array, sorting the array using bubble sort, etc...)
// Header guards prevent multiple inclusions of the same thing/s. This header file used for function declaration provides function prototypes
// so that other source files can use these functions once implemented into them, without having to type the specified code to perform an action/s
// for each function, since they'll already be typed and specified in 'cs3u.c.' This entire thing is a header file that contains a header guard.
// The header guards in this header file are '#ifndef', '#define', and #'endif'

// Header guards are constructs within a header file that are designed to prevent multiple inclusions of the same file
// A header file is a file with the '.h' extension that contains function declarations, macro definitions, and sometimes 'type' definitions. It
// allows you to share code between multiple '.c' files (therefore, a header file is your own personal library that you created whereas a header
// guard is a construct within a header file that prevents multiple inclusions of the same file; they ensure the file is only included one time
// to avoid errors)

// What is the point of making your own library for arrays?: The point of making your own library for arrays is to maximize coding efficiency
// (you don't
// have to use 'for' or 'while' loops for arrays since you typically use 'for' or 'while' loops when working with arrays in C programming,
// which results in more lines of code and less coding efficiency, whereas if you create your own library which initially states and defines
// the functions
// that you'll use for the arrays, you can easily just type the function declaration name in whatever your file is without having to re-state
// the definitions of each
// function declaration since they've already stated in your own person library
// (e.g. 'cs3u.h' and 'cs3u.c' state function declarations and define those
// functions that have been declared, which allows for files such as 'ugochukwu_daluchi_sort.c" to easily use those function declarations without
// having to use 'for' or 'while' loops while working with arrays because your own personal library for the arrays has already been stated and
// defined with code in both your header file and 'cs3u.c' file, which minimzes the lines of code that you have to type in the specified '.c'
// file that you're using to work with arrays, resulting in coding efficiency)
