#include <stdio.h>
#include <cs50.h>
#include <math.h>

int main(void){

        int x, y, product;
        x = get_int("What's the width of your rectangle: ");
        y = get_int("What's the length of your rectangle: ");
        product = x*y;
        printf("The area of your rectangle is: %i\n",product);

 /*       double x, y;
        x = get_double("provide an integer ");
        y = get_double("provide another integer ");
        double quotient = x/y;
        printf("%f\n",quotient);

        int x, radius, area;
        x = get_int("State the circumference: ");
        radius = x/2*3.14159265359;
        area = 4*3.14159265359*radius*radius;
        printf("The radius of the circle is: %i\n",radius);
        printf("The surface area of the sphere is: %i\n",area);
*/
}
