#import methods

import random
import time
 
algorithms=['Selection', 'Quick', 'Bubble']



lowRange = int(input("Enter lowest number for dataset:"))
highRange = int(input("Enter highest number for dataset:"))
numberOfIntegers = int(input("Enter the number of integers in the dataset:"))

rand_big_list=[]
n=numberOfIntegers
for i in range(n):
    rand_big_list.append(random.randint(lowRange,highRange))
print('Large List, 1000 Integers ', rand_big_list)
 
rand_small_list=[]
n=100
for i in range(n):
    rand_small_list.append(random.randint(1,50))
print('Small List, 50 Integers ',rand_small_list)

staticList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
              21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
              40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59,
              60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70]

def createList(r1, r2):
    return [item for item in range(r1, r2+1)]
     
r1, r2 = 1, 1000
#print('Big list, ordered except for first and last value', createList(r1, r2))

# Selection sort in Python
#if algorithms == 'Selection':
startSelect = time.time()
def selectionSort(rand_big_list, size):
    
    for ind in range(size):
        min_index = ind

        for j in range(ind + 1, size):
            # select the minimum element in every iteration
            if rand_big_list[j] < rand_big_list[min_index]:
                min_index = j
        # swapping the elements to sort the array
        (rand_big_list[ind], rand_big_list[min_index]) = (rand_big_list[min_index], rand_big_list[ind])

size = len(rand_big_list)
selectionSort(rand_big_list, size)
#print('The array after sorting in Ascending Order by selection sort is:')
#print(rand_big_list)
endSelect = time.time()
selectTime = (endSelect-startSelect)
# Optimized Python program for implementation of Bubble Sort

startBubble = time.time()
def bubbleSort(arr):
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        swapped = False

        # Last i elements are already in place
        for j in range(0, n-i-1):

            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if (swapped == False):
            break

# Driver code to test above for Bubble Sort
if __name__ == "__main__":
    arr = rand_big_list

    bubbleSort(arr)

#    print("Sorted array using bubble sort:")
#    for i in range(len(arr)):
#        print("%d" % arr[i], end=" ")

endBubble = time.time()
bubbleTime = (endBubble-startBubble)

# Python3 implementation of QuickSort
startQuick = time.time()
def quicksort(x):
    if len(x) == 1 or len(x) == 0:
        return x
    else:
        pivot = x[0]
        i = 0
        for j in range(len(x)-1):
            if x[j+1] < pivot:
                x[j+1],x[i+1] = x[i+1], x[j+1]
                i += 1
        x[0],x[i] = x[i],x[0]
        first_part = quicksort(x[:i])
        second_part = quicksort(x[i+1:])
        first_part.append(x[i])
        return first_part + second_part
        
alist = rand_small_list
quicksort(alist)
#print("quick sort", alist)
endQuick = time.time()
quickTime = (endQuick-startQuick)

print("The time of execution of Selection Sort is :",
      (selectTime) * 10**3, "ms")

print("The time of execution of Bubble Sort is :",
      (bubbleTime) * 10**3, "ms")

print("The time of execution of QuickSort is :",
      (quickTime) * 10**3, "ms")

print("The time of execution of all methods for this Run is :",
      (selectTime + quickTime + bubbleTime) * 10**3, "ms")

if selectTime < (bubbleTime and quickTime):
    print("Selection Sort:", selectTime, ", was faster than Quick Sort and Bubble Sort for this data set")
elif bubbleTime < (selectTime and quickTime):
    print("Bubble Sort with a time of:", bubbleTime, " was faster than Quick Sort and Selection Sort for this data set")
else:     
    print("Quick Sort with a time of:", quickTime, " was faster than Quick Sort and Bubble Sort for this data set")
 
