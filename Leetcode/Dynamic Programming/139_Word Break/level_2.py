class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp_str = [False] * (len(s) + 1)
        dp_str[0] = True

        for i in range(len(s) + 1):
            for j_word in wordDict:
                if i < len(j_word):
                    continue

                if dp_str[i - len(j_word)]:
                    if j_word == s[i - len(j_word) : i]:
                        dp_str[i] = True
                        break

        return dp_str[-1]
