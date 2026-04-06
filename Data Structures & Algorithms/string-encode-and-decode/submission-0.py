class Solution:

    def encode(self, strs: List[str]) -> str:
        op=""
        for word in strs:
            size=len(word)
            op=op+str(size)+"#"+word
        return op

    def decode(self, s: str) -> List[str]:
        res=[]
        i=0

        while i<len(s):
            j=i
            while(s[j]!='#'):
                j=j+1
        #currently j is on #
            word_length=int(s[i:j])
            res.append(s[j+1:j+1+word_length])
            i=j+1+word_length
        return res