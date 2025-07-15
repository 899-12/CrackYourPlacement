def binarySearch(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2  # Find the middle index

        if nums[mid] == target:
            return mid  # Found the target
        elif nums[mid] < target:
            left = mid + 1  # Search right half
        else:
            right = mid - 1  # Search left half

    return -1  # Target not found
