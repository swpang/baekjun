input_string = input()

croatian_alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
croatian_start = ['c', 'd', 'l', 'n', 's', 'z']

count = 0

idx = 0
while idx < len(input_string):
    if input_string[idx] not in croatian_start:
        count = count + 1
        idx = idx + 1
    else:
        if input_string[idx:idx+2] in croatian_alphabet:
            count = count + 1
            idx = idx + 2
        elif input_string[idx:idx+3] in croatian_alphabet:
            count = count + 1
            idx = idx + 3
        else:
            count = count + 1
            idx = idx + 1

print(count)
