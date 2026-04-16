#include <stdio.h>
#include <cs50.h>

int main (void){
    printf("Welcome to the Akinator 2.0 game! You can ONLY USE ONE OF THE FOLLOWING: cat, dog, human, pinetree, alligator, or salmon\n");

    int cat, dog, human, pinetree, alligator, salmon;

    cat = 0;
    dog = 0;
    human = 0;
    pinetree = 0;
    alligator = 0;
    salmon = 0;

    char q1 = get_char("Is it an animal (humans are considered animals)? Y or N: \n");

    if(q1=='Y'||q1=='y') {
        cat++;
        dog++;
        human++;
        alligator++;
        salmon++;
    }
    else {

        pinetree = pinetree + 2;
    }
    char q2 = get_char("Does it live on land (Alligators are considered to live on land for this question? Y or N: \n");

    if(q2=='Y'||q2=='y') {
        cat++;
        dog++;
        human++;
        pinetree++;
        alligator++;
    }
    else {

        salmon += 2;
    }
    char q3 = get_char("Is it a reptile? Y or N: \n");

    if(q3=='Y'||q3=='y') {

        alligator += 2;
    }
    else {
        cat++;
        human++;
        pinetree++;
        salmon++;
        dog++;
    }
    char q4 = get_char("Can it speak english? Y or N: \n");

    if(q4=='Y'||q4=='y') {

        human += 2;
    }
    else {
        cat++;
        dog++;
        alligator++;
        pinetree++;
        salmon++;
    }
    char q5 = get_char("Is it known for its loyalty (humans are not considered loyal for this question)? Y or N: \n");

    if(q5=='Y'||q5=='y') {

        dog = dog + 2;
    }
    else {
        cat++;
        human++;
        alligator++;
        pinetree++;
        salmon++;
    }
    char q6 = get_char("Does it have sharp claws that it uses for scratching things (N is the answer to this question if you're thinking of dogs/alligators)? Y or N: \n");

    if(q6=='Y'||q6=='y') {

        cat += 2;
    }
    else {
        human++;
        dog++;
        alligator++;
        salmon++;
        pinetree++;
    }
    if (cat>6) {
        printf("You're thinking of a cat!\n" );
    }
    else if (dog>6) {
        printf("You're thinking of a dog!\n" );
    }
    else if (human>6) {
        printf("You're thinking of a human!\n" );
    }
    else if (pinetree>6) {
        printf("You're thinking of a pinetree!\n" );
    }
    else if (alligator>6) {
        printf("You're thinking of an alligator!\n" );
    }
    else {
        printf("You're thinking of a salmon!\n" );
    }

/*
    int console, pc;
    console = 0;
    pc = 0;

    char q1 = get_char("Is it more powerful (performance-wise) than a console? Y or N: \n");

    if (q1=='Y'||q1=='y') {
        pc++;
    }
    else {
        console++;
    }
    if (pc>0) {
        printf ("You're thinking of a PC!\n");
    }
    else {
        printf("You're thinking of a console\n");
    }
    */
}
