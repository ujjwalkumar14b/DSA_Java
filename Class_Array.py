def binary_search(arr, target, left, right):
    if left > right:
        return -1
    mid = left + (right - left) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, left, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, right)


def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def find_max(arr):
    max_num = float("-inf")
    for num in arr:
        if num > max_num:
            max_num = num
    return max_num


def print_reversed(arr):
    print("Reversed Array: ", end="")
    for i in range(len(arr) - 1, -1, -1):
        print(arr[i], end=" ")
    print()


def print_pairs(arr):
    print("Pairs in array:")
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            print(f"({arr[i]},{arr[j]})", end=" ")
        print()


def max_subarray_brute_force(arr):
    max_sum = float("-inf")
    for i in range(len(arr)):
        current_sum = 0
        for j in range(i, len(arr)):
            current_sum += arr[j]
            max_sum = max(max_sum, current_sum)
    return max_sum


def max_subarray_prefix_sum(arr):
    if not arr:
        return 0
    prefix = [0] * len(arr)
    prefix[0] = arr[0]
    for i in range(1, len(arr)):
        prefix[i] = prefix[i - 1] + arr[i]

    max_sum = float("-inf")
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            current_sum = prefix[j] if i == 0 else prefix[j] - prefix[i - 1]
            max_sum = max(max_sum, current_sum)
    return max_sum


def trapping_water(heights):
    if not heights:
        return 0
    trapped_water = 0
    n = len(heights)
    left_max = [0] * n
    right_max = [0] * n
    left_max[0] = heights[0]
    right_max[n - 1] = heights[n - 1]

    for i in range(1, n):
        left_max[i] = max(heights[i], left_max[i - 1])

    for i in range(n - 2, -1, -1):
        right_max[i] = max(heights[i], right_max[i + 1])

    for i in range(n):
        water_level = min(left_max[i], right_max[i])
        trapped_water += water_level - heights[i]
    return trapped_water


def best_time_to_buy_stocks(prices):
    if not prices:
        return 0
    min_price = float("inf")
    max_profit = 0

    for i in range(1, len(prices)):
        profit = prices[i] - min_price
        max_profit = max(max_profit, profit)
        min_price = min(min_price, prices[i])
    return max_profit


def bubble_sort(nums):
    n = len(nums)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


def selection_sort(nums):
    n = len(nums)
    for i in range(n - 1):
        min_pos = i
        for j in range(i + 1, n):
            if nums[min_pos] > nums[j]:
                min_pos = j
        nums[min_pos], nums[i] = nums[i], nums[min_pos]
    return nums


def insertion_sort(nums):
    n = len(nums)
    for i in range(1, n):
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key
    return nums


def print_2d(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))


# Returns both row and column indices, or None if not found
def search_2d(matrix, target):
    if not matrix or not matrix[0]:
        return None
    row = len(matrix)
    column = len(matrix[0])

    for i in range(row):
        for j in range(column):
            if matrix[i][j] == target:
                return [i, j]  # Return list with coordinates
    return None  # Target not found


def spiral_matrix(grid):
    result = []
    if not grid or not grid[0]:
        return result

    top = 0
    bottom = len(grid) - 1
    left = 0
    right = len(grid[0]) - 1

    while top <= bottom and left <= right:
        # Traverse top row from left to right
        for i in range(left, right + 1):
            result.append(grid[top][i])
        top += 1

        # Traverse right column from top to bottom
        for i in range(top, bottom + 1):
            result.append(grid[i][right])
        right -= 1

        # Traverse bottom row from right to left (if still valid)
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(grid[bottom][i])
            bottom -= 1

        # Traverse left column from bottom to top (if still valid)
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(grid[i][left])
            left += 1

    return result


def search_sorted_grid(sorted_grid, target):
    if not sorted_grid or not sorted_grid[0]:
        return [-1, -1]

    row = 0
    col = len(sorted_grid[0]) - 1

    while row < len(sorted_grid) and col >= 0:
        if sorted_grid[row][col] == target:
            return [row, col]
        elif target < sorted_grid[row][col]:
            col -= 1
        else:
            row += 1
    return [-1, -1]


if __name__ == "__main__":
    nums1 = [1, 2, 3, 4]
    nums2 = [1, 2]

    print(nums1)
    print(nums2)

    target = 3
    print("Linear Search index:", linear_search(nums1, target))
    print("Max number:", find_max(nums1))
    print("Binary Search index:", binary_search(nums1, target, 0, len(nums1) - 1))

    print_reversed(nums1)
    print_pairs(nums1)
    print("Max Subarray (Brute Force):", max_subarray_brute_force(nums1))
    print("Max Subarray (Prefix Sum):", max_subarray_prefix_sum(nums1))

    heights = [4, 2, 0, 6, 3, 2, 5]
    print(trapping_water(heights))

    prices = [7, 1, 5, 3, 6, 4]
    print(trapping_water(prices))

    array = [5, 4, 1, 3, 2]
    print("Bubble Sort:", bubble_sort(array.copy()))
    print("Selection Sort:", selection_sort(array.copy()))
    print("Insertion Sort:", insertion_sort(array.copy()))

    array.sort()
    print("Inbuilt Sort:", array)

    print("Enter 6 integers for a 2x3 matrix (e.g., enter space-separated numbers per row):")
    matrix = []
    for i in range(2):
        row_input = list(map(int, input(f"Row {i + 1}: ").split()))
        matrix.append(row_input)

    print("\nMatrix:")
    print_2d(matrix)

    target = 3
    result = search_2d(matrix, target)

    if result is not None:
        print(f"\nTarget {target} found at row {result[0]}, column {result[1]}")
    else:
        print(f"\nTarget {target} not found.")

    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(spiral_matrix(grid))

    sorted_grid = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    print(search_sorted_grid(sorted_grid, 7))
    
