class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        Lst=list()
        for i in range(n):
            for j in range(n):
                if j!=i:
                    if numbers[j]==target-numbers[i]:
                        Lst.append(i+1)
                        Lst.append(j+1)
                        Lst1=set(Lst)
                        Lst2=list(Lst1)
                        Lst2.sort()
        return Lst2
        