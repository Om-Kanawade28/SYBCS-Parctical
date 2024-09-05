
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