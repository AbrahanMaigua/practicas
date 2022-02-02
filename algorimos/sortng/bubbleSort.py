def bubleSort(Array):
    """
    notyacion  O(n²).
    """
    for i in range(len(Array) ): # o(1)
        for j in range(0, len(Array) - i - 1): # o(1)
           # print( Array[j], Array[j+1])
            if Array[j] > Array[j+1]:
                Array[j], Array[j+1] = Array[j+1], Array[j]


def bubble_sort(Array):
    swa = True
    while(swa):
        swa = False
        for i in range(len(Array)):
            for j in range(0, len(Array) - i - 1):
                Array[j], Array[j+1] = Array[j+1], Array[j]
                swa = False
def SelectionSort(Array):
    """es igual al alterio lo unico es que
    diveide en dos parte la que esta ordenada y la desordenada
    # nitacion O(n²)
    """
    for i in range(len(Array)):
        minimo = i 
        for j in range(i+1, len(Array)):
            if Array[minimo] > Array[j]:
                minimo = j
        Array[i], Array[minimo] =  Array[minimo], Array[i]



def mergeSort(array):
    if len(array) > 1:

        #  r is the point where the array is divided into two subarrays
        r = len(array)//2
        L = array[:r]
        M = array[r:]

        # Sort the two halves
        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1


# Print the array
def printList(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()


# Driver program    array = [6, 5, 12, 10, 9, 1]

    mergeSort(array)

    print("Sorted array is: ")
    printList(array)