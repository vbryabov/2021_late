#include<stdio.h>
#define N 100
double next(double x, double r) {
    if (0 <= x && x <= 0.5) {
        return 2 * x;
    } else {
        return 2 * (1 - x);
    }
    // return r * (1 - x) * x;
}
int main(void){
    int n;
    double r;
    double xn = 0.7;
    double xn1;
    scanf("%lf", &r);
    for(n = 0; n <= N; n++) {
        xn1 = next(xn, r);
        printf("%lf %lf\n", xn, xn1);
        printf("%lf %lf\n", xn1, xn1);
        xn = xn1;
    }
    return 0;
}