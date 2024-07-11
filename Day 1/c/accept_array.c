#include<stdio.h>
int main()
{
    int a[100],n;
    printf("Enter how many element want to accept:-");
    scanf("%d",&n);
    printf("Enter the Element:-");
    for(int i = 0;i < n;i++){
       scanf("%d",&a[i]);
    }
    printf("the given array is:-");
    for(int i = 0;i < n;i++){
       printf("%d",a[i]);
    }
return 0;
}