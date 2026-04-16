#include <stdio.h>

int main(void) {
    int frogs[] = {23, 37, 723, -9, 3, 46, 3, 6}, temp, n = 8, swapped;

    for (int pass = 0; pass < n - 1; pass++) {
        swapped = 0;  // Reset swap flag
        for (int i = 0; i < n - 1 - pass; i++) {
            if (frogs[i] > frogs[i + 1]) {
                temp = frogs[i];
                frogs[i] = frogs[i + 1];
                frogs[i + 1] = temp;
                swapped = 1;
            }
        }
        if (!swapped) break;  // If no swaps, the array is sorted
    }

    for (int i = 0; i < n; i++) printf("%d ", frogs[i]);
    return 0;
}
// Logic behind this code: For the integer, "swapped", if there are no swaps made in a pass, the loop will end early.
// The inner loop reduces the number of comparisons after each pass (n - 1 - pass)
// Achieves the same result as the version underneath, but with fewer lines and minimizes the number of checks, making this code more efficient

/* #include <stdio.h>

int main(void) {
    int frogs[] ={23, 37, 723, -9, 3, 46, 3, 6};
    int temp;
    // Bubble sorting an array
    // Start from index 0 (which is the beginning of the array) to check the values (aka loop)
    for(int pass = 0; pass<7; pass++) {
    for(int i = 0; i<7; i++) { // This for loop needs to loop the appropriate number of checks (n - 1). The number of elements in the array
        // when bubble sorting an array MUST ALWAYS BE THE NUMBER OF ELEMENTS IN THE ARRAY MINUS 1 (n - 1)
        // Check if a swap is needed between 2 values of each swap attemtpion, in the array
    if(frogs[i]>frogs[i+1]) {
        temp = frogs[i]; // saves the earlier position of the array
        frogs[i] = frogs[i+1];
        frogs[i+1] = temp;
    }
    }
    }
    for(int i = 0; i<8; i++) {
        printf("%d ", frogs[i]);
    }
*/

