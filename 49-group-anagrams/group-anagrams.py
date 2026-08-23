class Solution(object):
    def groupAnagrams(self, strs):
        an=defaultdict(list)
        for i in strs:
            j="".join(sorted(i))
            an[j].append(i)
        return an.values()