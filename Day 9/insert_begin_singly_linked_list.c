#include<stdio.h>
#include<stdlib.h>
struct node{
    int data;
    struct node *next;
};
int main(){
    struct node *newnode,*head,*tail;
    head = NULL;
    newnode = (struct node *)malloc(sizeof(struct node));
    newnode -> next = NULL;
    if( head == NULL){
        head = newnode;
        tail = newnode;
    }
    return 0;
}