#include <stddef.h>
#include <stdbool.h>
#include <stdio.h>
/*
Given a positive integer n, write a function to find the maximum number k that satisfies the following equation. Do not use the math library

2^k <= n. The function should take an integer as input and return the maximum k.

Output example: 
Enter a positive integer: 2 Maximum k that satisfies 2^k<=n is 1 
Enter a positive integer: 17 Maximum k that satisfies 2^k<=n is 4


To compile: gcc -o exercises exercises.c
To run (in terminal): exercises (or) ./exercises

*/

int maxk(int n){
    int power = 0, num = n;
    bool flag = true;
    if(n == 0){
        return -1;
    } else if(n == 1){
        return 0;
    } else if(n == 2){
        return 1;
    }
    int cur = num;
    while(num > 0){
        cur = num /2;
        if(cur > 0){
            power++;
        }
        num = cur;
    }
    return power;
}

int main(){
    int n;
    printf("Enter a positive integer: ");
    scanf("%d", &n);

    printf("Maximum k that satisfies 2^k<=n is %d\n", maxk(n));
    return 0;
}

