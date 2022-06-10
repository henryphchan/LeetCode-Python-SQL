# https://leetcode.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for p in s:
            if p in ["(","{","["]:
                stack.append(p)
            elif p in [")","}","]"]:
                if len(stack) == 0:
                    return False
                value = stack.pop()
                if (value == "(" and p != ")") \
                or (value == "[" and p != "]") \
                or (value == "{" and p != "}") :
                    return False
                
        if len(stack) == 0:
            return True
        else:
            return False

if __name__ == '__main__':
    s = Solution()
    print(s.isValid("()[]{}"))
    print(s.isValid("((([[]]{[]})))"))
    print(s.isValid("()[]{})"))