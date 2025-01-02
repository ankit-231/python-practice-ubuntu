if __name__ == "__main__":
    n = int(input().strip())

    arr = list(map(str, input().rstrip().split()))
    arr = arr[::-1]
    joined = " ".join(arr)
    print(joined)
