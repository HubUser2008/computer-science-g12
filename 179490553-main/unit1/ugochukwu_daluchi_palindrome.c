#include <stdio.h>
#include <cs50.h>
#include <math.h>

int main(void) {
// the value of the integer of the variable, 'number' is going to then get reversed using the palindrome, which right now, is 0 because
// the palindrome must have a numerical value of 0 in order to reverse the original number correctly


    int number, palindrome;
    number = get_int("provide an integer that is 2 digits - 7 digits, NOT A NEGATIVE NUMBER, and is MORE THAN 0: ");
    palindrome = 0;

// the number's numerical value must be more than 10 because in order for a reversed number to actually be recognized,
// the number has to be 2 digits or more, so I wrote in code, if the value of the number is less than 10, meaning that it's only 1 digit,
// then the program will ask the user to input another number that follows the digit the requirement

// if the number is more than 7 digits, the user will be prompted to provide a number that is exactly 7 digits or less

// the number must also not be a negative number because it interrupts my code entirely so I made sure that the user knows not to provide
// a negative number. If the user provids a negative number, the code will ask for a proper number to be implemented

// if the integer provided as a number is 0, the code will prompt the user to provide a proper number

    if(number==0) {
        printf("Stop. Provide a proper number following the digits requirement (2-7 digits) and the numerical value requirement (more than 0)\n");
        number = get_int("Provide your correct integer: ");
    }


    if(number<10) {

        printf("You didn't provide a number that is 2 digits - 7 digits long or you provided a NEGATIVE NUMBER! Provide another integer that follows the digit/value requirement!\n");
        number = get_int("PROVIDE AN INTEGER THAT IS 2 DIGITS OR MORE: ");
    }
    if(number>9999999) {
        printf("You provided a number that is more than 7 digits long! Provide another integer that follows the digit requirement!\n");
        number = get_int("PROVIDE AN INTEGER THAT IS 7 DIGITS OR LESS: ");
    }

    while (number==0);

// The 1st step is to get the last digit from the number provided

// The 2nd step is to add the digit to a new number

// The 3rd step is to divide the input number by 10, in order to move on to the next digit of the input number
// (that's why if the last digit is 0, a new digit is not moved on because 0/10 = 0 and since 0 doesn't need to be written,
// nothing appears as the palindrome for 0 (the reversed number of 0 is 0, so nothing appears))

// multiplying the palindrome (which is 0 right now) by 10 will move on to the next digit,
// then adding that product to the remainder of the number (which will be the last digit of the integer provided)
// Then the code will divide the number by 10 which will result in the next digit, and the process repeats until there are no more digits left
    while (number != 0){
        palindrome = palindrome * 10;
        palindrome = palindrome + number % 10;
        number /= 10;
    }
    printf("The palindrome (reversed) number of the original integer that you provided is %i\n", palindrome);
}
