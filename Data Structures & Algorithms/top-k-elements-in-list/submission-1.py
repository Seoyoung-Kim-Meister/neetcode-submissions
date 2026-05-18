from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
#        print(freq.most_common(k))
        l=freq.most_common(k)
        return [num for num, count in l] 
#        nums_set = sorted(nums)
#        N = len(nums_set)
#        for i in range(N):
#            count = []
#            for j in range(len(nums)):
#                j_count = 0
#                if nums[j] == nums[i]:
#                    j_count = j_count + 1
#                return [j_count,i]    
#            count.append(j_count)