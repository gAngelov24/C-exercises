#include <stdio.h>
/*
Write a function that compares two strings. This function starts comparing the first character of each string. 
If they are equal to each other, it continues with the following pairs until the characters differ or until a terminating null-character is reached. 
Do not use “string.h”.

Output:
ABC is less than ABCD

*/


int stringcmp(const char *str1, const char *str2){
    int i = 0, ret = 0;
    while(str1[i] != '\0' || str2[i] != '\0'){
        if(str1[i] < str2[i]){
            ret = -1;
            break;
        } else if(str1[i] > str2[i]){
            ret = 1;
            break;
        } 
        i++;
    }

    return ret;
}

int main(){
    char *str1 = "ABC";
    char *str2 = "ABCD";

    int ret = stringcmp(str1, str2);
    if(ret == 0)
        printf("%s and %s are the same. \n", str1, str2);
    else if(ret <0)
        printf("%s is less than %s. \n", str1, str2);
    else
        printf("%s is greater than %s. \n", str1, str2);

    return 0;
}
