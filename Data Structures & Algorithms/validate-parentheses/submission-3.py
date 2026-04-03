class Solution:
    def isValid(self, s: str) -> bool:
        matcher={
            '}':'{',
            ']':'[',
            ')':'('
        }
        stack=[]
        for i in s:
            if i in matcher.values():
                stack.append(i)
            else: 
                if not stack or matcher[i]!=stack.pop():
                    return False
        
        return len(stack)==0