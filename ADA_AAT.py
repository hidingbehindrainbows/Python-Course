def hoarePartition(array, low, high):
    pivot = array[low]
    i = low - 1
    j = high + 1
    
    while True:
        i += 1
        while array[i] < pivot:
            i += 1

        j -= 1
        while array[j] > pivot:
            j -= 1

        if i >= j:
            return j
 
        array[i], array[j] = array[j], array[i]



def quickSort(array, low, high):
    
    if low < high:
        pivot = hoarePartition(array, low, high)
        quickSort(array, low, pivot)
        quickSort(array, pivot + 1, high)


def printArray(array):
    [print(v, end=" ") for v in array]
    print()


def main():
    inp = input("Please enter the title or the author of the book:\n")
    array = list(inp)
    array = inp.split(" ")
    quickSort(array, 0, len(array) - 1)
    printArray(array)

main()
