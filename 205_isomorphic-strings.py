# https://leetcode.com/problems/isomorphic-strings/
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        charMap = dict()
        for i in range(len(s)):
            #print(s[i],t[i],charMap)
            if charMap.get(s[i]) is None and t[i] not in charMap.values():
                charMap[s[i]] = t[i]
            elif charMap.get(s[i]) != t[i]:
                return False
        return True

if __name__ == "__main__":
    s = Solution()
    print(s.isIsomorphic("paper","title"))
    print(s.isIsomorphic("bbbaaaba","aaabbbba"))