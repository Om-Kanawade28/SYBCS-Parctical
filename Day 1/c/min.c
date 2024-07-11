#include<stdio.h>
void min(int n1,int n2){
    if(n1<n2){
        printf("%d is minimum",n1);
    }
    else{
        printf("%d is minimum",n2);
    }
}
int main(){
   int n1,n2;
   printf("Enter  the Number to check the min :-");
   scanf("%d%d",&n1,&n2);
   min(n1,n2);
    return 0;
}