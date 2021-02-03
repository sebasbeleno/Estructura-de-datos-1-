def Suma_grupo(start, nums, target):
    if (start >= len(nums)):
        return target == 0
    add = Suma_grupo(start+1, nums, target - nums[start])
    add_not = Suma_grupo(start+1, nums, target)
    return add or add_not

print(Suma_grupo(0,[2, 5, 3],10))