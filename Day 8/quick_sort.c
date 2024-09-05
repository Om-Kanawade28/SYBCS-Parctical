#include<stdio.h>
void quicksort(int [ ], int, int);
void main(){
    int low,high,pivot,t,n,i,j,a[10];
    printf("\n How many elements you want to start");
    scanf("%d", &n);
    printf("\n Enter elements for array:-");
    for(i = 0;i < n;i++){
        scanf("%d",&a[i]);
    }
    low = 0;
    high = n -1;
    quiksort(a,low,high);
    printf("\n After sorting the elements are:-\n");
    for(i = 0;i < n;i++){
        printf("%d\n",a[i]);
    }

void quicksort(int a[],int low,int high)

}