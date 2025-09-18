#different arrays
def find_uniq(arr):
    first = arr[0]
    list_length = len(arr)
    i = 1
    while i < list_length:
        if arr[i] != first:
            # If the odd one out is at index i
            if i + 1 < list_length and arr[i] == arr[i + 1]:
                return first
            else:
                return arr[i]
        i += 1
