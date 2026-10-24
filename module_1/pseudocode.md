# Module 1 Pseudocode

**Conventions:** arrays are 0-indexed. `n = length(A)`. `NOT_FOUND = -1`. `floor(x)` rounds down. `mod` is the remainder.

## 1. Traversal

```
procedure Traverse(A):
    for i = 0 to length(A) - 1:
        visit(A[i])

procedure Sum(A):
    total = 0
    for i = 0 to length(A) - 1:
        total = total + A[i]
    return total
```

Time Θ(n). Space O(1).

## 2. Insertion into an array

`n` is the current size. The array has room for at least one more element.

```
procedure Insert(A, n, pos, value):
    if pos < 0 or pos > n:
        error "invalid position"
    if n == capacity:
        error "overflow"
    for i = n down to pos + 1:        // shift right
        A[i] = A[i - 1]
    A[pos] = value
    return n + 1                      // new size
```

Best case (insert at the end): Θ(1). Worst case (insert at index 0): Θ(n).

## 3. Deletion from an array

```
procedure Delete(A, n, pos):
    if pos < 0 or pos >= n:
        error "invalid position"
    value = A[pos]
    for i = pos to n - 2:             // shift left
        A[i] = A[i + 1]
    return value, n - 1               // removed value, new size
```

Best case (delete the last element): Θ(1). Worst case (delete index 0): Θ(n).

## 4. Linear search

```
procedure LinearSearch(A, target):
    n = length(A)
    for i = 0 to n - 1:
        if A[i] == target:
            return i
    return NOT_FOUND
```

```
procedure LinearSearchRecursive(A, target, i):
    if i == length(A):
        return NOT_FOUND
    if A[i] == target:
        return i
    return LinearSearchRecursive(A, target, i + 1)
// call: LinearSearchRecursive(A, target, 0)
```

Works on any order. Best Θ(1), worst Θ(n). Space: iterative Θ(1), recursive Θ(n).

## 5. Binary search (sorted array only)

```
procedure BinarySearch(A, target):
    low = 0
    high = length(A) - 1
    while low <= high:
        mid = low + floor((high - low) / 2)
        if A[mid] == target:
            return mid
        else if A[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return NOT_FOUND
```

```
procedure BinarySearchRecursive(A, target, low, high):
    if low > high:
        return NOT_FOUND
    mid = low + floor((high - low) / 2)
    if A[mid] == target:
        return mid
    else if A[mid] < target:
        return BinarySearchRecursive(A, target, mid + 1, high)
    else:
        return BinarySearchRecursive(A, target, low, mid - 1)
// call: BinarySearchRecursive(A, target, 0, length(A) - 1)
```

Best Θ(1), worst Θ(log n). Space: iterative Θ(1), recursive Θ(log n).
`mid = low + (high - low) / 2` avoids overflow of `low + high`.

## 6. Binary search variants

```
procedure FirstOccurrence(A, target):
    low = 0
    high = length(A) - 1
    answer = NOT_FOUND
    while low <= high:
        mid = low + floor((high - low) / 2)
        if A[mid] == target:
            answer = mid
            high = mid - 1            // keep looking left
        else if A[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return answer
```

```
procedure LastOccurrence(A, target):
    // same as FirstOccurrence, but on equality:
    //     answer = mid
    //     low = mid + 1              // keep looking right
```

```
procedure CountOccurrences(A, target):
    first = FirstOccurrence(A, target)
    if first == NOT_FOUND:
        return 0
    return LastOccurrence(A, target) - first + 1
```

```
procedure InsertionPosition(A, target):
    // run the normal BinarySearch loop;
    // if it ends without finding the target:
    return low
```

All run in Θ(log n).

## 7. Merging two sorted arrays

```
procedure Merge(A, n, B, m):
    C = new array of size n + m
    i = 0
    j = 0
    k = 0
    while i < n and j < m:
        if A[i] <= B[j]:
            C[k] = A[i]
            i = i + 1
        else:
            C[k] = B[j]
            j = j + 1
        k = k + 1
    while i < n:                      // copy what is left of A
        C[k] = A[i]
        i = i + 1
        k = k + 1
    while j < m:                      // copy what is left of B
        C[k] = B[j]
        j = j + 1
        k = k + 1
    return C
```

Time Θ(n + m). Space Θ(n + m).

## 8. Stack (array with `top`)

Start with `top = -1`.

```
procedure Push(S, x):
    if top == capacity - 1:
        error "overflow"
    top = top + 1                     // move first
    S[top] = x                        // then store

procedure Pop(S):
    if top == -1:
        error "underflow"
    x = S[top]                        // read first
    top = top - 1                     // then move
    return x

procedure Peek(S):
    if top == -1:
        error "empty"
    return S[top]
```

Every operation is Θ(1).

## 9. Queue

### Simple queue

Start with `front = 0` and `rear = -1`.

```
procedure Enqueue(Q, x):
    if rear == capacity - 1:
        error "overflow"
    rear = rear + 1
    Q[rear] = x

procedure Dequeue(Q):
    if front > rear:
        error "underflow"
    x = Q[front]
    front = front + 1
    return x
```

Weakness: slots before `front` are never reused, so the queue can look full while it has free space.

### Circular queue

Start with `front = 0` and `count = 0`.

```
procedure EnqueueCircular(Q, x):
    if count == capacity:
        error "overflow"
    rear = (front + count) mod capacity
    Q[rear] = x
    count = count + 1

procedure DequeueCircular(Q):
    if count == 0:
        error "underflow"
    x = Q[front]
    front = (front + 1) mod capacity
    count = count - 1
    return x
```

Every operation is Θ(1).

## 10. Time-space trade-off

```
// Option 1: no extra memory, Θ(1) per query
procedure Square(i):
    return i * i

// Option 2: Θ(n) time once and Θ(n) space, then Θ(1) per query
procedure BuildTable(n):
    for i = 1 to n:
        S[i] = i * i
    return S
// query: S[i]
```

Option 2 pays off only when there are many queries and memory allows.

## 11. Complexity summary

| Algorithm | Best | Worst | Extra space |
|---|---|---|---|
| Traversal | Θ(n) | Θ(n) | O(1) |
| Insert in array | Θ(1) | Θ(n) | O(1) |
| Delete from array | Θ(1) | Θ(n) | O(1) |
| Linear search | Θ(1) | Θ(n) | O(1); recursive Θ(n) |
| Binary search | Θ(1) | Θ(log n) | O(1); recursive Θ(log n) |
| Merge | Θ(n + m) | Θ(n + m) | Θ(n + m) |
| Stack / queue operation | Θ(1) | Θ(1) | O(1) |

## 12. Dry-run template

Binary search for `___` in `[ ... ]`:

| Step | low | high | mid | A[mid] | Action |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |

Fill in `low`, `high` and `mid` at every step, and finish with `found at index ...` or `low > high, not found`.
