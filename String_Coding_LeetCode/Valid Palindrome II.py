"""
 Valid Palindrome II
Solved
Easy
Topics
premium lock icon
Companies
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

 

Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false

"""
class Solution:
    def is_palindrome(self,s:str,left:int,right:int)->bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

    def validPalindrome(self, s: str) -> bool:
        
        left = 0
        right = len(s)-1
        while left < right:
            if s[left] != s[right]:
                return self.is_palindrome(s,left+1,right) or self.is_palindrome(s,left,right-1)
            left+=1
            right-=1
        return True
            