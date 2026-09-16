def has_subarray_sum(nums, target):
    current_sum = 0
    start = 0

    # Expand the window by moving the 'end' pointer
    for end in range(len(nums)):
        current_sum += nums[end]

        # Shrink the window from the left if current_sum exceeds target
        while current_sum > target and start <= end:
            current_sum -= nums[start]
            start += 1

        # Check if we hit the target
        if current_sum == target:
            return True

    return False


# Example Usage:
nums = [1, 2, 3, 4]
target = 5
print(has_subarray_sum(nums, target))  # Output: True