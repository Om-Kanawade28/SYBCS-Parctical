#include<stdio.h>
int main()
{
    int a[100],n,j;
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
    printf("\n the reverse array:-");
    for( j = n-1;j >=0;j--){
       printf("%d",a[j]);
    }
  


return 0;
}