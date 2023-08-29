import timeit
# from QuickSort_in_c import quickSort
from ctypes import CDLL, Array, c_int


# Initializing the c file
path = "C:\\mycode\\python\\Data Structures\\AAT ADA\\QuickSort_in_c.so"
calling_c_function = CDLL(path)


def hashFunction(strings):
    final = []
    new_dict = {}
    # ming = min([len(st) for st in strings])
    ming = len(min(strings, key=len))
    for st in strings:
        offset = (ord(st[0].casefold()) - 97)
        fin = sum([ord(i.casefold()) for j,
                  i in enumerate(st) if j < ming + offset]) + offset*offset
        final.append(fin)
        new_dict[fin] = st
    return final, new_dict


def printArray(array, newDict):
    for i in array:
        print(newDict.get(i))
    print()


def main():
    array = ["Yashasvini", "Apple", "Ahamed", "badedzimmer", "risha"]
    newArray, newDict = hashFunction(array)
    # print(newArray)
    # print(newDict)
    arr = (c_int * len(newArray))(*newArray)
    calling_c_function.quickSort.argtypes = [Array, c_int]
    calling_c_function.quickSort(arr, 0, len(array) - 1)
    printArray(arr, newDict)


start = timeit.default_timer()
main()
stop = timeit.default_timer()
execution_time = stop - start
# It returns time in seconds
print(f"Program Executed in {str(execution_time)} seconds")
