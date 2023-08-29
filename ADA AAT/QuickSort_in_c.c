#include<stdio.h>


void swap(int *a, int *b){
    int t = *a;
    *a = *b;
    *b = t;
}

int hoarePartition(int a[], int low, int high){
    int pivot = a[low], i = low - 1, j = high + 1;
    
    while(1){

        do {
            i++;
        }while(a[i] < pivot);


        do{
            j--;
        }while(a[j] > pivot);

        if(i >= j)
            return j;
        

        swap(&a[i], &a[j]);
    }
    return 0;
}


int quickSort(int a[], int low, int high){
    int pivot;
    if(low < high){
        pivot = hoarePartition(a, low, high);
        quickSort(a, low, pivot);
        quickSort(a, pivot + 1, high);
    }
    return 0;
}

int printArray(int a[], int n){
    for(int i = 0; i< n; i++)
        printf("%d ", a[i]);
    printf("\n");
    return 0;
}

int main(){
    int a[] = {5, 6 ,2, 5, 1}, low = 0, high = 5; 
    quickSort(a, low, high);
    printArray(a, 5);
    return 0;
}


