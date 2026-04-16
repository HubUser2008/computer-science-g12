#include <stdio.h>
#include <cs50.h>
#include <stdlib.h> // for rand() and srand() - the "s" stands for seed and "rand" stands for random = random seed
#include <time.h> // for time ()

int main(void) {
// Declaring all the variables that will be used for ONLY the first 2 cards
    char card1, card2;
    int value1, value2, total;
    value1 = 0;
    value2 = 0;
    total = 0;

    // Tell the user to enter the value of their first card (2-9 for the numbers, T for 10, J for Jack, Q for Queen, K for King, and A for Ace)
    printf("Enter the value of your first card (2-9, T for 10, J for Jack, Q for Queen, K for King, A for Ace): ");
    scanf(" %c", &card1);

    // Tell the user to enter the value of their second card (2-9 for numbers, T for 10, J for Jack, Q for Queen, K for king, and A for Ace)
    printf("Enter the value of your second card (2-9, T for 10, J for Jack, Q for Queen, K for King, A for Ace): ");
    scanf(" %c", &card2);

    // Determine the numerical value of the first card using inequalities
    if (card1 >= '2' && card1 <= '9') {
        value1 = card1 - '0';  // Convert char digit to integer
    } else if (card1 == 'T' || card1 == 'J' || card1 == 'Q' || card1 == 'K') {
        value1 = 10;  // 10, Jack, Queen, King are worth 10
    } else if (card1 == 'A') {
        value1 = 1;  // Ace is worth 1 (simplified version)
    }

    // Determine the numerical value of the second card using inequalities
    if (card2 >= '2' && card2 <= '9') {
        value2 = card2 - '0';  // Convert char digit to integer
    } else if (card2=='T'||card2=='J'||card2=='Q'||card2=='K') {
        value2 = 10;  // The number 10, Jack, Queen, and King are all worth 10
    } else if (card2 == 'A') {
        value2 = 1;  // Ace is only worth 1
    }

    // Calculate the total value of the two cards
    total = value1 + value2;

    // Make the program print the value of the first card, the value of the 2nd card, and the total values of both of them combined
    printf("Your first card is worth: %d\n", value1);
    printf("Your second card is worth: %d\n", value2);
    printf("Your hand is worth: %d\n", total);

    // Declaration of the variables that will be used for the potential 3rd card if the user chooses to hit
        char choice;
        int card3, total2;
        card3 = 0;
        total2 = 0;

    // Random number generator. The s stands for "seed" and "rand" stands for "random". The current real time will be used as a "seed"
    // in order to generate random numbers, meaning that the current time in real life will be used as a sort of representation model
    // for random numbers to be based off of the representation model (which is the time in real life), which will give the specific
    // random numbers that I coded for below
    srand(time(NULL));

    // Declare all the possible numbers that the "srand" code will use. Each number stands for a card in blackjack and its numerical value
    char cards[] = {'2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A'};

    // Asking the user whether they want to get another card or just stay. "h" stands for hit and "s" stands for stay.
    // The space between " and %c is for skipping over any leading whitespace characters such as spaces, tabs, or new lines, which tells
    // the program to wait for the next non-whitespace character to be entered by the user. This is important because without the space
    // before "%c", the user could've entered a whitespace character which "scanf" would've read as the answer for "choice", messing up
    // the entire code
        printf("Do you want to hit (get another card) or stay? Enter 'h' to hit or 's' to stay: ");
        scanf(" %c", &choice);

        // if the user presses h, their 3rd card will be generated at random from the 13 possible card options. Once it has been generated
        // the program will then tell the user what their 3rd card is
        if (choice == 'h') {
            // Pick a random card
            card3 = cards[rand() % 13]; // There are 13 possible cards
            printf("You got a card: %c\n", card3);

            // Add the card value to the total. Tell the user the total value of their new hand if they decided to hit (get another card)
            // If the user decided to stay, tell the user that they decided to stay and repeat to them the value of their hand,
            // with their hand being the 1st cards that they themselves picked at the beginning
            total2 += value1 + value2 + card3;
            printf("The total value of your new hand is now: %d\n", total2);
        } else if (choice == 's') {
            printf("You chose to stay. Your final total is: %d\n", total);
        }
        // If neither of the above commands are run, it means that the user typed in the wrong input
        // Tell the user that they typed in a wrong input; prompt them to type the right input
        // by asking them the same question again, "do you want to hit or stay?"
        else {
            printf("Invalid choice. Please enter 'h' to hit or 's' to stay: \n");
        }
    while (choice != 's'); // End the program loop if the user decides to "stay"

    return 0;
}
