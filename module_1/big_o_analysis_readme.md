# Big-O & Algorithm Loop Analysis Cheatsheet

A comprehensive guide to analyzing the time complexity ($\Theta$ and $O$ notation) of iterative loops and recurrence relations, complete with patterns, mathematical proofs, and solved practice problems.

---

## 🛠️ Core Patterns & Heuristics

### 1. General Rule for Nested Loops
$$\text{Total Time Complexity} = (\text{Outer Loop Iterations}) \times (\text{Average Inner Loop Iterations})$$

### 2. Common Growth Patterns

| Pattern | Code Example | Complexity Class |
| :--- | :--- | :--- |
| **Linear Step** | `i = i + 1` or `i = i - 1` | $\Theta(n)$ |
| **Constant Jump** | `j = j + 2` | $\Theta(n)$ |
| **Multiplicative / Divisive Step** | `i = i * 2`, `i = i / 3` | $\Theta(\log n)$ |
| **Repeated Squaring** | `i = i * i` | $\Theta(\log \log n)$ |
| **Dependent Inner Loop (Summation)** | `for j = 1..i` | $\Theta(n^2)$ |

> **Note on Logarithm Bases:** Changing log bases amounts to multiplication by a constant factor ($\log_b n = \frac{\log_a n}{\log_a b}$). Thus, all logarithmic bases fall into the same complexity class: $\Theta(\log n)$.

---

## ⚠️ Special Cases & Traps

### Traps 1: The Shrinking Loop / "Starting Near $n$"
```text
for i = 1..n:
    j = i
    while j <= n:
        j = j * 2
```
* **Intuition Trap:** Looks like $O(n \log n)$ because of the multiplication.
* **Reality:** For most values of $i$ (specifically $i > n/2$), the inner loop runs only **1 time**.
* **Math:** $\sum_{i=1}^{n} \log_2\left(\frac{n}{i}\right) \approx \boldsymbol{\Theta(n)}$.

### Trap 2: Independent $n$-Step Inside a $\log n$ Loop
```text
i = n
while i > 1:
    for j = 1..n:
        x = x + 1
    i = i / 3
```
* **Outer Loop:** Cuts problem by 3 each step $\rightarrow \log_3 n$ iterations.
* **Inner Loop:** Runs a full $n$ steps regardless of $i$.
* **Total Work:** $(\log_3 n) \times n = \boldsymbol{\Theta(n \log n)}$.

---

## 🧮 Recurrence Relations (Iteration Method)

### 1. Linear Decrement: $T(n) = T(n-1) + c$
* Unrolling: $T(n) = T(n-k) + kc$
* Base Case ($k = n-1$): $T(1) + (n-1)c$
* **Complexity:** $\boldsymbol{\Theta(n)}$

### 2. Divide and Conquer Step: $T(n) = T(n/2) + c$
* Unrolling: $T(n) = T\left(\frac{n}{2^k}\right) + kc$
* Base Case ($2^k = n \implies k = \log_2 n$): $T(1) + c \log_2 n$
* **Complexity:** $\boldsymbol{\Theta(\log n)}$

### 3. Linear Decrement with Linear Work: $T(n) = T(n-1) + n$
* Unrolling: $T(n) = T(1) + \sum_{i=2}^{n} i = \frac{n(n+1)}{2}$
* **Complexity:** $\boldsymbol{\Theta(n^2)}$

---

## 📝 Practice Problem Set

### Problem 1
```text
i = 1
while i < n:
    j = 1
    while j < n:
        x = x + 1
        j = j + 2
    i = i * 2
```
* **Answer:** $\mathbf{\Theta(n \log n)}$
* **Reason:** Outer loop runs $\log n$ times; inner loop runs $n/2$ times.

### Problem 2
```text
for i = 1..n:
    j = 1
    while j < i:
        j = j * 3
```
* **Answer:** $\mathbf{\Theta(n \log n)}$
* **Reason:** Summation $\sum_{i=1}^{n} \log_3(i) = \log_3(n!) = \Theta(n \log n)$.

### Problem 3
```text
i = n
while i > 0:
    i = i - 1
    for j = 1..i:
        x = x + 1
```
* **Answer:** $\mathbf{\Theta(n^2)}$
* **Reason:** Standard triangle sum $n + (n-1) + \dots + 1 = \frac{n(n+1)}{2}$.