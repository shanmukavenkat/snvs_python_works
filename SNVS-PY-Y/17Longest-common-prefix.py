#here we are finding the words from the left to right
def longestCommonPrefix(self, strs):
    strs.sort()
    ##checking the first and the last one
    ans = ""
    for i in range(len(strs[0])):
        if strs[0][i] == strs[-1][i]:
            ans = ans + strs[0][i]
        else:
            break
    return ans





