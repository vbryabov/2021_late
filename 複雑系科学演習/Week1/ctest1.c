#include<stdio.h>
#include<stdlib.h>

int main(void) {
    int cnt = 0;
    for (int i = 1; i < 101; i++){
        cnt += i;
        printf("%d %d \n", i, cnt);
    }
    return 0;
}