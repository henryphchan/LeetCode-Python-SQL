# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        seen = ""
        for c in s:
            if c not in seen:
                seen += c
            else:
                seen += c
                seen = seen[seen.find(c)+1:]
            ans = max(ans,len(seen))
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))
    print(s.lengthOfLongestSubstring("bbbbb"))
    print(s.lengthOfLongestSubstring("pwwkew"))
    print(s.lengthOfLongestSubstring("aab"))