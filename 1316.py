num_inputs = int(input())

lines = []
for i in range(num_inputs):
    lines.append(input())

group_words_count = 0
for word in lines:
    unique_chars = []
    for i, char in enumerate(word):
        if char not in unique_chars:
            unique_chars.append(char)
        elif (char in unique_chars) and (unique_chars[-1] != char):
            break

        if i == len(word) - 1:
            group_words_count += 1

print(group_words_count)