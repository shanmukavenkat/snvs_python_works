def sockMerchant(n,arr):

    color_count = {}

    for color in arr:
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1


    pairs = 0
    for count in color_count.values():
        pairs += count//2

    return pairs

n = int(input())
arr = list(map(int, input().split()))
print(sockMerchant(n, arr))