#include <stdio.h>

int main(void) {

    char* rainbow[7] = {"r", "o", "y", "g", "b", "i", "v"};
    char* totalRainbow = rainbow[7];
    while (char c = 0; c <= 7; c++){
        totalRainbow += rainbow [c];
    }
    printf("%c\n", totalRainbow[c]);

}
