#include <stdio.h>
/*
Write a function that computes the sum of the 2D array elements at the boundary. For example, the function returns 65 for the following input array. 

1	2	3
4	5	6
7	8	9
10	11	12

1+2+3+4+6+7+9+10+11+12 = 65

*/

int sumBound(const int *array, int row, int col){
    int length = row*col , r, c, sum = 0;
    for(r = 0; r < row; r++){
        for(c = 0; c < col; c++){
            if(r == 0 || c == 0 || r == (row-1) || c == (col-1)){
                sum = sum + array[r*col+c];
            }
        }
    }
    return sum;

}
int main(){
    int array[4][3] = {{1,2,3},{4,5,6},{7,8,9},{10,11,12}};
    printf("The sum of boundary is %d.\n", sumBound(&array[0][0], 4, 3));
    return 0;
}
