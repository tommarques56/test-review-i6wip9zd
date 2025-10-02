#!/usr/bin/env python3
"""
File with performance issues for testing.
"""

import time

def inefficient_sort(data):
    """Inefficient bubble sort implementation."""
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data

def slow_fibonacci(n):
    """Slow recursive fibonacci - should use memoization."""
    if n <= 1:
        return n
    return slow_fibonacci(n - 1) + slow_fibonacci(n - 2)

def process_large_list(data):
    """Process large list inefficiently."""
    result = []
    for i in range(len(data)):
        for j in range(len(data)):
            result.append(data[i] * data[j])
    return result

def main():
    print("Testing performance issues...")
    
    # Test inefficient sort
    data = [64, 34, 25, 12, 22, 11, 90]
    sorted_data = inefficient_sort(data.copy())
    print(f"Sorted: {sorted_data}")
    
    # Test slow fibonacci
    print(f"Fibonacci(10): {slow_fibonacci(10)}")
    
    # Test large list processing
    large_data = list(range(100))
    processed = process_large_list(large_data)
    print(f"Processed {len(processed)} items")

if __name__ == "__main__":
    main()
