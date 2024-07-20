
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None
    
    while left <= right:
        iterations += 1
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            upper_bound = arr[mid]
            return (iterations, upper_bound)
        
        elif arr[mid] < target:
            left = mid + 1
        else:
            upper_bound = arr[mid]
            right = mid - 1
    
    if upper_bound is None and left < len(arr):
        upper_bound = arr[left]
    
    return (iterations, upper_bound)



def main():
    arr = [0.1, 1.2, 2.3, 3.4, 4.5, 5.6]
    target = 2.0
    result = binary_search(arr, target)
    print("Кількість ітерацій:", result[0])
    print("Верхня межа:", result[1])


if __name__ == "__main__":
    main()