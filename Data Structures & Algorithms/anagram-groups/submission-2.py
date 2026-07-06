class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result= defaultdict(list)

        for char in strs:
            count = [0]*26

            for ch in char:
                count[ord(ch)-ord("a")] +=1

            result[tuple(count)].append(char)
        return list(result.values())