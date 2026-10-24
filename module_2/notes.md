# Module 1 Notes: Definitions

CSE464 Data Structures and Algorithms. Rewrite each definition in your own words as you revise.

## 1. Data and terminology

| Term | Definition |
|---|---|
| **Data** | Raw facts, observations, symbols, measurements or signals that can be stored and processed |
| **Information** | Data that has been organized or interpreted so it answers a question (`72, 81, 69, 88` is data; "the average is 77.5" is information) |
| **Data item** | A single unit of data. *Elementary* items can't be divided further; *group* items are made of elementary items |
| **Entity** | A real-world object about which data is stored |
| **Attribute** | A property of an entity |
| **Field** | The storage location or value for an attribute |
| **Record** | A collection of related fields describing one entity |
| **File / table** | A collection of related records |
| **Database** | A collection of related files or tables |
| **Key** | An attribute (field) used to identify or search for a record |

**Hierarchy:** bit → byte / character → field → record → file → database

## 2. Data structure basics

| Term | Definition |
|---|---|
| **Data structure** | A systematic way to organize and relate data so that the required operations (access, insertion, deletion, traversal, searching) can be performed efficiently. It encodes assumptions about order, relationships and access |
| **Abstract data type (ADT)** | A behaviour contract: WHAT operations are supported, not how (e.g. a queue supports enqueue and dequeue) |
| **Implementation** | The language-specific code that realizes a data structure |
| **Algorithm** | A finite, well-defined sequence of steps that solves a problem or performs an operation |

**ADT vs data structure vs implementation:** the ADT says *what*, the data structure says *how the data is organized* (circular array, linked nodes), and the implementation is the *code*.

**Data structure vs algorithm:** a structure organizes data; an algorithm is a procedure that works on it. A sorted array (structure) enables binary search (algorithm).

## 3. Classification

| Term | Definition |
|---|---|
| **Primitive** | Basic built-in types: int, float, bool, char |
| **Non-primitive** | Structures built from primitives: linear and non-linear |
| **Linear** | Elements follow a sequential relation: array, linked list, stack, queue |
| **Non-linear** | An element can take part in branching or network relationships: tree, graph |
| **Static** | Capacity or organization is fixed or decided in advance (this is about capacity, not whether stored values can change) |
| **Dynamic** | Can grow or shrink during execution |
| **Homogeneous** | Elements have a similar type or role, e.g. `[12, 17, 21]` |
| **Composite / heterogeneous** | Different fields form one logical object, e.g. `(ID, name, age)` |

## 4. Operations

| Operation | Definition |
|---|---|
| **Traversal** | Visit elements systematically, usually once each |
| **Searching** | Determine whether a target exists and, if so, where |
| **Insertion** | Add an element at a position while keeping the structure valid |
| **Deletion** | Remove an element and repair the structure (shift elements or fix links) |
| **Sorting** | Rearrange elements by a key |
| **Merging** | Combine compatible collections into one |
| **Update** | Change the value of an existing element |
| **Access** | Retrieve an element, e.g. by index |

State the structure and position when you quote a cost: insertion at the end of an array is Θ(1), but at the front it is Θ(n).

## 5. Algorithms and analysis

| Term | Definition |
|---|---|
| **Algorithm characteristics** | Input (zero or more), output (at least one), definiteness, finiteness, effectiveness, generality |
| **A priori analysis** | Theoretical: counts operations as a function of n, before and independent of running, and independent of hardware |
| **A posteriori analysis** | Empirical: run the program and measure actual time and memory, which depends on hardware |
| **Input size (n)** | The measure of the input: elements, records or characters. Always say which |
| **Basic operation** | The operation whose repetitions dominate the work |
| **Best case** | The input needing the minimum work |
| **Worst case** | The input needing the maximum work |
| **Average case** | Expected work under a stated probability model (not simply (best + worst) / 2) |
| **Time complexity** | How the number of elementary operations grows with input size |
| **Space complexity** | How much memory is needed as the input grows |
| **Auxiliary space** | Extra memory beyond the input itself |
| **Time-space trade-off** | Using extra memory to reduce time, or extra computation to save memory |

**Order of growth (slow to fast):** 1 < log n < √n < n < n log n < n² < n³ < 2ⁿ < n!

## 6. Asymptotic notation

| Notation | Meaning | Formal definition |
|---|---|---|
| **O(g)** | Upper bound | ∃ c > 0, n₀ : 0 ≤ f(n) ≤ c·g(n) for all n ≥ n₀ |
| **Ω(g)** | Lower bound | ∃ c > 0, n₀ : 0 ≤ c·g(n) ≤ f(n) for all n ≥ n₀ |
| **Θ(g)** | Tight bound | ∃ c₁, c₂ > 0, n₀ : c₁·g(n) ≤ f(n) ≤ c₂·g(n) for all n ≥ n₀ |
| **o(g)** | Strict upper bound | for every c > 0, ∃ n₀ : f(n) < c·g(n); equivalently lim f/g = 0 |
| **ω(g)** | Strict lower bound | for every c > 0, ∃ n₀ : c·g(n) < f(n); equivalently lim f/g = ∞ |

- f ∈ O(g) and f ∈ Ω(g) imply f ∈ Θ(g).
- **Limit test** for L = lim f(n)/g(n): L = 0 gives o, 0 < L < ∞ gives Θ, L = ∞ gives ω.
- **Big-O is not the same as worst case.** O is a mathematical upper bound. Best, average and worst case functions can each be described with it.
- **Simplification:** drop constants, keep the dominant term, and ignore the base of a logarithm.

## 7. Recursion and recurrences

| Term | Definition |
|---|---|
| **Recursion** | A function that solves a problem by calling itself on a smaller input |
| **Base case** | The simplest input, answered directly with no further call |
| **Recursive case** | The call on a smaller input, plus the work that uses its result |
| **Call stack** | The memory holding the active recursive calls. Depth n uses Θ(n) space; depth log n uses Θ(log n) |
| **Recurrence relation** | An equation giving the running time T(n) in terms of T on smaller inputs |
| **Iteration method** | Expand the recurrence step by step, find the pattern after k steps, then solve for k |

## 8. Searching

| Term | Definition |
|---|---|
| **Linear search** | Check elements one by one until the target is found or the data ends. Works on any order: best Θ(1), worst Θ(n) |
| **Binary search** | On sorted data, compare with the middle element and discard half the range each step: best Θ(1), worst Θ(log n) |
| **Insertion position** | The index where a missing target would go to keep the data sorted (`low` when the search ends) |

Binary search needs sorted data. Iterative space is Θ(1); recursive space is Θ(n) for linear search and Θ(log n) for binary search.

## 9. Stack and queue

| Term | Definition |
|---|---|
| **Stack** | A linear structure with last-in, first-out (LIFO) access at one end, the top |
| **Push / pop / peek** | Add at the top / remove from the top / read the top without removing |
| **Queue** | A linear structure with first-in, first-out (FIFO) access: add at the rear, remove from the front |
| **Enqueue / dequeue** | Add at the rear / remove from the front |
| **Circular queue** | A queue whose indexes wrap around (with mod), so freed slots are reused |
| **Overflow** | Adding to a full structure |
| **Underflow** | Removing from an empty structure |

## 10. Quick self-test

1. Define a data structure in one sentence.
2. Distinguish data from information, and a data structure from an algorithm.
3. Write the formal definition of Θ.
4. Why is "Big-O means worst case" wrong?
5. State the base case and recursive case of binary search.
