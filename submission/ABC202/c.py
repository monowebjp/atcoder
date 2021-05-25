def main():
    from collections import Counter

    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    CntA = Counter(A)  # Aの値がそれぞれ何回出現するか、数えてくれます
    ans = 0

    for x in C:
        y = x - 1  # 1始まりで入力が与えられますが、indexに合わせて0始まりになおします
        k = B[y]  # B_{C_j} の値です。
        ans += CntA[k]  # A に k が出現する回数だけ答えに足します
    print(ans)


if __name__ == '__main__':
    main()