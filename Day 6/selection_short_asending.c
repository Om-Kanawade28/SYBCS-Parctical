#include<stdio.h>
int main(){
    int a[10],i,j,loc,temp,min,n;
    printf("\nEnter the size of array:-");
    scanf("%d",&n);
    printf("\n Enter the array:-");
    for(i = 0;i < n;i++){
        scanf("%d",&a[i]);
    }
    for(i = 0;i < n; i++){
        min = a[i];
        loc = i;
        for(j = i + 1; j < n;j++){
            if(min > a[j]){
                min = a[j];
                loc = j;
            }

        }
        temp = a[i];
        a[i] = min;
        a[loc] = temp;
    }
    printf("\nYour shorted array:-");
    for(i = 0;i < n;i++){
        printf("%d ->",a[i]);
    }
    return 0;
}