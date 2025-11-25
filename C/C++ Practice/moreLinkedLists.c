#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define BUF_SIZE 32

/*
Exercise 1.
We will modify the student management program from Worksheet17 and Worksheet18. 
The new program uses a linked list to store the student data. 
The new structure for the record is defined as:

*/


typedef struct node_t{
    char *FirstName;
    int UIN;
    float GPA;
    struct node_t *next;
} node;
void insert_sorted_name(node** head, node *data);
void print_list(node *head);
void print_list_GPA(node *head, float low, float high);
void delete_all(node **head);

int main(){
    node *head = NULL;
    int temp;
    char buf[BUF_SIZE];

    while(1){
        printf("Enter student's UIN: ");
        scanf("%d", &temp);
        if(temp == -1){
            break;
        }
        node data;
        data.UIN = temp;
        printf("Enter student's first name and GPA: ");
        scanf("%s %f", buf, &(data.GPA));
        data.FirstName = (char*)malloc(strlen(buf)+1);
        strcpy(data.FirstName, buf);

        insert_sorted_name(&head, &data);
        //free(data.FirstName);
    }
    print_list(head);

    float low, high;
    printf("Enter GPA range to print list(low-high): ");
    scanf("%f %f", &low, &high);
    print_list_GPA(head, low, high);
    delete_all(&head);
    return 0;
}

/*
This function inserts a new node to the linked list so that 
the names are sorted in ascending order. For example,
Alice->Casey->NULL
Alice->Bob->Casey->NULL
*/
void insert_sorted_name(node** head, node *data){
    node* list = *head;
    node* prev = NULL;
    while(list != NULL){
        if(strcmp(data->FirstName, list->FirstName) < 0){
            if(prev == NULL){
                *head = data;
                data->next = list;
                break;
            }
            data->next = list;
            prev->next = data;
            break;
        }
        prev = list;
        list = list->next;
    }
}

/*
This function prints out all the students’ information. For example, 
UIN, FirstName, GPA
1, Alice, 2.000000
3, Bob, 2.800000
2, Casey, 3.000000
*/
void print_list(node* head){
    while(head != NULL){
        printf("%d, %s, %f", head->UIN, head->FirstName, head->GPA);
        head = head->next;
    }
}

/*
This function prints out the students whose GPA is between low and high values. 
For the above example, if low is 3.0 and high is 4.0, then
UIN, FirstName, GPA
2, Casey, 3.000000
*/
void print_list_GPA(node *head, float low, float high){

}

void delete_all(node** head){
    node* cur = *head;
    node* next = *head;
    while(cur != NULL){
        free(next->FirstName);
        cur = next;
        next = cur->next;
        free(cur);
    }
    *head = NULL;
}