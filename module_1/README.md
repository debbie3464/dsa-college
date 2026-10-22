# CSE464 — Data Structures & Algorithms
## Module I: Introduction — Exam Cheat Sheet

> Covers: basic terminology · data-structure operations · algorithm analysis · asymptotic notation · time–space trade-off · linear & binary search

## Table of Contents
- [1. Terminology](#1-terminology)
- [2. Operations](#2-operations)
- [3. Analysing an Algorithm](#3-analysing-an-algorithm)
- [4. Asymptotic Notation](#4-asymptotic-notation)
- [5. Loop Complexity Patterns](#5-loop-complexity-patterns)
- [6. Recurrences (Iteration Method)](#6-recurrences-iteration-method)
- [7. Time–Space Trade-off](#7-timespace-trade-off)
- [8. Searching](#8-searching)
- [9. Common Mistakes](#9-common-mistakes)
- [10. Last-Minute Revision](#10-last-minute-revision)

---

## 1. Terminology

| Term | Definition |
|---|---|
| **Data** | Raw facts, observations or symbols that can be stored and processed |
| **Information** | Data that has been processed/organised so it is meaningful (72, 81, 69, 88 = data; "average is 77.5" = information) |
| **Data item** | A single unit of data meaningful in context. *Elementary* = can't be divided further; *Group* = made of elementary items |
| **Entity** | Real-world object about which data is stored |
| **Attribute** | A property of an entity |
| **Field** | Storage location/value for an attribute |
| **Record** | Collection of related fields for one entity |
| **File** | Collection of related records |
| **Key** | Attribute used to identify/search records |
| **Data structure** | Systematic way of organising and storing data **and the relationships among items** so access, insertion, deletion, traversal and searching are efficient |

Hierarchy: `bit → byte/character → field → record → file → database`

**Classification:** Primitive (int, float, bool, char) vs Non-primitive → **Linear** (array, linked list, stack, queue) and **Non-linear** (tree, graph).

---

## 2. Operations

| Operation | Meaning |
|---|---|
| **Traversal** | Visit elements systematically, usually once each — Θ(n) |
| **Insertion** | Add an element at a position, keeping the structure valid (array: shift right) |
| **Deletion** | Remove an element, restore validity (array: shift left) |
| **Searching** | Find whether a key exists / return its location |

Others: access, update, sorting, merging.

> Never say "insertion is O(n)" without naming the structure and position.

---

## 3. Analysing an Algorithm

**Algorithm characteristics:** Input (≥ 0) · Output (≥ 1) · **Definiteness** · **Finiteness** · **Effectiveness** · **Generality**

| | A priori (theoretical) | A posteriori (empirical) |
|---|---|---|
| When | Before / independent of running | After implementing and running |
| Measures | Operation count as function of n | Actual time/memory |
| Depends on hardware? | No | Yes |

- **Input size n:** elements / records / characters — state what n means.
- **Basic operation:** the operation whose repetitions dominate the work.
- **Best case** = minimum work · **Worst case** = maximum work · **Average case** = expected work under a **stated probability model** (**not** (best+worst)/2).
- **Time complexity:** how the number of elementary operations grows with input size.
- **Space complexity:** memory needed as function of input size. **Auxiliary space** = extra memory beyond the input.
- Recursion depth n ⇒ Θ(n) stack; depth log n ⇒ Θ(log n) stack.

**Order of growth (slow → fast):**

```
1 < log n < √n < n < n log n < n² < n³ < 2ⁿ < n!
```

**Combining rules**
1. Sequence → add, keep the dominant term
2. Simple loop → iterations × body cost
3. Nested loops → multiply if independent; **sum actual counts if dependent**
4. Conditional → worst case uses the costliest branch
5. Recursion → write a recurrence

---

## 4. Asymptotic Notation

| Notation | Meaning | Formal definition |
|---|---|---|
| **O(g)** | Upper bound | ∃ c, n₀ : 0 ≤ f(n) ≤ c·g(n) ∀ n ≥ n₀ |
| **Ω(g)** | Lower bound | ∃ c, n₀ : 0 ≤ c·g(n) ≤ f(n) ∀ n ≥ n₀ |
| **Θ(g)** | Tight bound | ∃ c₁, c₂, n₀ : c₁g(n) ≤ f(n) ≤ c₂g(n) ∀ n ≥ n₀ |
| **o(g)** | Strict upper | ∀ c > 0 ∃ n₀ : f(n) < c·g(n) ⇔ lim f/g = 0 |
| **ω(g)** | Strict lower | ∀ c > 0 ∃ n₀ : c·g(n) < f(n) ⇔ lim f/g = ∞ |

- f ∈ O(g) **and** f ∈ Ω(g) ⇒ f ∈ Θ(g)
- **Limit test** L = lim f(n)/g(n): `L = 0 → o` · `0 < L < ∞ → Θ` · `L = ∞ → ω`
- Examples: `n ∈ o(n²)` ✔ · `n² ∈ o(n²)` ✘ · `n² ∈ ω(n)` ✔ · `n ∉ ω(n)` · `n log n = o(n²)` · `2ⁿ = o(3ⁿ)`
- **Big-O ≠ worst case.** O is a mathematical upper bound; best/average/worst functions can each be described with it.
- Simplification: drop constants · keep dominant term · log bases differ by a constant · (n+k)² = Θ(n²)

### Proofs to memorise
```
3n + 7 ∈ O(n):         n ≥ 1 ⇒ 7 ≤ 7n ⇒ 3n+7 ≤ 10n          c = 10, n₀ = 1
4n²+3n+2 ∈ O(n²):      n ≥ 1 ⇒ ≤ 9n²                          c = 9,  n₀ = 1
4n²+3n+2 ∈ Ω(n²):      ≥ 4n²                                  c = 4,  n₀ = 1
6n²+5n+9 ∈ Θ(n²):      6n² ≤ f(n) ≤ 20n²                      c₁ = 6, c₂ = 20, n₀ = 1
```
**Method:** for n ≥ 1, bound each lower-order term by a multiple of the dominant term, add the coefficients, state c and n₀.

---

## 5. Loop Complexity Patterns

**Method:** write `i` after 1, 2, 3 iterations → formula after t iterations → apply stop condition → solve for t → simplify.

| Loop | After t steps | Iterations | Complexity |
|---|---|---|---|
| `i = i + 1` or `i + k` | i = tk | n/k | **Θ(n)** |
| `i = i - 3` | n − 3t | n/3 | **Θ(n)** |
| `i = i * k` (k > 1) | kᵗ ≤ n | log_k n | **Θ(log n)** |
| `i = i / 2` | n/2ᵗ ≤ 1 | log₂ n | **Θ(log n)** |
| `i` loses a fixed fraction | n·(3/4)ᵗ ≈ 1 | log_{4/3} n | **Θ(log n)** |
| `i = i * i` / `i = iᵏ` (from 2) | 2^(kᵗ) ≤ n | log_k(log₂ n) | **Θ(log log n)** |

### Nested loops

| Code | Count | Complexity |
|---|---|---|
| `for i=1..n: for j=1..n` | n·n | Θ(n²) |
| `for i=1..n: for j=1..i` | 1+2+…+n = n(n+1)/2 | Θ(n²) |
| `for i=1..n: for j=i..n` | n+(n−1)+…+1 | Θ(n²) |
| outer `n`, inner `j = j*2` up to n | n · log n | Θ(n log n) |
| outer `i *= 2`, inner `j *= 2` | log n · log n | Θ((log n)²) |
| `for i=1..n: j=1; while j<=i: j*=2` | Σ log i = log(n!) | Θ(n log n) |
| `for i=1..n: j=i; while j<=n: j*=2` | Σ (1 + log(n/i)) | **Θ(n)** (non-obvious) |
| Loop of n, then loop of n² | Θ(n) + Θ(n²) | Θ(n²) |

---

## 6. Recurrences (Iteration Method)

| Recurrence | Expansion | Time | Stack depth |
|---|---|---|---|
| `T(n) = T(n−1) + c` | T(0) + n·c | **Θ(n)** | Θ(n) |
| `T(n) = T(n/2) + c` | T(n/2ᵏ) + k·c, k = log₂n | **Θ(log n)** | Θ(log n) |
| `T(n) = T(n−1) + n` | n + (n−1) + … + 1 | **Θ(n²)** | Θ(n) |
| `T(n) = 2T(n/2) + c` | 2ᵏT(n/2ᵏ) + (2ᵏ−1)c → nT(1) + (n−1)c | **Θ(n)** | Θ(log n) |

- For `2T(n/2) + c`: time counts **all** calls (Θ(n)); space counts only the **deepest active path** (Θ(log n)).
- If a function has a loop of size n **plus** a recursive call on n/2, the recurrence is `T(n/2) + Θ(n)`, **not** `+ Θ(1)`.

---

## 7. Time–Space Trade-off

Using **extra memory to reduce time**, or extra computation to save memory.

```
Option 1: compute i*i on every query      → no extra memory, Θ(1) per query
Option 2: precompute S[i] = i*i, 1..n     → Θ(n) time once + Θ(n) space, then Θ(1) lookup
```
Worth it only if there are many queries and memory allows.

---

## 8. Searching

### Linear search (iterative) — **must write**
```
procedure LinearSearch(A, target):
    n = length(A)
    for i = 0 to n - 1:
        if A[i] == target:
            return i
    return NOT_FOUND
```

### Linear search (recursive) — **must write**
```
procedure LinearSearchRecursive(A, target, i):
    if i == length(A):
        return NOT_FOUND
    if A[i] == target:
        return i
    return LinearSearchRecursive(A, target, i + 1)
# call: LinearSearchRecursive(A, target, 0)
```

### Binary search (iterative) — **must write**
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

### Binary search (recursive) — **must write**
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
# call: BinarySearchRecursive(A, target, 0, length(A) - 1)
```
> `mid = low + (high - low)/2` avoids integer overflow of `low + high`.

### Variants
- **First occurrence (sorted, duplicates):** on equality set `answer = mid` and `high = mid - 1`.
- **Last occurrence:** on equality set `answer = mid` and `low = mid + 1`.
- **Count occurrences:** `last − first + 1` (0 if absent) → Θ(log n).
- **Insertion position:** normal binary search, then `return low`.

### Complexity

| | Linear | Binary |
|---|---|---|
| Data | Any order | **Must be sorted** |
| Strategy | One by one | Discard half each step |
| Best | Θ(1) | Θ(1) |
| Worst | Θ(n) | Θ(log n) |
| Average (successful) | (n+1)/2 = Θ(n) | Θ(log n) |
| Iterative space | Θ(1) | Θ(1) |
| Recursive space | Θ(n) | Θ(log n) |

Why logarithmic: n/2ᵏ ≤ 1 ⇒ k ≥ log₂ n.

**Linear still wins when:** the collection is tiny · data unsorted with few searches · sequential-access data (e.g. linked list) · sorting costs more than it saves.

### Traces
```
Linear:  find 23 in [11, 7, 18, 23, 5]  → i = 0,1,2 no; i = 3 yes → return 3 (4 comparisons)

Binary:  find 31 in [4, 9, 13, 18, 24, 31, 37, 42, 56]
         low=0 high=8 mid=4 (24)  → 31 > 24 → low=5
         low=5 high=8 mid=6 (37)  → 31 < 37 → high=5
         low=5 high=5 mid=5 (31)  → found at index 5
```

---

## 9. Common Mistakes

1. Counting lines of code instead of repetitions
2. Assuming every nested loop is Θ(n²)
3. Ignoring best vs worst case
4. Confusing O with Θ (`n ∈ O(n²)` is true but loose)
5. Forgetting recursion stack space
6. Using binary search on unsorted data
7. Saying average = (best + worst) / 2
8. Writing `T(n/2) + c` when the function also has an n-size loop
9. Giving a Θ answer without showing the value sequence / summation

---

## 10. Last-Minute Revision

```
Loop patterns     +c → Θ(n)   ×c → Θ(log n)   /c → Θ(log n)   i^k → Θ(log log n)
Recurrences       T(n-1)+c → n      T(n/2)+c → log n      T(n-1)+n → n²      2T(n/2)+c → n
Searching         linear Θ(n) any data · binary Θ(log n) sorted data
Space             iterative Θ(1) · recursive linear Θ(n) · recursive binary Θ(log n)
Method            values after t steps → formula → stop condition → solve t → simplify
```
