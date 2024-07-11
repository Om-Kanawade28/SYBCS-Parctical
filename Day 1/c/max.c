#include<stdio.h>
void max(int n1,int n2){
    if(n1<n2){
        printf("%d is maximum",n2);

    }
    else{
        printf("%d is maximum",n1);
    }
}
int main(){
    int n1,n2;
    printf("Enter the numbers to cheak the max in the two numbers:-");
    scanf("%d%d",&n1,&n2);
    max(n1,n2);
    return 0;
}