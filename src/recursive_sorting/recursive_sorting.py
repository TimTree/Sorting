# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    # merged_arr = [0] * elements
    merged_arr = []
    # TO-DO
    arrAClone = arrA.copy()
    arrBClone = arrB.copy()
    while True:
        if len(arrBClone) == 0:
            merged_arr.append(arrAClone[0])
            arrAClone.pop(0)
        elif len(arrAClone) == 0:
            merged_arr.append(arrBClone[0])
            arrBClone.pop(0)
        elif arrAClone[0] < arrBClone[0]:
            merged_arr.append(arrAClone[0])
            arrAClone.pop(0)
        else:
            merged_arr.append(arrBClone[0])
            arrBClone.pop(0)
        if not arrAClone and not arrBClone:
            break
    return merged_arr




# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        left, right = merge_sort(arr[:len(arr)//2]), merge_sort(arr[len(arr)//2:])
        print(left, right)
    return merge(left, right)


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr


theArray = [9, 5, 7, 1, 3, 6, 4, 2, 8]

merge_sort(theArray)