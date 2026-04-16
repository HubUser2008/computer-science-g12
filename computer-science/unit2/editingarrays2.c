#include <stdio.h>
#include <time.h>
#include <stdlib.h>

int main(void) {
    srand(time(NULL)); // Start at a different seed (so that you don't get the same random number each time, hence the use of "NULL")
    int elems = rand()%15; // A random number from 0-14 (% 15 = not including 15, so any integer less than 15)
    int newnums[elems];
    int len = sizeof(newnums) / sizeof(newnums[0]);

    for(int i = 0; i<len; i++) {
        newnums[i] = rand()%11;
        printf("%d ", newnums[i]);
    if(int i = 9;) {
        newnums[i] = rand()%8;
        printf("%d ", newnums[i])
    }
    }
// Try to COMPLETELY REMOVE a number of your choice from the random array provided below
}
