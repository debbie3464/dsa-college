"""Count loop iterations and recursive calls to verify complexities.

Topic: Algorithm analysis (loop patterns, recurrences, time-space trade-off)
Each function RETURNS the number of basic operations, so you can print it
for several values of n and see the growth.
"""

# ---------------------------------------------------------------- loops


def count_step_k(n, k):
    """i = i + k            -> about n / k iterations  -> Theta(n)"""
    i, steps = 0, 0
    while i < n:
        i += k
        steps += 1
    return steps


def count_double(n):
    """i = i * 2 (from 1)   -> log2(n) iterations      -> Theta(log n)"""
    i, steps = 1, 0
    while i < n:
        i *= 2
        steps += 1
    return steps


def count_halve(n):
    """i = i // 2           -> log2(n) iterations      -> Theta(log n)"""
    i, steps = n, 0
    while i > 1:
        i //= 2
        steps += 1
    return steps


def count_square(n):
    """i = i * i (from 2)   -> log2(log2(n)) iterations -> Theta(log log n)"""
    i, steps = 2, 0
    while i < n:
        i = i * i
        steps += 1
    return steps


def count_nested_independent(n):
    """for i in 1..n: for j in 1..n          -> n * n          -> Theta(n^2)"""
    steps = 0
    for i in range(n):
        for j in range(n):
            steps += 1
    return steps


def count_nested_dependent(n):
    """for i in 1..n: for j in 1..i          -> n(n+1)/2       -> Theta(n^2)"""
    steps = 0
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            steps += 1
    return steps


def count_nested_log(n):
    """outer n times, inner j = j * 2        -> n * log n      -> Theta(n log n)"""
    steps = 0
    for i in range(n):
        j = 1
        while j < n:
            j *= 2
            steps += 1
    return steps


# ----------------------------------------------------------- recurrences


def t_minus_one_plus_c(n):
    """T(n) = T(n-1) + c      -> Theta(n)       (stack depth Theta(n))"""
    if n == 0:
        return 1
    return t_minus_one_plus_c(n - 1) + 1


def t_half_plus_c(n):
    """T(n) = T(n/2) + c      -> Theta(log n)   (stack depth Theta(log n))"""
    if n <= 1:
        return 1
    return t_half_plus_c(n // 2) + 1


def t_minus_one_plus_n(n):
    """T(n) = T(n-1) + n      -> Theta(n^2)     (stack depth Theta(n))"""
    if n == 0:
        return 0
    return t_minus_one_plus_n(n - 1) + n


def t_two_half_plus_c(n):
    """T(n) = 2T(n/2) + c     -> Theta(n)       (stack depth Theta(log n))"""
    if n <= 1:
        return 1
    return 2 * t_two_half_plus_c(n // 2) + 1


# ------------------------------------------------- time-space trade-off


def square_on_demand(i):
    """Option 1: no extra memory, Theta(1) per query."""
    return i * i


def build_square_table(n):
    """Option 2: Theta(n) time once and Theta(n) space, then Theta(1) lookup."""
    return [i * i for i in range(n + 1)]


if __name__ == "__main__":
    assert count_step_k(100, 5) == 20
    assert count_double(1024) == 10
    assert count_halve(1024) == 10
    assert count_square(65536) == 4
    assert count_nested_independent(10) == 100
    assert count_nested_dependent(10) == 55
    assert count_nested_log(16) == 64

    assert t_minus_one_plus_c(10) == 11
    assert t_half_plus_c(1024) == 11
    assert t_minus_one_plus_n(10) == 55
    assert t_two_half_plus_c(16) == 31          # 2n - 1 for n = 16

    table = build_square_table(10)
    assert table[7] == square_on_demand(7) == 49

    print(f"{'n':>6} {'double':>7} {'n*n':>8} {'n log n':>8}")
    for n in (8, 16, 32, 64):
        print(f"{n:>6} {count_double(n):>7} "
              f"{count_nested_independent(n):>8} {count_nested_log(n):>8}")
    print("complexity demos: all tests passed")
