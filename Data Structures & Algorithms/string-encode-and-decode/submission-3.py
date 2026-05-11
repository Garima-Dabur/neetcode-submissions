class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for char in strs:
            l = str(len(char))
            s += l + "#" + char
        return s
            

    def decode(self, s: str) -> List[str]:
        i = 0
        final = []
        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            string = s[j + 1: j + 1 + length]
            final.append(string)
            i = j + 1 + length
        return final 


