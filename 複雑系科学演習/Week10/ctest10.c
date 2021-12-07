# include <stdio.h>
# define size 10000     // Change the value depending on the problem

int x_points[size];
int y_points[size];

void henon(long double* x, long double* y, long double a, long double b) {
    long double xx = a - (*x) * (*x) + b * (*y);
    long double yy = (*x);
    *x = xx;
    *y = yy;
}

int main() {
    long double a = 1.4, b = 0.3;
    long double x = 0, y = 0;
    for (int i = 0; i < size; i++) {
        henon(&x, &y, a, b);
        if (i < 10) {
            printf("%d %d\n", x, y);
        }

        /*
        if (i >= 1000) {
            printf("%d %d\n", x, y);
        }
        */
    }
    return 0;
}