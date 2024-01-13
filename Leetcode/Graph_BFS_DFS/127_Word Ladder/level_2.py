import collections


def main(beginWord, endWord, wordList):
    if endWord not in wordList:
        return 0

    all_combo_dict = collections.defaultdict(list)
    for word in wordList:
        for i in range(len(beginWord)):
            all_combo_dict[word[:i] + "*" + word[i + 1 :]].append(word)

    seen = set()
    queue = collections.deque()
    queue.append((beginWord, 1))

    while queue:
        curr_word, level = queue.popleft()
        for i in range(len(beginWord)):
            intermediate_word = curr_word[:i] + "*" + curr_word[i + 1 :]
            for next_word in all_combo_dict[intermediate_word]:
                if next_word == endWord:
                    return level + 1
                if next_word not in seen:
                    queue.append((next_word, level + 1))
                    seen.add(next_word)
            all_combo_dict[intermediate_word] = []

    return 0


if __name__ == "__main__":
    strs = ["hot", "dot", "dog", "lot", "log", "cog"]
    beginWord = "hit"
    endWord = "cog"
    print(main(beginWord, endWord, strs))
