print("Algorithms file loaded")
#---------------------------------------------BUBBLE SORT-----------------------------------------------------------
def bubblesort(arr_to_be_sorted):

    swap_happened = True
    while swap_happened:
        swap_happened = False
        for num in range(len(arr_to_be_sorted) - 1):
            if arr_to_be_sorted[num] > arr_to_be_sorted[num + 1]:
                arr_to_be_sorted[num], arr_to_be_sorted[num + 1] = arr_to_be_sorted[num + 1], arr_to_be_sorted[num]
                swap_happened = True

    return arr_to_be_sorted

#-------------------------------------------SELECTION SORT----------------------------------------------------------
def selectionsort(arr_to_be_sorted):

    spot_marker = 0
    while spot_marker < len(arr_to_be_sorted):
        for num in range(spot_marker, len(arr_to_be_sorted)):
            if arr_to_be_sorted[num] < arr_to_be_sorted[spot_marker]:
                arr_to_be_sorted[num], arr_to_be_sorted[spot_marker] = arr_to_be_sorted[spot_marker], arr_to_be_sorted[num]
        spot_marker += 1
    return arr_to_be_sorted

#--------------------------------------------INSERTON SORT-----------------------------------------------------------
def insertionsort(arr_to_be_sorted):

    for key in range(1, len(arr_to_be_sorted)):
        for working_key in range(key - 1):
            if arr_to_be_sorted[key] < arr_to_be_sorted[working_key]:
                arr_to_be_sorted[key], arr_to_be_sorted[working_key] = arr_to_be_sorted[working_key], arr_to_be_sorted[key]
    return arr_to_be_sorted

#------------------------------------------------MERGE SORT----------------------------------------------------------
def merge_sort(arr1, arr2):

    # print("Merge function called with 2 lists below:")
    # print(f"Left : {arr1} and Right : {arr2}")
    sorted_arr = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            sorted_arr.append(arr1[i])
            i += 1
        else:
            sorted_arr.append(arr2[j])
            j += 1
        # print(sorted_arr)
    while i < len(arr1):
        sorted_arr.append(arr1[i])
        i += 1
    while j < len(arr2):
        sorted_arr.append(arr2[j])
        j += 1
    return sorted_arr

def mergesort(arr_to_be_sorted):
    if len(arr_to_be_sorted) < 2:
        # print(f"Base consition reached with : {arr_to_be_sorted[ : ]}")
        return arr_to_be_sorted[ : ]
    else:
        middle = len(arr_to_be_sorted) // 2
        # print("Left : ", arr_to_be_sorted[ : middle])
        # print("Right : ", arr_to_be_sorted[middle : ])
        l1 = mergesort(arr_to_be_sorted[ : middle])
        l2 = mergesort(arr_to_be_sorted[middle : ])
        return merge_sort(l1, l2)

#-------------------------------------------------QUICK SORT---------------------------------------------------------
def quicksort(arr_to_be_sorted):

    if len(arr_to_be_sorted) < 2:
        return arr_to_be_sorted
    else:
        pivot = arr_to_be_sorted[-1]
        smaller, equal, larger = [], [], []
        for num in arr_to_be_sorted:
            if num < pivot:
                smaller.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                larger.append(num)
        return quicksort(smaller) + equal + quicksort(larger)
