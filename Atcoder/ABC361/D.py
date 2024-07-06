import io
import sys
import collections


def debug_input():
    _INPUT = """\
14
BBBWBWWWBBWWBW
WBWWBBWWWBWBBB
    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    N = int(input())
    S = input()
    T = input()

    S_w = 0
    S_b = 0
    for stone in S:
        if stone == "W":
            S_w += 1
        else:
            S_b += 1

    T_w = 0
    T_b = 0
    for stone in T:
        if stone == "W":
            T_w += 1
        else:
            T_b += 1

    if S_w != T_w or S_b != T_b:
        print(-1)
        return

    S += ".."
    T += ".."
    seen = set(S)
    queue = collections.deque([(S, 0, N)])

    while queue:
        state, count, brank = queue.popleft()

        if state == T:
            print(count)
            return

        for i in range(N + 1):
            if not (state[i] != "." and state[i + 1] != "."):
                continue
            new_state = list(state)
            new_state[brank], new_state[i] = new_state[i], new_state[brank]
            new_state[brank + 1], new_state[i + 1] = state[i + 1], state[brank + 1]
            new_state = "".join(new_state)

            if new_state in seen:
                continue
            seen.add(new_state)
            queue.append((new_state, count + 1, i))
    print(-1)


if __name__ == "__main__":
    # debug_input()
    main()
