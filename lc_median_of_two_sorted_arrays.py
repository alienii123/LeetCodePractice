class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        new_arr = nums1 + nums2
        medianofinput = 0
        new_arr.sort()
        modNew = int(len(new_arr) / 2)
        if len(new_arr) % 2 == 0:
            medianofinput = (new_arr[modNew-1] + new_arr[modNew])/2.0
        else:
            medianofinput = new_arr[modNew]
        return medianofinput

# Execute code
# mySol = Solution()
# print(mySol.findMedianSortedArrays([1,2], [3,4]))


# Longest substring without repeating chars
"""
Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:
Input: s = ""
Output: 0
"""


"""
findLongestSubstring

# code in complete
"""

"""
def findLongestSubstring(s):
    if len(s) == 0:
        return 0

    slen = len(s)
    start = 0
    end = start + 1

    longStr = ""
    for i in range(len(s)):
        longStr = s[start]

    return len(longStr), longStr
a, b = findLongestSubstring("abcabb")

print(b)
"""


"""
Minimum Operations to Make the Array Increasing
This is solved as below 
Code works
"""

"""
class Solution(object):
    def minOperations(self, nums):
        
        # :type nums: List[int]
        # :rtype: int
        
        min_operations = 0
        min_internal_ops = 0
        num_length = len(nums)
        new_nums = nums
        for i in range(num_length):
            if i+1 < num_length:
                if nums[i] < nums[i+1]:
                    print("ok")
                else:
                    min_internal_ops = (nums[i] - nums[i+1]) + 1
                    newnum = nums[i+1] + min_internal_ops
                    nums[i+1] = newnum
                    min_operations += min_internal_ops
                    # new_nums[i] = nums[i+1] + min_operations
            else:
                print("In else")
        return min_operations

objSol = Solution()
print(f"Return value is {objSol.minOperations([8])}")

"""

"""
1828. Queries on Number of Points Inside a Circle
This solution woks submitted!!!
"""

"""
import math
class Solution(object):
    def countPoints(self, points, queries):
        
        # :type points: List[List[int]]
        # :type queries: List[List[int]]
        # :rtype: List[int]
        
        outList = []

        for lstQuery in queries:
            x = lstQuery[0]
            y = lstQuery[1]
            rad = lstQuery[2]
            points_in_circle = 0
            for lstPoint in points:
                x_coordinate = lstPoint[0]
                y_coordinate = lstPoint[1]
                dist_two_pts = math.sqrt((x_coordinate-x)**2 + (y_coordinate-y)**2)
                if dist_two_pts <= rad:
                    points_in_circle+=1
            outList.append(points_in_circle)
        return outList

quNumber = Solution()
retList = quNumber.countPoints([[1,3],[3,3],[5,3],[2,2]], [[2,3,1],[4,3,1],[1,1,2]])
# ([[1,1],[2,2],[3,3],[4,4],[5,5]], [[1,2,2],[2,2,2],[4,3,2],[4,3,3]])

print(retList)
"""


"""
sliding window example
"""

import collections


def found_target(target_len):
    return target_len == 0


class Solution(object):
    def minWindow(self, search_string, target):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        target_letter_counts = collections.Counter(target)
        print(f'target_letter_counts value is {target_letter_counts}')
        start = 0
        end = 0
        min_window = ""
        target_len = len(target)

        for end in range(len(search_string)):
            # If we see a target letter, decrease the total target letter count
            if target_letter_counts[search_string[end]] > 0:
                target_len -= 1

            # Decrease the letter count for the current letter
            # If the letter is not a target letter, the count just becomes -ve
            target_letter_counts[search_string[end]] -= 1

            # If all letters in the target are found:

            while found_target(target_len):
                window_len = end - start + 1
                if not min_window or window_len < len(min_window):
                    # Note the new minimum window
                    min_window = search_string[start: end + 1]

                # Increase the letter count of the current letter
                target_letter_counts[search_string[start]] += 1

                # If all target letters have been seen and now, a target letter is seen with count > 0
                # Increase the target length to be found. This will break out of the loop
                if target_letter_counts[search_string[start]] > 0:
                    target_len += 1

                start += 1

        return min_window
"""
strFind = Solution()
# print(strFind.minWindow("ADOBECODEBANC", "BCO"))
print(strFind.minWindow("ab", "ccdeqqyy"))

"""

"""
Maximum XOR for Each Query

# Find a non-negative integer k < 2maximumBit such that nums[0] XOR nums[1] XOR ... 
# XOR nums[nums.length-1] XOR k is maximized. k is the answer to the ith query.
# Remove the last element from the current array nums.


# Input: nums = [0,1,1,3], maximumBit = 2
# Output: [0,3,2,3]
# Explanation: The queries are answered as follows:
# 1st query: nums = [0,1,1,3], k = 0 since 0 XOR 1 XOR 1 XOR 3 XOR 0 = 3.
# 2nd query: nums = [0,1,1], k = 3 since 0 XOR 1 XOR 1 XOR 3 = 3.
# 3rd query: nums = [0,1], k = 2 since 0 XOR 1 XOR 2 = 3.
# 4th query: nums = [0], k = 3 since 0 XOR 3 = 3.
# 
# Input: nums = [2,3,4,7], maximumBit = 3
# Output: [5,2,6,5]
# Explanation: The queries are answered as follows:
# 1st query: nums = [2,3,4,7], k = 5 since 2 XOR 3 XOR 4 XOR 7 XOR 5 = 7.
# 2nd query: nums = [2,3,4], k = 2 since 2 XOR 3 XOR 4 XOR 2 = 7.
# 3rd query: nums = [2,3], k = 6 since 2 XOR 3 XOR 6 = 7.
# 4th query: nums = [2], k = 5 since 2 XOR 5 = 7.
"""

class Solution(object):
    def getMaximumXor(self, nums, maximumBit):
        """
        :type nums: List[int]
        :type maximumBit: int
        :rtype: List[int]
        """
        maxElement = 2**maximumBit
        max_num_list = nums[0]
        outList = []
        for i in range(1,len(nums)):
            if max_num_list < nums[i]:
                if nums[i] <maxElement:
                    max_num_list = nums[i]
        # Now I have max element in the list
        print("Max num,", max_num_list)
        def get_XOR(lst):
            for i in range(len(lst)):
                if i == 0:
                    computeXOR = lst[0]
                else:
                    computeXOR = (computeXOR ^ lst[i])
            return computeXOR
        bb_list = nums
        for i in range(len(bb_list)):
            result_num = max_num_list - get_XOR(bb_list)
            bb_list = bb_list[:-1]
            outList.append(result_num)
        return outList

maxXOR = Solution()
print(maxXOR.getMaximumXor([0],1))

