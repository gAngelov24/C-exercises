#include <stddef.h>
#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
typedef struct dll_node_t {
    int val;
    struct dll_node_t *next;
    struct dll_node_t **prev;
} dll_node;

void dll_insert_head(dll_node **head, int v) {
    dll_node *tmp = malloc(sizeof(*tmp));
    tmp->val = v;
    tmp->next = *head;
    if (*head)
        (*head)->prev = &(tmp->next);
    tmp->prev = head;
    *head = tmp;
}

void dll_insert_sorted(dll_node **head, int v) {
    dll_node *tmp = malloc(sizeof(*tmp));
    tmp->val = v;
    while (*head && ((*head)->val < v))
        head = &((*head)->next);
        tmp->next = *head;
    if (*head)
        (*head)->prev = &(tmp->next);
    tmp->prev = head;
    *head = tmp;
}

void dll_print(const dll_node *head) {
    while (head) {
        printf("%d ", head->val);
        if (head->next)
            assert(head->next->prev == &head->next);
        head = head->next;
    }
    printf("\n");
}
/*
This function updates the list such that there are no more than 
max_duplicate duplicate nodes. For the following example:
0<->1<->1<->2<->2<->3<->3<->3<->3->NULL
If max_duplicate = 4, then the list remains the same. 
If max_duplicate = 2, then the list is updated as:	
0<->1<->1<->2<->2<->3<->3->NULL
Assume that max_duplicate is greater than or equal to 1. 
*/
void dll_compress(dll_node **head, int max_duplicate){
    /* Your code here */
    dll_node* list = *head;
    int count = 0, flag = max_duplicate;
    int cur = list->val, prev_val = list->val;

    while(list != NULL){
        cur = list->val;
        if(cur == prev_val){
            count++;
            if(count > flag){
                //remove duplicates
                dll_node* temp = list;
                if (list->next) {
                    list->next->prev = list->prev;
                }
                if(list->prev){
                    *(list->prev) = list->next;
                } 
                list = list->next;
                free(temp);
                continue;
            }
        } else{
            count = 1;
            prev_val = cur;
        }
        //prev_val = cur;
        list = list->next;
    }  
}
/*
This function counts the maximum duplicate nodes. For the following example,
0<->1<->1<->2<->2<->3<->3<->3<->3->NULL
the function returns 4
*/
int dll_max_duplicate(dll_node *head){
    int max = 0, cur = 0, prev = head->val, count = 0;
    dll_node* list = head;
    while(list != NULL){
        cur = list->val;
        if(cur == prev){
            count++;
            if(count > max){
                max = count;
            }
        } else{
            count = 1;
        }
        prev = cur;
        list = list->next;
    }
    return max;
}

void dll_remove_all(dll_node **head){
    dll_node *tmp;
    while(*head){
        tmp = (*head)->next;
        free(*head);
        *head = tmp;
    }
}

int main() {
    dll_node *head = NULL;
    int i;
    int arr[11] = {3,1,1,2,2,2,3,3,3,0,3};

    for(i=0;i<11;i++)
        dll_insert_sorted(&head, arr[i]);
    dll_print(head);
    printf("Max number of duplicates: %d\n", dll_max_duplicate(head));

    int n;
    printf("Enter a new number of duplicates: ");
    scanf("%d", &n);

    dll_compress(&head, n);
    dll_print(head);
    printf("Max number of duplicates: %d\n", dll_max_duplicate(head));

    dll_remove_all(&head);
    dll_print(head);
    printf("Max number of duplicates: %d\n", dll_max_duplicate(head));

}
