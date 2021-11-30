#include <stdio.h>
#define N 1000000
#define nSizeMax 1000

#define xmin -1.5
#define xmax 1.5
#define ymin -0.5
#define ymax 0.5

int hist[nSizeMax][nSizeMax];

void next(double* x, double* y, double a, double b) {
    double xx = (*y) + 1 - a * (*x) * (*x);
    double yy = b * (*x);
    *x = xx;
    *y = yy;
}

// initialization
void init(int nS) {
    int i, j;
    for ( i = 0; i < nS; i++ ) {
        for ( j = 0; j < nS; j++ ) {
            hist[i][j] = 0;
        }
    }
}

// print out
void print(int nS) {
    int i, j, count = 0;
    for ( i = 0; i < nS; i++ ) {
        for ( j = 0; j < nS; j++ ) {
            if (hist[i][j]) {
                count++;
            }
        }
    }
    printf("%d %d\n", nS, count);
}


int main(){
    double a = 1.4, b = 0.3;
    double x = 0.5, y = 0.5;

    for (int nSize = 0; nSize <= 500; nSize++) {
        init(nSize);
        int px, py;
        for (int n = 0; n <= N; n++) {
            next(&x, &y, a, b);
            if (n > 10000) {
                px = (int)((x - xmin) / (xmax - xmin) * nSize);
                py = (int)((y - ymin) / (ymax - ymin) * nSize);
                hist[px][py] = 1;
            }
        }
        print(nSize);
    }
    return 0;
}