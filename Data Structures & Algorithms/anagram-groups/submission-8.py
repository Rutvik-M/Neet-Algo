class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap={}
        for word in strs:
            key=[0]*26
            for char in word:
                key[ord(char)-ord("a")]+=1
            tupl = tuple(key)
            if tupl not in hashmap:
                hashmap[tupl]=[]
            hashmap[tupl].append(word)
        return list(hashmap.values())
            





        