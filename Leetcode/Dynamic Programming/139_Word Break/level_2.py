class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp_s = [False] * (len(s) + 1)
        dp_s[0] = True

        for i in range(len(s) + 1):
            for j_word in wordDict:
                word_length = len(j_word)

                if i < word_length:
                    continue

                if s[i - word_length : i] == j_word:
                    if dp_s[i - word_length]:
                        dp_s[i] = True
                        break

        return dp_s[-1]
