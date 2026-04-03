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
                if len(stack)==0 or matcher[i]!=stack.pop():
                    return False
        
        return len(stack)==0