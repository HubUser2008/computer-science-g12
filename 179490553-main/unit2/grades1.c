#include <stdio.h>
#include <cs50.h>

int main (void){

    int grades[6] = {12, 23, 34, 45, 56, 67};
    int highest = 0;
    int lowest = 100;
    int totalGrades = 0;
    for (int i = 0; i<6; i++){
    totalGrades += grades[i];

    if (grades[i] > highest){
            highest = grades[i];
    }
    if (grades[i] < lowest){
        lowest = grades[i];
    }

    }
    printf("%i is the total grades, ", totalGrades);
    printf("%i is the average grade, ", totalGrades/6);
    printf("%i is the lowest grade, ", lowest);
    printf("%i is the highest grade\n", highest);

}
