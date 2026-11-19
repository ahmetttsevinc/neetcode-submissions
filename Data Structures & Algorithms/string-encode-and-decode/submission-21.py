class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        i = 0
        final_list = []

        while i<len(s):
            j = i
            while s[j] != "#" and j<len(s):
                j += 1
            lenght = int(s[i:j])
            final_list.append(s[j+1:j+1+lenght])
            i = j + 1 + lenght



        return final_list
