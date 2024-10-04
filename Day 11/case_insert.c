#include<stdio.h>
#include<stdlib.h>
struct node{
    int data;
    struct node *next;
};
int main(){
int help;
int ch=1;
struct node *head,*newnode,*tail,*temp,*insert;
head = NULL;
int pos,i = 2;
int choice = 1;
while(ch){
printf("\n**********MENU*********\n");
printf("1.create linked list\n2.display linked list\n3.insert begin\n4.insert end\n5.insert specific\n");
printf("Enter the choice:-");
scanf("%d",&help);
printf("do you want to cotinue(0,1)?");
scanf("%d",&ch);


switch (help)
{
case 1:printf("create linked list:-\n");
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
    break;
case 2:printf("\nDisplay Linked list:-");
    printf("\nYour Linked List:-");
    temp = head;
    while(temp != NULL){
        printf("%d -> ",temp -> data);
        temp = temp -> next;
    }
    printf("NULL");
    break;
case 3:printf("\nInsert at begin:-");
    printf("\nYour Linked List:-");
    temp = head;
    while(temp != NULL){
        printf("%d -> ",temp -> data);
        temp = temp -> next;
    }
    //insert the beginning
    insert = (struct node *)malloc(sizeof(struct node));
    printf("\nEnter the insert data at begin:-");
    scanf("%d",&insert -> data);
    insert -> next = head;
    head = insert;

    printf("\nAfter insert linked list:-");
    temp = head;
    while(temp != NULL){
        printf("%d -> ",temp -> data);
        temp = temp -> next;
    }
    break;
case 4:printf("\nInsert at End:-");
    printf("\nYour Linked List:-");
    temp = head;
    while(temp != NULL){
        printf("%d -> ",temp -> data);
        temp = temp -> next;
    }
    printf("NULL");
    printf("\nEnter the data at end position:-");
    insert = (struct node*)malloc(sizeof(struct node));
    scanf("%d",&insert -> data);
    tail -> next = insert;
    insert -> next = NULL;
    tail = insert;

    printf("\nafter insert at end Linked List:-");
    temp = head;
    while(temp != NULL){
        printf("%d -> ",temp -> data);
        temp = temp -> next;
    }
    printf("NULL");
    break;
case 5:printf("\nInsert at specific Position:-");
    insert = (struct node *)malloc(sizeof(struct node));
    printf("\n specific position:-");

    printf("\nEnter the data:-");
    scanf("%d", &insert->data);
    printf("Enter the position:-");
    scanf("%d", &pos);
        temp = head;
    while (i != pos)
    {
        temp = temp->next;
        i++;
    }
    insert->next = temp->next;
    temp->next = insert;
    printf("\n The Linked List after specific insert:-");

    temp = head;
    while (temp != NULL)
    {
        printf("%d ->", temp->data);
        temp = temp->next;

    }
    printf("NULL");
    break;

default:
    break;
}
}
    return 0;
}