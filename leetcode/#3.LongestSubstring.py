def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    d = {}
    start = 0
    res = 0

    for i, ch in enumerate(s):
        if ch in d and start <= d[ch]:
            start = d[ch] + 1
        else:
            res = max(res, i - start + 1)
        d[ch] = i
    return res

if __name__ == '__main__':
    print(lengthOfLongestSubstring('abcabdab'))