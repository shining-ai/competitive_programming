s = "abba"

ans = 0
cnt = 0
hash_map = {}
s_start = 0

for i, i_s in enumerate(s):
    if i_s in hash_map:
        ans = max(ans, i - s_start)
        s_start = max(hash_map[i_s] + 1, s_start)
        hash_map[i_s] = i
    else:
        hash_map[i_s] = i

ans = max(ans, len(s) - s_start)
print(ans)
