#include <stdio.h>
#include <cs50.h>

void sayName(string s);

int main(void) {
    string name = get_string("What is your name?\n");
    sayName(name);
}

// says name
void sayName(string s)
{
    printf("Hello my name is %s\n", s); // "sayName" was originally given the command "name" but then it was re-identified in this line of code
                                        // as "s", so you say "s" in the printf statement, and NOT "name"
}
