#include <stdio.h>
#include <stdlib.h>

int sunlight(int *array, int size, int is_west);
int swapEqSum(int *array1, int size1, int *array2, int size2);

int main(){
    int user = 0, seed = 0, i, size = 0, size2 = 0;
    int *array = malloc(size * sizeof(int));
    if (array == NULL) {
        printf("Memory allocation failed\n");
        return 1;
    }
    int *array2 = malloc(size * sizeof(int));
    if (array2 == NULL) {
        printf("Memory allocation failed\n");
        return 1;
    }
    printf("Enter #: 1 (sunlight), 2 (swapEqSum), 0 (quit)\n");
    scanf("%d", &user);

    
    printf("\n");
    if(user == 1){
        int num = 0, done = 0;
        while(user != 3){
            printf("Would like a random array (0), manually enter your array (1), or quit (3): ");
            scanf("%d", &user);

            if(user == 0){
                printf("Enter a seed and array size: ");
                scanf("%d %d", &seed, &size);
                srand(seed);
                for(i = 0; i < size; i++){
                    array[i] = (rand() % 9) + 1;
                    printf("%d ", array[i]);
                }

                printf("Enter west (1) or east (0): ");
                scanf("%d", &num);
                printf("%d", sunlight(array, size, num));
                free(array);
                free(array2);
            } else if(user == 1){
                printf("Enter -1 when done: ");
                i = 0;
                size = 0;
                while(user != -1){
                    scanf("%d", &user);
                    if(user != -1){
                        array[i] = user;
                        size++;
                        printf("%d ", array[i]);
                    }
                    i++;
                }
                printf("Enter west (1) or east (0): ");
                scanf("%d", &num);
                printf("%d", sunlight(array, size, num));
                free(array);
                free(array2);
            } else if(user == 3) {
                free(array);
                free(array2);
                break;
            } else {
                printf("Invalid response, try again\n");
            }
        }
    } else if(user == 2){

        while(user != 3){
            printf("Would like random arrays (0), manually enter your arrays (1), or quit (3): ");
            scanf("%d", &user);

            if(user == 0){
                printf("Enter a seed and array size: ");
                scanf("%d %d", &seed, &size);
                srand(seed);
                for(i = 0; i < size; i++){
                    array[i] = (rand() % 9) + 1;
                    printf("%d ", array[i]);
                }

                printf("Enter a seed and array size: ");
                scanf("%d %d", &seed, &size2);
                srand(seed);
                for(i = 0; i < size2; i++){
                    array2[i] = (rand() % 9) + 1;
                    printf("%d ", array2[i]);
                }
                printf("\n%d", swapEqSum(array, size, array2, size2));


            } else if(user == 1){
                printf("Enter -1 when done: ");
                i = 0;
                size = 0;
                printf("Enter 1st array: ");
                while(user != -1){
                    scanf("%d", &user);
                    if(user != -1){
                        array[i] = user;
                        size++;
                        printf("%d ", array[i]);
                    }
                    i++;
                }
                printf("Enter 2nd array: ");
                i = 0;
                size2 = 0;
                while(user != -1){
                    scanf("%d", &user);
                    if(user != -1){
                        array2[i] = user;
                        size2++;
                        printf("%d ", array2[i]);
                    }
                    i++;
                }

                printf("\n%d", swapEqSum(array, size, array2, size2));
                
            } else if(user == 3){
                free(array);
                free(array2);
                break;
            } else{
                printf("Invalid response, try again\n");
            }

        }
        /*Example vals:
        int arr[6] = {4, 1, 2, 1, 1, 2};
        int arr2[4] = {3, 6, 3, 3};
        size = 6;
        size2 = 4;
        */
        printf("\n%d", swapEqSum(array, size, array2, size2));
    } else if(user == 0){
        return 0;
    } else{
        printf("ERROR: number not recognized");
    }
}
/*
Exercise 1.
Given the heights of the trees that lie adjacent to each other, sunlight shines from either the west or the east side of the forest. 
If there is a tree of height H and the sunlight is from the west, all the trees smaller than H on the east of it are blocked and do not receive sunlight. 
Find the total number of the trees that receive sunlight. 
*/

/*
 * array: the heights of the trees
 * size: the size of the array
 * is_west: 1- sunlight from west, 0- sunlight from east 
 */
int sunlight(int *array, int size, int is_west){
    int large = 0, i, count = 0;
    if(is_west == 1){
        for(i = 0; i < size; i++){
            if(array[i] > large){
                count++;
                large = array[i];
            }
        }

    } else if(is_west == 0){
        for(i = size-1; i >= 0; i--){
            if(array[i] > large){
                count++;
                large = array[i];
            }
        }
    } else{
        return -1;
    }

    return count;
}


/*
Exercise 2.
Given two arrays of integers, write a function to check if a pair of values (one value from each array) 
exists such that swapping the elements of the pair makes the sum of two arrays equal. 
If the pair exists, the elements of the pair are swapped after the function call. 

Example:
Array1 = [4, 1, 2, 1, 1, 2] = 11
Array2 = [3, 6, 3, 3] = 15

After the function call, 
Array1 = [6, 1, 2, 1, 1, 2] = 13
Array2 = [3, 4, 3, 3] = 13
*/

/*
 * inputs::
 * array1, array2: two arrays
 * size1, size2: the size of the arrays
 * output::
 * 1 if the pair exists
 * 0 if not
 */
int swapEqSum(int *array1, int size1, int *array2, int size2){
    //find sums of both arrays
    int sum1 = 0, sum2 = 0, i, j;

    for(i = 0; i < size1; i++){
        sum1 = sum1 + array1[i];

    }
    printf("\n%d ", sum1);
    for(i = 0; i < size2; i++){
        sum2 = sum2 + array2[i];
    }
    printf("%d \n", sum2);
    if(sum1 == sum2){
        return 0;
    }

    int count = 0;
    for(i = 0; i < size1; i++){
        for(j = 0; j < size2; j++){
            int temp1 = sum1, temp2 = sum2;
            temp1 = temp1 - array1[i] + array2[j];
            temp2 = temp2 - array2[j] + array1[i];
            printf("Pass %d: temp1 = %d, temp2 = %d ", count, temp1, temp2);
            if(temp1 == temp2){
                return 1;
            }
            count++;
        } printf("\n");
    }

    return 0;
}
