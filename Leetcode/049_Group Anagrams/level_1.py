from collections import defaultdict


def solve_1(strs):
    hash_map = defaultdict(list)
    ans = []

    for i_str in strs:
        hash_map["".join(sorted(i_str))].append(i_str)

    for key in hash_map:
        ans.append(hash_map[key])

    return ans


if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(solve_1(strs))
