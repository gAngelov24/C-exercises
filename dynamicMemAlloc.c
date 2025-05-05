#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define BUF_SIZE 12
struct StudentStruct{
    char *FirstName;
    int UIN;
    float GPA;
};
typedef struct StudentStruct student;
void SwapStudent(student *s1, student *s2);
void PrintAllStudent(student *s, int total);
void SortGPA(student *s, int total);


int main(){
    student *s = NULL;
    student *more_s = NULL;
    int total = 0, temp;
    float gpa = 0;
    char buf[BUF_SIZE];

    while(1){
        printf("Enter student's UID: ");
        scanf("%d", &temp);
        if(temp == -1){
            break;
        }
        more_s = (student*)realloc(s, sizeof(student)*(total+1));
        if(more_s != NULL){
            s = more_s;
        } else{
            printf("No more students can be added\n");
            break;
        }
        printf("Enter student First Name, UIN and GPA:");
        scanf("%s %d %f", buf, &temp, &gpa);
        s[total].FirstName = (char*)malloc(strlen(buf)+1);
        strcpy(s[total].FirstName, buf);
        s[total].UIN = temp;
        s[total].GPA = gpa;
        temp = 0;
        total++;
    }
    PrintAllStudent(s, total);
    SortGPA(s, total);
    printf("\n<< Sorted Result >>\n");
    PrintAllStudent(s, total);
    for(int i = 0; i < total; i++){
        free(s[i].FirstName);
    }
    free(s);
    return 0;
}

void SwapStudent(student *s1, student *s2){
    student temp;
    temp = *s1;
    *s1 = *s2;
    *s2 = temp;
}

void PrintAllStudent(student* s, int total){
    for(int i = 0; i < total; i++){
        printf("%s, UIN: %d, GPA: %f \n", s[i].FirstName, s[i].UIN, s[i].GPA);
    }
}
void SortGPA(student* s, int total){
    for(int i = 0; i < total-1; i++){
        for(int j = i+1; j < total; j++){
            if(s[j].GPA < s[i].GPA){
                SwapStudent((s+j), (s+i));
            }
        }
    }
}
