class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap={}

        for word in strs:
            words=[0]*26
            for ch in word:
                words[ord(ch)-ord("a")]+=1
            tup=tuple(words)
            if tup not in hashmap:
                hashmap[tup]=[]
            hashmap[tup].append(word)
        return list(hashmap.values())
        
            
        