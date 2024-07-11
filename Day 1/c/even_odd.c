#include<stdio.h>
void even_odd(int no){

     if(no%2==0){
        printf("%d is even",no);
     }else{
        printf("%d is odd",no);
     }
}
int main()
{
     int no;
     printf("Enter the Number to check the even and odd:-");
     scanf("%d",&no);
     even_odd(no);
    return 0;
}