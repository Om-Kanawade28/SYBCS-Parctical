#include<stdio.h>
int main(){
    int a[10],n,i,j,max,loc,temp;
    printf("Enter the size of array:-");
    scanf("%d",&n);
    printf("\nEnter the Array:-");
    for(i = 0; i < n; i++){
        scanf("%d",&a[i]);
    }
    for(i = 0;i < n; i++){
        max = a[i];
        loc = i;
        for(j = i + 1;j < n; j++){
            if(max < a[j]){
                max = a[j];
                loc = j;
            }
        }
        temp = a[i];
        a[i] = max;
        a[loc] = temp;
    }
    for(i = 0;i < n; i++){
        printf("%d ->",a[i]);
    }
    return 0;
}