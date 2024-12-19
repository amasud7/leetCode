def move_zeroes(nums):
    x = 0
    for i in range(0, len(nums)):
        x -= 1
        if nums[x] == 0:
            nums.pop(x)
            nums.append(0)

    return nums

print(move_zeroes([0, 0, 1]))



