# Create a list of unsorted values
numbers = [61, 76, 19, 4, 94, 32, 27, 83, 58]
numbers2 = [1, 3, 4, 56, 54, 344, 1254535, 4456, 7, 2, 45, 46, 47, 48, 87, 36, 61, 76, 19, 4, 94, 32, 27, 83, 58]

#Merge Sort
def merge(numbers, i, j, k):
    merged_size = k - i + 1               # Size of merged partition
    merged_numbers = [0] * merged_size    # Dynamically allocates temporary array
                                          # for merged numbers
    merge_pos = 0                         # Position to insert merged number
    left_pos = i                          # Initialize left partition position
    right_pos = j + 1                     # Initialize right partition position
   
    # Add smallest element from left or right partition to merged numbers
    while left_pos <= j and right_pos <= k:
        if numbers[left_pos] <= numbers[right_pos]:
            merged_numbers[merge_pos] = numbers[left_pos]
            left_pos += 1
        else:
            merged_numbers[merge_pos] = numbers[right_pos]
            right_pos += 1
        merge_pos = merge_pos + 1
   
    # If left partition is not empty, add remaining elements to merged numbers
    while left_pos <= j:
        merged_numbers[merge_pos] = numbers[left_pos]
        left_pos += 1
        merge_pos += 1
   
    # If right partition is not empty, add remaining elements to merged numbers
    while right_pos <= k:
        merged_numbers[merge_pos] = numbers[right_pos]
        right_pos = right_pos + 1
        merge_pos = merge_pos + 1
   
    # Copy merge number back to numbers
    for merge_pos in range(merged_size):
        numbers[i + merge_pos] = merged_numbers[merge_pos]


def merge_sort(numbers, i, k):
    j = 0

    if i < k:
        j = (i + k) // 2  # Find the midpoint in the partition

        # Recursively sort left and right partitions
        merge_sort(numbers, i, j)
        merge_sort(numbers, j + 1, k)
            
        # Merge left and right partition in sorted order
        merge(numbers, i, j, k)




#BubbleSort

def bubbleSort(numbers2):
    n = len(numbers2)
    
    # Traverse through all array elements
    for i in range(n):
        swapped = False

        # Last i elements are already in place
        for j in range(0, n-i-1):

            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if numbers2[j] > numbers2[j+1]:
                numbers2[j], numbers2[j+1] = numbers2[j+1], numbers2[j]
                swapped = True
        if (swapped == False):
            break


# Driver code to test above
if __name__ == "__main__":
    numbers2 

    bubbleSort(numbers2)

    print("SORTED VIA BUBBLE:")
    for i in range(len(numbers2)):
        print("%d" % numbers2[i], end=" ")

# Print unsorted list
print('UNSORTED DATA:', numbers2)

# Initial call to merge_sort
merge_sort(numbers2, 0, len(numbers2) - 1)

# Print sorted list
print('SORTED VIA MERGE:', numbers2)