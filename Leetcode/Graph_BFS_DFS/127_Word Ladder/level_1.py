import collections


# timeout
def solve_1(beginWord, endWord, wordList):
    if endWord not in wordList:
        return 0

    def is_transformable(word1, word2):
        diff = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                diff += 1
        return diff == 1

    net = [set() for _ in range(len(wordList))]
    for i in range(len(wordList)):
        for j in range(i + 1, len(wordList)):
            if is_transformable(wordList[i], wordList[j]):
                net[i].add(j)
                net[j].add(i)

    seen = set()
    queue = collections.deque()
    queue.append((beginWord, 1))
    while queue:
        word, level = queue.popleft()
        if word == endWord:
            return level
        for i in range(len(wordList)):
            if i not in seen and is_transformable(word, wordList[i]):
                queue.append((wordList[i], level + 1))
                seen.add(i)

    return 0


# O(M^2 * N) time complexity
# O(M^2 * N) space complexity
def solve_2(beginWord, endWord, wordList):
    if endWord not in wordList:
        return 0

    L = len(beginWord)

    all_combo_dict = collections.defaultdict(list)
    for word in wordList:
        for i in range(L):
            all_combo_dict[word[:i] + "*" + word[i + 1 :]].append(word)

    seen = set()
    queue = collections.deque()
    queue.append((beginWord, 1))

    while queue:
        curr_word, level = queue.popleft()
        for i in range(L):
            intermediate_word = curr_word[:i] + "*" + curr_word[i + 1 :]
            for word in all_combo_dict[intermediate_word]:
                if word == endWord:
                    return level + 1
                if word not in seen:
                    queue.append((word, level + 1))
                    seen.add(word)
            all_combo_dict[intermediate_word] = []

    return 0


if __name__ == "__main__":
    strs = ["hot", "dot", "dog", "lot", "log", "cog"]
    beginWord = "hit"
    endWord = "cog"
    print(solve_1(beginWord, endWord, strs))
    print(solve_2(beginWord, endWord, strs))
