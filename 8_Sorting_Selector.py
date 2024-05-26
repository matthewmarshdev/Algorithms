#import methods

import random
import time
 
algorithms=['Selection', 'Quick', 'Bubble']

rand_big_list=[]
n=1000
for i in range(n):
    rand_big_list.append(random.randint(1,1000))
print('Large List, 1000 Integers ', rand_big_list)
 
rand_small_list=[]
n=100
for i in range(n):
    rand_small_list.append(random.randint(3,9))
print('Small List, 1000 Integers ',rand_small_list)

 
def createList(r1, r2):
    return [item for item in range(r1, r2+1)]
     
r1, r2 = 1, 1000
print('Big list, ordered except for first and last value', createList(r1, r2))

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
print('The array after sorting in Ascending Order by selection sort is:')
print(rand_big_list)
endSelect = time.time()

print("The time of execution of SelectSort is :",
      (endSelect-startSelect) * 10**3, "ms")

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

    print("Sorted array using bubble sort:")
    for i in range(len(arr)):
        print("%d" % arr[i], end=" ")

endBubble = time.time()

print("The time of execution of Bubble Sort is :",
      (endBubble-startBubble) * 10**3, "ms")

# Python3 implementation of QuickSort
# Function to find the partition position
def partition(array, low, high):

    # Choose the rightmost element as pivot
    pivot = array[high]

    # Pointer for greater element
    i = low - 1

    # Traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:

            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1

            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])

    # Swap the pivot element with
    # the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    # Return the position from where partition is done
    return i + 1

# Quicksort
def quicksort(array, low, high):
    if low < high:

        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)

        # Recursive call on the left of pivot
        quicksort(array, low, pi - 1)

        # Recursive call on the right of pivot
        quicksort(array, pi + 1, high)

if __name__ == '__main__':
    array = rand_big_list
    N = len(array)

    # Function call
    quicksort(array, 0, N - 1)
    print('Quick Sorted array:')
    for x in array:
        print(x, end=" ")




# This code is modified by Suraj krushna Yadav


#instantiate the UI with pop-up, loading input window
#add help language in the UI

#ask user to input a series of numbers (can be 3 numbers or up to 100000)
#Click a run method in the UI

#Add list variable from input into method 1 (Selection Sort)
#output should be a sorted list and time from start to finish

#Add list variable from input into method 1 (Shell Sort)
#output should be a sorted list and time from start to finish

#Add list variable from input into method 1 (Quick Sort)
#output should be a sorted list and time from start to finish

#put all 3 method outputs in a table with the following columns:
#Sort Algorithm Name, Original List, Sorted List, Time to Sort, Time Variable

#Render the Table in the UI
#Render a new button in the UI: Clear Table
#Render a new button in the UI: See Logs
#Render a new button in the UI: Ask GPT?

#If user clicks Clear Table, reset list variable, derender table, wipe API response
#If user clicks See Logs, open file that shows each iteration performed in each method
#If user clicks Ask GPT, use OpenAI API to send following Prompt:
#"What sorting algorithm would be best to use to sort the following list:" + ListVar
#Display and render response from API 