"""Basic data-structure operations on an array (Python list).

Topic: Operations (traversal, access, update, insertion, deletion, merging)
Insertion and deletion shift elements by hand to show where the cost comes from.
"""


def traverse(arr):
    """Visit every element once. Time O(n)."""
    for x in arr:
        print(x)


def total(arr):
    """Traversal that computes a sum. Time O(n), space O(1)."""
    s = 0
    for x in arr:
        s += x
    return s


def access(arr, index):
    """Read arr[index]. Time O(1)."""
    return arr[index]


def update(arr, index, value):
    """Change arr[index]. Time O(1)."""
    arr[index] = value


def insert_at(arr, index, value):
    """Insert value at index by shifting elements right.

    Time: O(n) in the worst case (index 0), O(1) at the end.
    """
    if index < 0 or index > len(arr):
        raise IndexError("index out of range")
    arr.append(None)                       # make room at the end
    for i in range(len(arr) - 1, index, -1):
        arr[i] = arr[i - 1]                # shift right
    arr[index] = value


def delete_at(arr, index):
    """Delete and return arr[index] by shifting elements left.

    Time: O(n) in the worst case (index 0), O(1) at the end.
    """
    if index < 0 or index >= len(arr):
        raise IndexError("index out of range")
    removed = arr[index]
    for i in range(index, len(arr) - 1):
        arr[i] = arr[i + 1]                # shift left
    arr.pop()                              # drop the duplicate last slot
    return removed


def merge_sorted(a, b):
    """Merge two sorted lists into one sorted list.

    Time O(n + m), space O(n + m).
    """
    result = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])                   # one of these is empty
    result.extend(b[j:])
    return result


if __name__ == "__main__":
    assert total([8, 4, 9, 2, 7, 5]) == 35
    assert access([5, 6, 7], 1) == 6

    arr = [10, 20, 40, 50]
    insert_at(arr, 2, 30)
    assert arr == [10, 20, 30, 40, 50]
    insert_at(arr, 0, 5)
    assert arr == [5, 10, 20, 30, 40, 50]
    insert_at(arr, len(arr), 60)
    assert arr == [5, 10, 20, 30, 40, 50, 60]

    assert delete_at(arr, 0) == 5
    assert arr == [10, 20, 30, 40, 50, 60]
    assert delete_at(arr, 5) == 60
    assert arr == [10, 20, 30, 40, 50]

    update(arr, 0, 11)
    assert arr[0] == 11

    assert merge_sorted([1, 4, 8], [2, 3, 9]) == [1, 2, 3, 4, 8, 9]
    assert merge_sorted([], [1, 2]) == [1, 2]
    print("array operations: all tests passed")
