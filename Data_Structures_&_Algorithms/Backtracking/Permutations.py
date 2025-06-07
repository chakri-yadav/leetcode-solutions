class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def backtrack(path,used):
            if len(path)==len(nums):
                res.append(path[:])
                return
            
            for i in range(len(nums)):
                if i in used:
                    continue
                path.append(nums[i])
                used.add(i)
                backtrack(path,used)
                path.pop()
                used.remove(i)
        backtrack([],set())
        return res
        