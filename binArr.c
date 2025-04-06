#include <stdio.h>
/*
Write a function that takes a decimal number (you may assume the number is positive) and returns the number of digits in binary. 
For example, if the decimal input is 6, it returns 3. 

Write a function that converts the decimal input to the binary format in array. 
If the decimal input is 6, then array[0] = 0, array[1] = 1, array[2] = 1. The least significant bit stores at the lowest index. 

Output Example:
Input a decimal number: 18
Number of digit in binary: 5
10010

*/
unsigned int bindigit(unsigned int dec){
    int i;
    int num = (int) dec;
    while(num > 0){
        num = num/2;
        i++;
    }
    return i;
}
void dec2bin(unsigned int *arr, int count, unsigned int dec){
    unsigned int temp = dec;
    for(int i = count - 1; i >= 0; i--){
        int sub = 1;
        for(int j = 0; j < i; j++){
            sub = sub * 2;
        }
        if(sub <= temp){
            temp = temp - sub;
            arr[i] = 1;
        } else{
            arr[i] = 0;
        }
    }

}

int main(){
    unsigned int dec;
    printf("Input a decimal number: ");
    scanf("%d", &dec);

    unsigned int N, arr[32];
    int i;
    N = bindigit(dec);
    printf("Number of digit in binary: %d\n", N);

    dec2bin(arr, N, dec);
    for(i=N-1; i>=0; i--)
        printf("%d", arr[i]);
    printf("\n");
    return 0;
}
