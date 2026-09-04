# Optimized Binary Search

Two versions:

1. **Iterative**: Generally preferred in Python for avoiding recursion overhead and stack limits. It is slightly more memory efficient.
2. **Recursive**: Cleaner conceptually, but uses $O(\log n)$ stack space.

<!--more-->

### Optimizations Applied:

1. **Iterative Approach**: Avoids function call overhead.
2. **Floor Division (`//`)**: Used for index calculation to ensure integer results.
3. **Early Exit**: Handles edge cases like empty lists or single-element lists quickly.
4. **No Slicing**: Avoids creating new sub-lists during recursion (if using recursive approach) by passing `left` and `right` indices instead. This keeps time complexity at $O(\log n)$ and space complexity at $O(1)$ for the iterative version.

### Code (`binary_search.py`)

```python
def binary_search_iterative(arr: list, target) -> int:
    """
    Performs binary search on a sorted list iteratively.
    
    :param arr: A sorted list of elements
    :param target: The element to search for
    :return: The index of the target if found, otherwise -1
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        # Calculate mid index safely to avoid potential overflow in other languages
        # In Python, integers have arbitrary precision, so this is less critical,
        # but it's good practice.
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1


def binary_search_recursive(arr: list, target) -> int:
    """
    Performs binary search on a sorted list recursively.
    
    :param arr: A sorted list of elements
    :param target: The element to search for
    :return: The index of the target if found, otherwise -1
    """
    
    def _helper(left, right):
        if left > right:
            return -1
        
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return _helper(mid + 1, right)
        else:
            return _helper(left, mid - 1)
            
    return _helper(0, len(arr) - 1)


# Example usage
if __name__ == "__main__":
    sorted_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    
    # Test iterative
    print(f"Iterative search for 7: Index {binary_search_iterative(sorted_list, 7)}")  # Output: 3
    print(f"Iterative search for 6: Index {binary_search_iterative(sorted_list, 6)}")  # Output: -1
    
    # Test recursive
    print(f"Recursive search for 15: Index {binary_search_recursive(sorted_list, 15)}")  # Output: 7
    print(f"Recursive search for 2: Index {binary_search_recursive(sorted_list, 2)}")    # Output: -1
```

### Which one to use?

- Use **`binary_search_iterative`** for production code in Python. It is faster and doesn't risk hitting the recursion limit for very large lists.
- Use **`binary_search_recursive`** if you prefer code readability and don't expect extremely large inputs.

Both have $O(\log n)$ time complexity and $O(1)$ space complexity (for iterative) or $O(\log n)$ space complexity (for recursive due to call stack).

---

In **Python**, `mid = (left + right) // 2` **will not cause an overflow**.

### Why?
Python integers have **arbitrary precision**. This means they can grow as large as your computer's memory allows. There is no fixed bit-width (like 32-bit or 64-bit) that truncates values. So, `left + right` will simply result in a larger Python integer without overflowing.

### Why do people say it causes overflow?
This warning is critical in languages like **C, C++, Java, or Go**, where integers have fixed sizes (e.g., 32-bit signed integers max out at `2,147,483,647`).

If `left` and `right` are both large (e.g., near `2^31 - 1`), their sum can exceed the maximum value an `int` can hold, causing **integer overflow** (wrapping around to negative numbers), which breaks the binary search logic.

### Safe Calculation (Language-Agnostic Best Practice)
To be safe across all languages and follow best practices, you can calculate `mid` without adding the two large numbers directly:

```python
mid = left + (right - left) // 2
```

This avoids the intermediate sum `left + right` becoming larger than necessary. In Python, this isn't strictly necessary for correctness, but it's good practice if you ever translate this code to another language.

### Summary for Python:

- `mid = (left + right) // 2` is **safe** in Python.
- In other languages, use `mid = left + (right - left) // 2` to prevent overflow.
