class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        route = {} # key : index(0,1,2,3...)
        groups = [] # [[a,b],[c],[d,e]]

        for word in strs:
            key = "".join(sorted(word))
            if key not in route: 
                route[key] = len(groups)
                groups.append([])
            groups[route[key]].append(word)

        return groups