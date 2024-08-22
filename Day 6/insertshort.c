#include<stdio.h>
void insertshort(int a[], int n) {
    int i, j, key;

    for (i = 1; i < n; i++) {
        key = a[i];
        for (j = i - 1; j >= 0 && key < a[j]; j--) {
            a[j + 1] = a[j];
        }
        a[j + 1] = key;
    }
}

int main(){
int a[200],i,n;
printf("Enter the size of Array:-");
scanf("%d",&n);
printf("\nEnter the array:-");
for(i = 0;i < n;i++){
    scanf("%d",&a[i]);
}
insertshort(a,n);
printf("Your shorted array:-");
for(i = 0;i<n;i++){
    printf("%d ->",a[i]);
}
    return 0;
}