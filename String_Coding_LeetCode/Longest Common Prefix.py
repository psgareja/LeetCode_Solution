"""
Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
5,368,978/11.5M
Acceptance Rate
46.8%
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        for i in range(len(strs[0])):
            ch=strs[0][i]
            for word in strs[1:]:
                if i >= len(word) or word[i]!=ch:
                    return strs[0][:i]
        
        return strs[0]