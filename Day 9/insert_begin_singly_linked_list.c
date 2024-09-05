#include<stdio.h>
#include<stdlib.h>
struct node{
    int data;
    struct node *next;
};
int main(){
    struct node *newnode,*head,*tail;
    head = NULL;
    int choice = 1;
    while(choice){
    newnode = (struct node *)malloc(sizeof(struct node));
    newnode -> next = NULL;
    if( head == NULL){
        head = newnode;
        tail = newnode;
    }else{
        tail -> next = newnode;
        tail = newnode;
    }
    printf("\nDo you want to Continue(0,1)?");
    scamf("%d",&choice);
    }
    printf("\n")
    return 0;
}