#include <stdio.h>
#include <string.h>
#include "cs3u.h"

int main(void) {
    // The original version of the ascii art:
    char asciiArt[5][20] = {
        " ^-----^",
        "(  'o'  )",
        "(       )",
        "(       )",
        "(  uu  )"
    }; // All these characters within each row of the ASCII ART are used to display a pig

    printf("\nThis is the original ASCII art:\n");
    for (int i = 0; i < 5; i++) { // Iterates (passes) through each row of the ASCII ART array, which has 5 rows
        printf("%s\n", asciiArt[i]);
    }

    // HORIZONTALLY flip the original ASCII Art
    flipHorizontally(asciiArt, 5);
    printf("\nThis is the horizontally flipped version of the original ASCII art:\n");
    for (int i = 0; i < 5; i++) { // Goes through each row of the ASCII art
        printf("%s\n", asciiArt[i]); // Prints each row of the HORIZONTALLY FLIPPED version of the original ASCII ART, displaying what the
        // 'flipHorizontally' function did to the original ASCII ART array, which was that it horizontally flipped it by providing its function
        // declaration in 'cs3u.h' and ACTUALLY DEFINING the 'flipHorizontally' function in 'cs3u.c'
    }

    // VERTICALLY flip the original ASCII Art
    flipVertically(asciiArt, 5);
    printf("\nThis is the vertically flipped version of the original ASCII art:\n");
    for (int i = 0; i < 5; i++) { // Goes through each row of the ASCII art
        printf("%s\n", asciiArt[i]); // Prints each row of the VERTICALLY FLIPPED version of the original ASCII ART, displaying what the
        // 'flipVertically' function did to the original ASCII ART array, which was that it vertically flipped it by providing its function
        // declaration in 'cs3u.h' and ACTUALLY DEFINING its function declaration 'flipVertically' in 'cs3u.c'
    }
    return 0;
}

// The function declarations in 'cs3u.h' just tells the C program that those functions exist and will be defined later in another program, which
// in this case is in 'cs3u.c', which is where all the function declarations in 'cs3u.h' are then later defined in 'cs3u.c' including
// the 'flipHorizontally' and 'flipVertically' functions
