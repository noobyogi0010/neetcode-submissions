class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join([str(len(s))+"#"+s for s in strs])

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i<len(s):
            j = i
            while j<len(s) and s[j] != "#":
                j += 1
            wordLength = int(s[i:j])
            res.append(s[j+1:j+1+wordLength])

            i = j + 1 + wordLength

        return res
