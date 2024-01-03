# O(n^3) time complexity
# O(min(n,m)) space complexity
def blute_force(s):
    def check_same_char(start, end):
        chars = set()
        for i in range(start, end + 1):
            c = s[i]
            if c in chars:
                return False
            chars.add(s[i])
        return True

    n = len(s)
    ans = 0
    for i in range(n):
        for j in range(i, n):
            if check_same_char(i, j):
                ans = max(ans, j - i + 1)

    return ans


from collections import Counter


# O(2n) time complexity
# O(min(n,m)) space complexity
def sliding_window(s):
    chars = Counter()
    left = 0
    right = 0
    ans = 0

    while right < len(s):
        r = s[right]
        chars[r] += 1

        while chars[r] > 1:
            l = s[left]
            chars[l] -= 1
            left += 1

        ans = max(ans, right - left + 1)

        right += 1

    return ans


# O(n) time complexity
# O(min(n,m)) space complexity
def two_pointers(s):
    ans = 0
    hash_map = {}
    s_start = 0
    for i, i_s in enumerate(s):
        if i_s in hash_map:
            ans = max(ans, i - s_start)
            s_start = max(hash_map[i_s] + 1, s_start)
        hash_map[i_s] = i

    ans = max(ans, len(s) - s_start)

    return ans


# O(n) time complexity
# O(m) space complexity
def assumption_charset(s):
    chars = [None] * 128

    left = 0
    right = 0
    ans = 0

    while right < len(s):
        r = s[right]

        index = chars[ord(r)]
        if index is not None and left <= index < right:
            left = index + 1

        ans = max(ans, right - left + 1)

        chars[ord(r)] = right
        right += 1

    return ans


if __name__ == "__main__":
    s = "abcabcbb"
    print(blute_force(s))
    print(sliding_window(s))
    print(two_pointers(s))
    print(assumption_charset(s))
