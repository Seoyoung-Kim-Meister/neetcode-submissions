class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_list = []
        used = set()
        for i in range(len(strs)):
            if i in used:
                continue
            group = [strs[i]]
            for j in range(i+1, len(strs)):
                if sorted(strs[j]) == sorted(strs[i]):
                    group.append(strs[j])
                    used.add(j)
            final_list.append(group)        
        return final_list  