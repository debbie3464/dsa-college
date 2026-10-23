# Module 1 Notes: Foundations of Data Structures

CSE464 Data Structures and Algorithms, Lecture 1 (From Data to Data Structures)

## 1. Data vs information

| Term | Meaning |
|---|---|
| **Data** | Raw observations, symbols, measurements, records, signals or relationships |
| **Information** | Data that has been organized, interpreted or summarized so it answers a question |

Example: `98, 66, 113/84` is data. "These are patient vital-sign readings taken at a particular time" is information. The difference is **context**.

## 2. Data structure

A **data structure** is a systematic way to organize and relate data so that the required operations can be performed efficiently.

- It is not merely a container. It encodes assumptions about **order, relationships and access**.
- Choose a structure by the operations you perform **most often** (the dominant operation).

## 3. Terminology (value to collection)

| Level | Example |
|---|---|
| Data item | 98.6 |
| Field | Temperature |
| Record | one patient visit |
| File / table | many visits |
| Database | related tables |

A **key** is a field that identifies a record, such as Patient ID.

## 4. ADT vs data structure vs implementation

| Term | Answers | Example (queue) |
|---|---|---|
| **ADT** | WHAT: the behaviour contract | supports enqueue and dequeue |
| **Data structure** | HOW the data is organized | circular array, or linked nodes |
| **Implementation** | CODE in a language | the Python or C class |

## 5. Classifications

| Pair | Meaning |
|---|---|
| **Linear** | elements follow a sequential relation (array, linked list, stack, queue) |
| **Non-linear** | elements can branch or form a network (tree, graph) |
| **Static** | capacity fixed or decided in advance |
| **Dynamic** | can grow or shrink during execution |
| **Homogeneous** | similar type or role, e.g. `[12, 17, 21]` |
| **Composite** | different fields form one object, e.g. `(ID, name, age)` |

"Static" refers to structural **capacity**, not whether stored values can change.

## 6. Core operations

| Operation | Meaning |
|---|---|
| Traversal | visit elements systematically |
| Search | find whether a target exists, and where |
| Insert | add an element while keeping the structure's rules |
| Delete | remove an element and repair the structure |
| Sort | reorder by a key |
| Update | change a value |
| Merge | combine compatible collections |
| Access | retrieve an element |

## 7. Cost depends on organization

| Need | Unsorted sequence | Sorted sequence | Relationship graph |
|---|---|---|---|
| Find exact value | may scan many items | can exploit order | follows connections |
| Insert new value | often simple at the end | may need to preserve order | add node or edge |
| Represent relationships | awkward | awkward | natural |

| Structure | Strength | Weakness |
|---|---|---|
| Array | direct positional access, compact | shifting on insert or delete is costly |
| Linked list | flexible insert and delete when position is known | no direct random access |
| Tree / graph | encodes hierarchy or relationships | search follows the structure |

## 8. Data structure vs algorithm

- **Data structure:** how data is organized and related.
- **Algorithm:** a finite procedure to solve a problem or perform an operation.
- Example: a sorted array (structure) enables binary search (algorithm).

## 9. Choose by dominant operation

| Scenario | Dominant need | Typical structure |
|---|---|---|
| Image tensor | indexed access | array |
| Orders or sensor readings by arrival | oldest first | queue |
| Undo history | most recent first | stack |
| Roads between cities, social network | connections | graph |
| Company hierarchy | parent and child | tree |

Name the **operation** first, then the structure.

## 10. Stack vs queue

| | Stack | Queue |
|---|---|---|
| Rule | last in, first out (LIFO) | first in, first out (FIFO) |
| Add at | top | rear |
| Remove from | top | front |

## 11. Common misconceptions

| Myth | Reality |
|---|---|
| Data structures are only about coding | they are modelling and organization choices before syntax |
| One structure is best | efficiency depends on workload and constraints |
| More complex means faster | complexity adds overhead and may be unnecessary |
| C is required to learn them | behaviour and reasoning are language-independent |

## 12. Self-test (answer closed-book)

1. Define a data structure in one sentence.
2. Distinguish data from information, and structure from algorithm.
3. Why does the same operation cost different amounts on different structures?
