# class Solution(object):
#     # def removeElement(self, nums, val):
#     #     """
#     #     :type nums: List[int]
#     #     :type val: int
#     #     :rtype: int
#     #     """
#     #     count = 0
#     #     while val in nums:
#     #         nums.remove(val)
#     #         count += 1
#     #     k = len(nums)
#     #     for _ in range(count):
#     #         nums.append('_')
#     #     return k, nums
#
#     def removeElement(self, nums, val):
#         k = 0  # Указатель для сохранения элементов, которые не равны val
#
#         # Проходим по всем элементам массива
#         for i in range(len(nums)):
#             if nums[i] != val:
#                 # Если элемент не равен val, сохраняем его на место nums[k]
#                 nums[k] = nums[i]
#                 k += 1
#
#         # Возвращаем количество элементов, которые не равны val
#         return k
# #
#
# l = [3, 2, 2, 3]
# v = 3
#
# s = Solution()
# print(s.removeElement(l, v))
from typing import List


# #--------------

# from typing import List
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         if not nums:
#             return 0
#
#         i = 0
#         for j in range(1, len(nums)):
#             if nums[j] != nums[i]:
#                 i += 1
#                 nums[i] = nums[j]
#
#         print(nums)
#         return i + 1

# #--------------

# from collections import Counter
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         c = Counter(nums)
#         for k, v in c.items():
#             if v > len(nums) / 2:
#                 return k

# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         nums_dict = {}
#         for i in nums:
#             nums_dict[i] = nums_dict.get(i, 0) + 1
#             if nums_dict[i] > len(nums)/2:
#                 return i
#
#         # for k, v in nums_dict.items():
#         #     if v > len(nums) / 2:
#         #         return k
#
#
# nums = [2, 2, 4]
# sol = Solution()
# res = sol.majorityElement(nums)
# print(res)


#--------------

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         min_price = float('inf')
#         max_prof = 0
#         for price in prices:
#             print(f"{price=}")
#             if price < min_price:
#                 print(f"new min = {price}")
#                 min_price = price
#             else:
#                 diff = price - min_price
#                 if max_prof < diff:
#                     max_prof = diff
#                 print(f"new max = {max_prof}")
#             print("=======================")
#         return max_prof
#
#
# s = Solution()
# l = [1, 5, 2, 2]
# res = s.maxProfit(l)
# print(res)


class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        number = 0
        pairs = {i: v for i, v in enumerate(s)}
        print(pairs)
        i = 0
        while i < len(s):
            if ((pairs[i] == 'I' and pairs.get(i + 1) in ('V', 'X'))
                    or (pairs[i] == 'X' and pairs.get(i + 1) in ('L', 'C'))
                    or (pairs[i] == 'C' and pairs.get(i + 1) in ('D', 'M'))
            ):
                number += (d[pairs[i+1]] - d[pairs[i]])
                i += 2
            else:
                number += d[pairs[i]]
                i += 1

        return number
#

# rome_number = "III"
rome_number = "IV"
sol = Solution()
print(sol.romanToInt(rome_number))
#
#
# class Solution:
#     def romanToInt(self, s: str) -> int:
#         translations = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
#         s = s.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace("XC", "LXXXX").replace("CD", "CCCC").replace("CM", "DCCCC")
#         return sum([translations[char] for char in s])
#
# # Пример
# sol = Solution()
# print(sol.romanToInt("MCMXCIV"))  # 1994

# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         words = s.split(" ")
#         words = [w for w in words if w]
#         return len(words[-1])
#
# s = "Hello world  "
#
# sol = Solution()
# res = sol.lengthOfLastWord(s)
# print(res)

#===========================================================
# https://leetcode.com/problems/longest-common-prefix/
# from typing import List
#
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         if len(strs) == 0:
#             return ""
#         pref = strs[0]
#         for s in strs:
#             while not s.startswith(pref):
#                 pref = pref[:-1]
#                 if not pref:
#                     return ""
#         return pref
#
# s = Solution()
# strs = ["flower", "flow", "flight"]
# res = s.longestCommonPrefix(strs)
#
# print(res)
#
# s = 'somestring'
# res = s.startswith('string', 4, 10)
# print(res)



# haystack = "ooosadbutsad"
# needle = "sad"
#
# # haystack = 'leetcode'
# # needle = "leeto"
#
# haystack, needle = ("mississippi", "issip")
#
#
# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         i, j, k = (0, 0, -1)
#         while i < len(haystack):
#
#             if haystack[i] == needle[j]:
#                 if j == 0:
#                     k = i
#                 if j == len(needle) - 1:
#                     return k
#                 j += 1
#             else:
#                 j = 0
#                 if k != -1:
#                     i = k
#                 k = -1
#             i += 1
#         return -1
#
#
# print(f"{i=} -- {j=} -- {k=}")
# print(f"{haystack[i]} -- {needle[j]}")
# print("====================================")

# haystack, needle = ('superday', 'day')
# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         return haystack.find(needle)
#
# s = Solution()
# res = s.strStr(haystack, needle)
# print(res)

# s = "A man, a plan, a canal: Panama"
# s = "P"
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         s_clean = list(l for l in s.lower() if l.isalnum())
#         print(f"{s_clean}")
#         if s_clean[::-1] == s_clean:
#             return True
#         else:
#             return False
#
# sol = Solution()
# print(sol.isPalindrome(s))

s = "axc"
t = "ahbxgdc"

# s = "aaaaaa"
# t = "bbaaaa"


# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         s_index = 0
#         if not s:
#             return True
#         for t_el in t:
#             if t_el == s[s_index]:
#                 s_index += 1
#                 if s_index == len(s):
#                     return True
#         return False
#
# sol = Solution()
#
# print(sol.isSubsequence(s, t))

# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

# l = 'mama'
# print(l.count('t'))
#
# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         ransomNote_dict = {i: ransomNote.count(i) for i in ransomNote}
#         magazine_dict = {i: magazine.count(i) for i in magazine}
#
#         for i, k in ransomNote_dict.items():
#             if magazine_dict.get(i, 0) < k:
#                 return False
#         return True
#
# r = 'aa'
# m = 'aab'
# sol = Solution()
# print(sol.canConstruct(r, m))

# s = "egg"
# t = "add"
#
# class Solution:
#     def isIsomorphic(self, s: str, t: str) -> bool:
#         def create_struct(some_str):
#             char_d = {}
#             for i, char in enumerate(some_str):
#                 tmp_list = char_d.get(char, [])
#                 tmp_list.append(i)
#                 char_d[char] = tmp_list
#             return list(char_d.values())
#
#         if create_struct(s) == create_struct(t):
#             return True
#         else:
#             return False
#
# sol = Solution()
# res = sol.isIsomorphic(s, t)
# print(res)

# from collections import defaultdict
# char_d = defaultdict(list)
# print(char_d)
# def_dict = {}
# print(def_dict)
#
# class Solution:
#     def isIsomorphic(self, s: str, t: str) -> bool:
#         def create_struct(some_str):
#             char_d = defaultdict(list)  # Используем defaultdict, чтобы избежать явного использования get
#             for i, char in enumerate(some_str):
#                 char_d[char].append(i)  # Добавляем индекс напрямую
#             return list(char_d.values())  # Возвращаем список значений (индексов)
#
#         # Сравниваем структуру двух строк
#         return create_struct(s) == create_struct(t)
#
# sol = Solution()
# res = sol.isIsomorphic(s, t)
# print(res)

# from collections import defaultdict
# char_d = defaultdict(int)
# char_d['a'] = char_d['a'] + 1
# print(char_d)
# print(type(char_d))
#
#
# char_e = {}
# char_e['a'] = char_e.get('a', 0) + 1
# print(char_e)

# from collections import defaultdict
# class Solution:
#     def wordPattern(self, pattern: str, s: str) -> bool:
#         def create_str(list_in: list):
#             char_d = defaultdict(list)
#             for i, ch in enumerate(list_in):
#                 char_d[ch].append(i)
#             print(char_d)
#             return list(char_d.values())
#
#         return create_str(list(pattern)) == create_str(s.split(" "))
#
# p = 'abba'
# s = 'dog cat cat dog'
# sol = Solution()
# res = sol.wordPattern(p, s)
#
# print(res)

# nums = [0, 1, 2, 4, 5, 7]
#
#
# class Solution:
#     def summaryRanges(self, nums: List[int]) -> List[str]:
#         path_list = []
#         i_s = 0
#         i_b = 0
#         for ind, i in enumerate(nums):
#             if i - i_b > 1:
#                 if i_s == i_b:
#                     path_list.append(f"{i_b}")
#                 else:
#                     path_list.append(f"{i_s}->{i_b}")
#                 i_s = i
#             i_b = i
#
#         if i_s == i_b:
#             path_list.append(f"{i_b}")
#         else:
#             path_list.append(f"{i_s}->{i_b}")
#
#         return path_list
#
# sol = Solution()
# res = sol.summaryRanges(nums)
# print(res)


# numbers_list = [1, 1, 2, 2, 3] # N = 5
# from collections import Counter
# def return_repeat(numbers: list) -> list:
#     return [k for k, v in Counter(numbers).items() if v > 1]
#
# res = return_repeat(numbers_list)
# print(res)


# from collections import Counter
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         c = Counter(nums)
#         for digit, freq in c.items():
#             if freq > 1:
#                 return True
#         return False

# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         freq_dict = {l: nums.count(l) for l in nums}
#         freq_dict_sorted = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)
#         if freq_dict_sorted[0][1] > 1:
#             return False
#
# #l = [1, 2, 10, 20, 20]

#
# sol = Solution()
# print(sol.containsDuplicate(l))

# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
#         left, right = (0, len(nums) -1)
#         while left <= right:
#             mid = (left + right) // 2
#             print("=================")
#             print(f"{mid=}")
#             print(f"{left=}")
#             print(f"{right=}")
#             if nums[mid] == target:
#                 print("found")
#                 return mid
#             elif nums[mid] < target:
#                 left = mid + 1
#             else:
#                 right = mid - 1
#         nums.append(target)
#         nums.sort()
#         return(nums.index(target))
#
#
# nums_list = [1, 3, 5, 10]
# target = 6
#
# sol = Solution()
# res = sol.searchInsert(nums_list, target)
# print(res)

s = "()[]{}"


class Solution:
    def isValid(self, s: str) -> bool:
        lifo = []
        pairs_dict = {
            '[':']',
            '{':'}',
            '(': ')',
        }
        for b in s:
            if b in pairs_dict.keys():
                lifo.append(b)
            else:
                if not lifo:
                    return False
                last = lifo.pop()
                if pairs_dict[last] == b:
                    print("ok")
                else:
                    return False
        if lifo:
            return False
        return True


str_in = '[]{}'
sol = Solution()
res = sol.isValid(str_in)
print(res)