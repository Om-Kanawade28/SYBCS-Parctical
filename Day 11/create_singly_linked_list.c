#include<stdio.h>
#include<stdlib.h>
struct node{
    int data;
    struct node *next;
};
int main(){
    struct node *head,*newnode,*tail,*temp;
    head = NULL;
    int choice = 1;
    while(choice){
    newnode = (struct node *)malloc(sizeof(struct node));
    printf("Enter the Data:-");
    scanf("%d",&newnode -> data);
    newnode -> next = NULL;
    if(head == NULL){
    head = newnode;
    tail = newnode;
    }else{
         tail -> next = newnode;
         tail = newnode;
     }
     printf("\nDo you want to continue(0,1)?");
     scanf("%d",&choice);
    }
    printf("\nYour Linked List:-");
    temp = head;
    while(temp != NULL){
        printf("%d -> ",temp -> data);
        temp = temp -> next;
    }
    printf("NULL");
    return 0;
}