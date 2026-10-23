"""Binary search and its variants.

Topic: Searching
Works on: SORTED data only
Time:  best O(1), worst O(log n), average O(log n)
Space: iterative O(1), recursive O(log n) because of the call stack
Why log n: n / 2^k <= 1  =>  k >= log2(n)
"""

NOT_FOUND = -1


def binary_search(arr, target):
    """Iterative binary search. Return the index of target, or NOT_FOUND."""
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2      # avoids overflow of low + high
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1                  # target is in the right half
        else:
            high = mid - 1                 # target is in the left half
    return NOT_FOUND


def binary_search_recursive(arr, target, low=0, high=None):
    """Recursive version. Call it as binary_search_recursive(arr, target)."""
    if high is None:
        high = len(arr) - 1
    if low > high:                         # base case: empty range
        return NOT_FOUND
    mid = low + (high - low) // 2
    if arr[mid] == target:                 # base case: found
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)


def first_occurrence(arr, target):
    """Index of the first copy of target (sorted array with duplicates)."""
    low, high, answer = 0, len(arr) - 1, NOT_FOUND
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            answer = mid                   # remember it, keep looking left
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return answer


def last_occurrence(arr, target):
    """Index of the last copy of target."""
    low, high, answer = 0, len(arr) - 1, NOT_FOUND
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            answer = mid                   # remember it, keep looking right
            low = mid + 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return answer


def count_occurrences(arr, target):
    """How many times target appears. Time O(log n)."""
    first = first_occurrence(arr, target)
    if first == NOT_FOUND:
        return 0
    return last_occurrence(arr, target) - first + 1


def insertion_position(arr, target):
    """Index where target is, or where it would be inserted to keep order."""
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return low                             # low is the insertion point


def binary_search_trace(arr, target):
    """Print a low / high / mid table. Use it to practise dry runs."""
    low, high = 0, len(arr) - 1
    print(f"{'low':>4} {'high':>4} {'mid':>4} {'arr[mid]':>9}  action")
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            print(f"{low:>4} {high:>4} {mid:>4} {arr[mid]:>9}  found")
            return mid
        elif arr[mid] < target:
            print(f"{low:>4} {high:>4} {mid:>4} {arr[mid]:>9}  go right, low = {mid + 1}")
            low = mid + 1
        else:
            print(f"{low:>4} {high:>4} {mid:>4} {arr[mid]:>9}  go left, high = {mid - 1}")
            high = mid - 1
    print(f"{low:>4} {high:>4}                low > high, not found")
    return NOT_FOUND


if __name__ == "__main__":
    data = [4, 9, 13, 18, 24, 31, 37, 42, 56]
    assert binary_search(data, 31) == 5
    assert binary_search(data, 5) == NOT_FOUND
    assert binary_search([], 1) == NOT_FOUND
    assert binary_search_recursive(data, 31) == 5
    assert binary_search_recursive(data, 5) == NOT_FOUND

    dup = [1, 2, 2, 2, 3, 5, 5]
    assert first_occurrence(dup, 2) == 1
    assert last_occurrence(dup, 2) == 3
    assert count_occurrences(dup, 2) == 3
    assert count_occurrences(dup, 4) == 0

    assert insertion_position([1, 3, 5, 6], 5) == 2
    assert insertion_position([1, 3, 5, 6], 2) == 1
    assert insertion_position([1, 3, 5, 6], 7) == 4
    assert insertion_position([1, 3, 5, 6], 0) == 0

    binary_search_trace(data, 31)
    print("binary search: all tests passed")
