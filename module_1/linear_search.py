"""Linear search (iterative and recursive).

Topic: Searching
Works on: any order (sorted or unsorted)
Time:  best O(1), worst O(n), average O(n)
Space: iterative O(1), recursive O(n) because of the call stack
"""

NOT_FOUND = -1


def linear_search(arr, target):
    """Return the index of target in arr, or NOT_FOUND."""
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return NOT_FOUND


def linear_search_recursive(arr, target, i=0):
    """Recursive version. Call it as linear_search_recursive(arr, target)."""
    if i == len(arr):                 # base case: ran out of elements
        return NOT_FOUND
    if arr[i] == target:              # base case: found
        return i
    return linear_search_recursive(arr, target, i + 1)


if __name__ == "__main__":
    data = [11, 7, 18, 23, 5]
    assert linear_search(data, 23) == 3
    assert linear_search(data, 99) == NOT_FOUND
    assert linear_search([], 1) == NOT_FOUND
    assert linear_search_recursive(data, 23) == 3
    assert linear_search_recursive(data, 99) == NOT_FOUND
    print("linear search: all tests passed")
