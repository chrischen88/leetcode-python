from typing import List

def removeDuplicates(nums: List[int]) -> int:
    '''
    This function removes duplicate integers in-place, does not deal with extraneous space\n
    Returns number of integers left\n
    Time: O(n)
    '''
    idx_to_keep = []
    prev = None
    for idx, num in enumerate(nums):
        if prev is None:
            prev = num
            idx_to_keep.append(idx)
        else:
            if prev != num:
                idx_to_keep.append(idx)
                prev = num
    cur_idx = 0
    while cur_idx < len(idx_to_keep):
        nums[cur_idx] = nums[idx_to_keep[cur_idx]]
        cur_idx += 1
    return cur_idx

def rotate(nums: List[int], k: int) -> None:
    num_to_move = k % len(nums)
    last_nums = nums[-num_to_move:]
    nums[num_to_move:] = nums[:-num_to_move]
    nums[:num_to_move] = last_nums

def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    num_freq = {}
    res = []
    for num in nums1:
        if num_freq.get(num):
            num_freq[num] += 1
        else:
            num_freq[num] = 1
    for num in nums2:
        if num_freq.get(num) and num_freq.get(num) != 0:
            num_freq[num] -= 1
            res.append(num)
    return res