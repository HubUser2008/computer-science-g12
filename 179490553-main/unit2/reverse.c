#include <stdio.h>

int reversePrint(int array[], int size) {
    for(int i = size-1; i>=0; i--) {
        printf("%d ", array[i]);
    }
    printf("\n");
    return 0;
}

int main(void) {
    int array1[]={1,2,3,4,5};
    int array2[]={12,45,-8,9,3,77};
    reversePrint(array1, 5);
    reversePrint(array2, 6);

    /*

    for(int i = 0; i<5; i++) {
        printf("%d ", array1[i]);
    }
    printf("\n");
    printf("The reverse list: ");

    for(int i = 4; i>=0; i--){
        printf("%d ", array1[i]);
    }
    printf("\n");

    int array2[] = {12,45,-8,9,3,77};
*/

}
