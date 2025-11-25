#include <stdio.h>
#include <stdlib.h>

// Define the Node structure
typedef struct Node {
    int data;
    struct Node* next;
} Node;

// Function to print the linked list
void printList(Node* head) {
    Node* current = head;
    while (current != NULL) {
        printf("Data = %d\n", current->data);
        current = current->next;
    }
}

// Function to remove duplicate nodes from the list
void removeDuplicates(Node* head) {
    Node* current = head;
    Node* copy = (Node*) malloc(sizeof(Node));
    while(current != NULL){
        Node* newNode = 
        copy->data = current->data;

    }

    while (current != NULL && current->next != NULL) {
        if (current->data == current->next->data) {
            Node* temp = current->next;
            current->next = current->next->next;
            free(temp);
        } else {
            current = current->next;
        }
    }
}

// Function to remove every other node from the list
void removeEveryOtherNode(Node* head) {
    int count = 1;
    Node* current = head;
    Node* previous = NULL;

    while (current != NULL) {
        if (count % 2 == 0) {
            previous->next = current->next;
            Node* temp = current;
            current = current->next;
            free(temp);
        } else {
            previous = current;
            current = current->next;
        }
        count++;
    }
}

void removeEveryKNode(Node* head, int k) {
    if (k <= 1 || head == NULL) return;

    Node* current = head;
    Node* prev = NULL;
    int count = 1;

    while (current != NULL) {
        if (count % k == 0) {
            // Remove current node
            Node* temp = current;
            if (prev != NULL) {
                prev->next = current->next;
            }
            current = current->next;
            free(temp);
        } else {
            prev = current;
            current = current->next;
        }
        count++;
    }
}


// Function to free the entire linked list
void freeList(Node* head) {
    Node* current = head;
    while (current != NULL) {
        Node* temp = current;
        current = current->next;
        free(temp);
    }
}

// Main function
int main() {
    // Initialize the linked list
    Node* head = (Node*)malloc(sizeof(Node));
    head->data = 0;
    head->next = NULL;

    int user = 1, count = 0;
    while (user) {
        printf("Enter a number: ");
        int num = 0;
        scanf("%d", &num);

        if (count == 0) {
            head->data = num;
        } else {
            Node* current = head;
            while (current->next != NULL) {
                current = current->next;
            }
            Node* newNode = (Node*)malloc(sizeof(Node));
            newNode->data = num;
            newNode->next = NULL;
            current->next = newNode;
        }
        count++;

        printf("\nWould you like to enter another node? (1) yes, (0) no: ");
        scanf("%d", &user);
    }

    // Print the initial list
    printf("Initial list:\n");
    printList(head);

    // Remove every other node
    printf("After getting rid of every other node:\n");
    removeEveryOtherNode(head);
    printList(head);

    // Remove duplicates from the list
    printf("After removing duplicates:\n");
    removeDuplicates(head);
    printList(head);

    // Free the list
    freeList(head);

    return 0;
}