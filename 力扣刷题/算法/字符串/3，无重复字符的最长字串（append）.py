'''
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:
输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
'''
#1，自己的代码（运行不通过）
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = []
        nums = 1
        for i in range(len(s)-1):
            for j in range(i+1,len(s)-1):
                if s[i] != s[j] and s[i] != s[j+1] and s[i+1] != s[j+1]:
                    nums += 2
                else:
                    res.append(nums)
                    nums = 1
                    break
        return max(res)
#solution = Solution()
#print(solution.lengthOfLongestSubstring("abcabcbb"))

#2,别人的代码
#字典st记录字符出现的位置，两个相同字符之间的距离，就是无重复字符的长度
class Solution:
    def lengthOfLongestSubstring1(self, s):
        """
        :type s: str
        :rtype: int
        """
        st = {}
        i, ans = -1, 0
        for j in range(len(s)):
            if s[j] in st:
                i = max(st[s[j]], i)
            ans = max(ans, j - i)
            st[s[j]] = j
        return ans;

solution = Solution()
print(solution.lengthOfLongestSubstring1("abcabcbb"))
print(solution.lengthOfLongestSubstring1("pwwkew"))
print(solution.lengthOfLongestSubstring1("bbbbb"))