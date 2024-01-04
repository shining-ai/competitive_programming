from math import ceil


def SimulateZig_ZagMovement(s, numRows):
    if numRows == 1 or numRows >= len(s):
        return s

    ans = ""
    s_rows = [""] * (numRows + 1)
    step = 1
    index = 1

    for i_char in s:
        s_rows[index] += i_char
        index += step
        if index == numRows or index == 1:
            step *= -1

    for i_str in s_rows:
        ans += i_str

    return ans


if __name__ == "__main__":
    s = "PAYPALISHIRING"
    num_rows = 3

    print(SimulateZig_ZagMovement(s, num_rows))
