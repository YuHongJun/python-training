#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Demi Yu'


# class Solution(object):
#     def longestCommonPrefix(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: str
#         """
#         if not strs:
#             print("kong")
#             return ""
#         for i, letter_group in enumerate(zip(*strs)):
#             print(list(zip(*strs)))
#             print(len(set(letter_group)))
#             if len(set(letter_group)) > 1:
#                 print(i)
#                 print('jinlaile')
#                 print(strs[0][:i])
#                 return strs[0][:i]
#             else:
#                 print('min')
#                 print(min(strs))
#                 return min(strs)
# # me=Solution()
# Solution().longestCommonPrefix(["abc","de"])

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dict = {"]":"[", "}":"{", ")":"("}
        for char in s:
            if char in dict.values():

                stack.append(char)
                print(stack)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []
result=Solution().isValid("{}[")
print(result)