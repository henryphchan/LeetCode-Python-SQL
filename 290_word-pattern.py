# https://leetcode.com/problems/word-pattern/
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hashMap = dict()
        ptr = 0
        if len(pattern) != len(s.split()): return False
        for word in s.split():
            if word not in hashMap.values() and pattern[ptr] not in hashMap.keys():
                hashMap[pattern[ptr]] = word
            elif word == hashMap.get(pattern[ptr]):
                pass
            else :
                return False
            ptr += 1
        return True
                
if __name__ == "__main__":
    s = Solution()
    print(s.wordPattern("abba","dog dog dog dog"))
    print(s.wordPattern("abba","dog cat cat dog"))