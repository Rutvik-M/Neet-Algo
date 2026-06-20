class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for ch in strs:
            res=res+str(len(ch))+"#"+ch
        return res

    def decode(self, s: str) -> List[str]:
        res=[]
        i=0
        while i<len(s):
            j=i
            while s[j]!="#":
                j+=1
            length=int(s[i:j])
            count=s[j+1 :length+j+1]
            res.append(count)
            i=j+1+length
        return res
