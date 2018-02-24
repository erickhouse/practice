

def search(nums, target):
    if len(nums) == 0:
        return -1
    if len(nums) == 1:
        if nums[0] == target:
            return nums[0]
        else:
            return -1

    def find_pivot(lo, hi):
        mid = (hi - (hi - lo)) // 2

        if nums[mid + 1] < nums[mid]:
            return mid
        if nums[hi] < nums[mid]:
            return find_pivot(mid, hi)
        if nums[lo] > nums[mid]:
            return find_pivot(lo, mid)

        return -1

    def binary_search(lo, hi):
        mid = (hi - (hi - lo)) // 2

        if lo == hi:
            return -1

        if target == nums[mid]:
            return mid
        if target < nums[mid]:
            return binary_search(lo, mid)
        if target > nums[mid]:
            return binary_search(mid, hi)

    pivot = find_pivot(0, len(nums) - 1)

    if target == nums[pivot]:
        return pivot
    elif pivot == -1:
        return binary_search(0, len(nums) -1)
    elif target < nums[pivot]:
        return binary_search(0, pivot)
    else:
        return binary_search(pivot, len(nums) -1)






nums = [1,3]
print(search(nums,10))
