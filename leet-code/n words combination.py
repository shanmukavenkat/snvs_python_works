def all_unique_combinations(words, n):
    words = sorted(words)
    word_combinations = set()

    combinations = []
    for i in range(len(words)):
        combinations.append([i])

    iteration = 0
    while iteration < n - 1:
        new_combinations = []
        for combination in combinations:
            for i in range(combination[-1] + 1, len(words)):
                new_combination = combination.copy()
                new_combination.append(i)
                new_combinations.append(new_combination)
        combinations = new_combinations
        iteration += 1

    for combination in combinations:
        word_combination = []
        for i in combination:
            word_combination.append(words[i])
        word_combinations.add(' '.join(word_combination))

    return sorted(list(word_combinations))


words = input().strip().split()
n = int(input())
all_combinations = all_unique_combinations(words, n)
for combination in all_combinations:
    print(combination)