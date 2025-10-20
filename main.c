#include <stdio.h>
#include <math.h>  // for sqrt() function

int main() {
    float a, b, c, discriminant, root1, root2;

    printf("Enter coefficients a, b, and c: ");
    scanf("%f %f %f", &a, &b, &c);

    discriminant = b*b - 4*a*c;

    if (discriminant > 0) {
        root1 = (-b + sqrt(discriminant)) / (2*a);
        root2 = (-b - sqrt(discriminant)) / (2*a);
        printf("Roots are real and different.\n");
        printf("Root1 = %.2f and Root2 = %.2f\n", root1, root2);
    }
    else if (discriminant == 0) {
        root1 = -b / (2*a);
        printf("Roots are real and equal.\n");
        printf("Root1 = Root2 = %.2f\n", root1);
    }
    else {
        // Negative discriminant → no real roots
        printf("No real roots exist.\n");
    }

    return 0;
}