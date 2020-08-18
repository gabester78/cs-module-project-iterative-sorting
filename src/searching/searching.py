def linear_search(arr, target):
    # Your code here

    # looping starting from index[0]
    for i in range(len(arr)):

        # if index matches our target arguement
        if arr[i] == target:

            # return the target index
            return i

    # placeholder to say target wasn't found (almost same as None)
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    # var to start our search
    low = 0

    # var from end of the array
    high = len(arr) - 1

    # loops through the array while our low var is less than or equal to our high var
    while low <= high:

        # finds the middle of the array - // 2 would round down any intger numbers
        middle = (low + high) // 2

        # sets the middle of the array to begin the binary search
        guess = arr[middle]

        # if guess is equal to the middle of the array, the middle value is returned
        if guess == target:
            return middle

        # if middle of array is higher than the target, the right side of the array is eliminated from the search
        if guess > target:
            high = middle - 1

        # otherwise the lower half of the array is eliminated from the search
        else:
            low = middle + 1
    return -1  # not found
