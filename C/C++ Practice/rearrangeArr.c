#include <stdio.h>
/*
Write a function that rearranges the array elements, where the odd integers are filled from the lowest index and the even integers from the highest index. 
For example, if the array is [1, 9, 4, 3, 8, 7, 1, 2], then it is updated as [1, 9, 3, 7, 1, 2, 8, 4] after the function call. 
*/

void oddeven(int *arr, unsigned int count){
    int temp[count], i, j;
    for(i = 0; i < count; i++){
        temp[i] = -1;
    }
    
    for(i = 0; i < count; i++){
        if(arr[i] % 2 == 1){
            for(j = 0; j < count; j++){
                if(temp[j] == -1){
                    temp[j] = arr[i];
                    break;
                }
            }
        }
    }
    for(i = 0; i < count; i++){
        if(arr[i] % 2 == 0){
            for(j = count-1; j > 0; j--){
                if(temp[j] == -1){
                    temp[j] = arr[i];
                    break;
                }
            }
        }
    }
    for(i = 0; i < count; i++){
        arr[i] = temp[i];
    }

}

int main(){
    int arr[50];
    int i, N;
    for(i=0; i<50; i++){
        scanf("%d", arr+i);
        if(arr[i] == -1)
            break;
    }
    N = i;
    oddeven(arr, N);
    for(i=0; i<N; i++){
        printf("%d ", arr[i]);
    }
    printf("\n");
    return 0;
}
