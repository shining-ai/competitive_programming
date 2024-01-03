def convert(s, numRows):
    ans = ""
    s_rows = [""] * (numRows + 1)
    add_num = 1
    row = 1

    if numRows == 1:
        ans = s
    else:
        for i in range(len(s)):
            s_rows[row] += s[i]
            row += add_num
            if row == numRows or row == 1:
                add_num *= -1

        for i_str in s_rows:
            ans += i_str

    return ans


if __name__ == "__main__":
    s = "PAYPALISHIRING"
    numRows = 3

    print(convert(s, numRows))


# 2:
# 1 3 5 7 9 11 13 15 17 19 21 23 25 27 29
# 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30

# 3:
# 1   5   9
# 2 4 6 8 10
# 3   7   11

# 4:
# 1     7      13
# 2   6 8   12 14
# 3 5   9 11   15
# 4     10     16

# 5:
# 1       9         17
# 2     8 10     16 18
# 3   7   11   15   19
# 4 6     12 14     20
# 5       13        21
