#include<stdio.h>
struct node{
    int data;
    struct node *next;
};
int main(){
    struct node *head,*newnode,*tail;
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
    }

    return 0;
}