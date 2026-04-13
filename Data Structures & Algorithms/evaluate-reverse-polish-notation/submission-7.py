class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=deque()

        for s in tokens:
            if s!="+" and s!="/" and s!="*" and s!="-":
                st.append(int(s))
            else:
                e1=st.pop()
                e2=st.pop()
                match s:
                    case "+":
                        st.append(e1+e2)
                    case "-":
                        st.append(e2-e1)
                    case "*":
                        st.append(e1*e2)
                    case "/":
                        st.append(int(e2/e1))
            print(st)
        
        return st[0]
            
        