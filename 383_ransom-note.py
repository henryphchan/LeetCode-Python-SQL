# https://leetcode.com/problems/ransom-note/
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for m in ransomNote:
            if magazine.count(m) < ransomNote.count(m):
                return False
        return True

if __name__ == "__main__":
    s = Solution()
    print(s.canConstruct("aa", "aab"))
    print(s.canConstruct("aab", "baa"))