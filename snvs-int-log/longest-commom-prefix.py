## o(n)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        for i in range(len(str[0])):
            for s in strs:
                if i== len(s) or s[i] != str[0][i]:
                    return res
            res += str[0][i]
        return res
    