def moveZeroes(nums):
    left = 0  # 指向非零元素应该放置的位置
    for right in range(len(nums)):
        if nums[right] != 0:
            # 交换非零元素到左边
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
    return nums

# 示例
nums = [1, 1, 3,0, 3, 12]
moveZeroes(nums)
print(nums)  # 输出应该是 [1, 3, 12, 0, 0]