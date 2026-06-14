class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for ch in strs:
            res=res+(str(len(ch)))+"#"+ch
        return res

    def decode(self, s: str) -> List[str]:
        res=[]
        i=0
        while i<len(s):
            j=i
            while s[j]!="#":
                j+=1
            word=int(s[i:j])
            freq=s[j+1 : word+j+1]
            res.append(freq)
            i=j+1+word
        return res
