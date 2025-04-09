def generate_2_combinations(words):
    words = sorted(words)
    items = list(range(len(words)))
    combinations_1 = []
    for item in items:
        combinations_1.append([item])  # Generating one word combinations
    # Generating two words combinations by adding one more word to one word combinations
    combinations_2 = []
    for combination in combinations_1:
        for item in items:
            if item > combination[-1]:
                combinations_2.append(combination + [item])

    word_combinations = []
    for combination in combinations_2:
        word_combination = []
        for index in combination:
            word_combination.append(words[index])
        word_combinations.append(tuple(word_combination))
    return sorted(set(word_combinations))


words = input().split()
all_combinations = generate_2_combinations(words)
for combination in all_combinations:
    print(' '.join(combination))