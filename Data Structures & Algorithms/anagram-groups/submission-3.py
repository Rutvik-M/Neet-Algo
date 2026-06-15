class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap={}
        for words in strs:
            word=[0]*26
            for ch in words:
                word[ord(ch)-ord("a")]+=1
            key=tuple(word)
            if key not in hashmap:
                hashmap[key]=[]
            hashmap[key].append(words)
        return list(hashmap.values())
        