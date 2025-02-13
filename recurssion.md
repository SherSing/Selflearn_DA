# We will follow recurssion exercise later

Write a algorithm to Sort this list

list_A =[30, 249, 264, 115, 167, 475, 386, 308, 319, 193, 232, 406, 376, 236, 471, 12, 146, 419, 411, 280, 74, 151, 18, 190, 196, 335, 322, 402, 51, 369, 354, 362, 70, 12, 374, 316, 389, 168, 90, 136, 372, 172, 89, 284, 147, 410, 255, 130, 486, 377]


def mergeSort(arr, l, r):
    if l < r:
 
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l+(r-l)//2
 
        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)