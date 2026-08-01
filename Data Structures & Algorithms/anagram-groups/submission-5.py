class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap={}
        for words in strs:
            freq=[0]*26
            for ch in words:
                freq[ord("a")-ord(ch)]+=1
            key=tuple(freq)
            if key not in hashmap:
                hashmap[key]=[]
            hashmap[key].append(words)
        return list(hashmap.values())




        