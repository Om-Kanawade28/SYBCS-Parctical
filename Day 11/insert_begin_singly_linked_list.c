#include<stdio.h>
#include<stdlib.h>
struct node{
    int data;
    struct node *next;
};
int main(){
    struct node *newnode,*head,*tail,*temp,*insert;
    head = NULL;
    int choice = 1;
    while(choice){
    newnode = (struct node *)malloc(sizeof(struct node));
    printf("Enter the data:-");
    scanf("%d",&newnode -> data);
    newnode -> next = NULL;
    if( head == NULL){
        head = newnode;
        tail = newnode;
    }else{
        tail -> next = newnode;
        tail = newnode;
    }
    printf("\nDo you want to Continue(0,1)?");
    scanf("%d",&choice);
    }
    printf("\nYour Linked List:-");
    temp = head;
    while(temp != NULL){
        printf("%d -> ",temp -> data);
        temp = temp -> next;
    }
    //insert the beginning
    insert = (struct node *)malloc(sizeof(struct node));
    printf("\nEnter the insert data:-");
    scanf("%d",&insert -> data);
    insert -> next = head;
    head = insert;

    printf("\nAfter insert linked list:-");
    temp = head;
    while(temp != NULL){
        printf("%d -> ",temp -> data);
        temp = temp -> next;
    }
    return 0;
}