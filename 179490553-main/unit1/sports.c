#include <stdio.h>
#include <cs50.h>
#include <math.h>

int main(void) {

    printf("Welcome to the 'which sport do you like quiz!'\n");

    int football, basketball, soccer, track;

    basketball = 0;
    soccer = 0;
    football = 0;
    track = 0;

    char q1 = get_char("Do you enjoy physical activity (coming in contact/hitting/bumping teammates/opponents)?: Y or N\n");

    if(q1=='Y'||q1=='y') {
        football += 5;
        basketball += 3;
        soccer += 2;
    }
    else{
        track += 5;
    }
    char q2 = get_char("Do you like running/sprinting?: Y or N\n");

    if(q2=='Y'||q2=='y') {
        track += 5;
        football +=4;
        soccer += 4;
    }
    else{
        basketball += 3;
    }
    char q3 = get_char("Do you enjoy sports games that last a long time?: Y or N\n");

    if(q3=='Y'||q3=='y') {
        soccer += 5;
        football += 4;
        basketball += 2;
        track += 3;
    }
    else{
        basketball += 2;
        soccer += 5;
        football += 4;
        track += 3;
    }
    char q4 = get_char("Do you like team-based sports more than individual-based sports?: Y or N\n");

    if(q4=='Y'||q4=='y') {
        football += 5;
        basketball += 4;
        soccer += 5;
    }
    else{
        track += 3;
    }
    char q5 = get_char("I would rather watch basketball and soccer over football and track: Y or N\n");

    if(q5=='Y'||q5=='y') {
        basketball && soccer++;
    }
    else{
        football && track++;
    }
    if(basketball&&soccer > football&&track) {
        printf("CONGRATS! You prefer playing/watching basketball and/or soccer over football and/or track!\n");
    }
    else {
        printf("CONGRATS! You prefer playing/watching football and/or track over basketball and/or soccer!\n");
    }
}
