import io
import sys


def debug_input():
    _INPUT = """\
3 2 2
3 1 2 3 o
2 2 3 x

    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    N, M, K = map(int, input().split())
    candidates = []
    for i in range(2**N):
        candidates.append(format(i, "b").zfill(N))

    for i in range(M):
        next_candidates = []
        input_values = input().split()
        c = int(input_values[0])
        A = input_values[1:-1]
        R = input_values[-1]
        while candidates:
            bin_candidate = candidates.pop()
            count = 0
            if R == "o":
                for a in A:
                    count += int(bin_candidate[int(a) - 1])
                    if count >= K:
                        next_candidates.append(bin_candidate)
                        break
            else:
                for a in A:
                    count += int(bin_candidate[int(a) - 1])
                    if count >= K:
                        break
                else:
                    next_candidates.append(bin_candidate)

        candidates = next_candidates
    print(len(candidates))


if __name__ == "__main__":
    # debug_input()
    main()
