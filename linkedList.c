#include <stdio.h>
#include <stdlib.h>
/*
Test Data :

Input the number of nodes : 3
Input data for node 1 : 5
Input data for node 2 : 6
Input data for node 3 : 7

Expected Output :

 Data entered in the list :                                                                                   
 Data = 5                                                                                                     
 Data = 6                                                                                                     
 Data = 7 
*/
typedef struct Node{
    int data;
    struct Node* next;
} Node;
int main(){
    //init list
    Node* list = (Node*) malloc(sizeof(Node));
    list->data = 0;
    list->next = NULL;

    int user = 1, count = 0;
    while(user){
        printf("Enter a number: ");
        int num = 0;
        scanf("%d", &num);
        if(count == 0){
            list->data = num;
        } else{
            Node* curr = list;
            while(curr->next != NULL){
                curr = curr->next;
            }
            Node* new_node = (Node*) malloc(sizeof(Node));
            new_node->data = num;
            new_node->next = NULL;
            curr->next = new_node;
        }
        count++;
        printf("\nWould you like to enter another node? (1) yes, (0) no: ");
        scanf("%d", &user);
    }

    printf("Initial list:\n");
    Node* curr = list;
    while(curr != NULL){
        printf("Data = %d\n", curr->data);
        curr = curr->next;
    }

    printf("After getting rid of every other node: \n");
    count = 1;
    curr = list;
    Node* prev = NULL;
    while(curr != NULL){
        if(count % 2 == 0){
            prev->next = curr->next;
            Node* temp = curr;
            curr = curr->next;
            free(temp);
        } else{
            prev = curr;
            curr = curr->next;
        }
        count++;
    }

    curr = list;
    while(curr != NULL){
        printf("Data = %d\n", curr->data);
        curr = curr->next;
    }

    Node* temp;
    while(curr != NULL){
        temp = list;
        list = list->next;
        free(temp);
    }
}

