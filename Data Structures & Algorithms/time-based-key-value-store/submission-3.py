class TimeMap:

    def __init__(self):
        self.hashmap={}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key]=[]
        self.hashmap[key].append((value,timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ""
        arr = self.hashmap[key]
        left=0
        right=len(arr)-1
        ans=""
        while left<=right:
            mid=(left+right)//2
            if arr[mid][1]==timestamp:
                return arr[mid][0]
            elif arr[mid][1]<timestamp:
                ans=arr[mid][0]
                left=mid+1
            else:
                right=mid-1
        return ans
        
