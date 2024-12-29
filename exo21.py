def length(lst):
    return len(lst)

def mean(lst):
    if len(lst) == 0:
        return None  # Avoid division by zero
    return sum(lst) / len(lst)

def range_of_list(lst):
    if len(lst) == 0:
        return None  # Range is undefined for empty list
    return max(lst) - min(lst)

numbers = [1, 2, 3, 4, 5]

print(f"Length: {length(numbers)}")  # Output: 5
print(f"Mean: {mean(numbers)}")  # Output: 3.0
print(f"Range: {range_of_list(numbers)}")  # Output: 4