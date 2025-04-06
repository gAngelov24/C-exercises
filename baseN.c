#include <stdio.h>
#include <math.h>

/*
Write a function that calculates the number of digits of a decimal integer in base N.  
For example, 27 in base 4 is 27 = 4^(2 )+2⋅4+3⋅1=123_4. Therefore, the function returns 3.  

Use the above function and implement a function that prints out a decimal integer in base N. 
You can assume both the input number and the base are positive integers. You may use the math library.

Output example:
type number: 27
type base N: 4
number of digits: 3
123

Output example:
type number: 16
type base N: 2
number of digits: 5
10000

*/


/* Calculate the number of digits in base N */
int getDigitBaseN(int number, int N){
    int i = 0; 
    while(pow(N, i) <= number){
        i++;
    }
    return i;
    
}

/* Print out a number in base N */
void printBaseN(int number, int N){
    int digit = getDigitBaseN(number, N);
    int num = 0, temp = number;
    for(int i = digit-1; i >= 0; i--){
        while(temp >= 0){
            temp = temp - pow(N,i);
            num++;
        }
        num--;
        printf("%d", num);
        num = 0;
        temp = temp + pow(N,i);
    }

}
int main(){
    int number, N;
    printf("type number: ");
    scanf("%d", &number);
    printf("type base N: ");
    scanf("%d", &N);

    printf("number of digits: %d\n", getDigitBaseN(number, N));
    printBaseN(number, N);

    return 0;
}
