input_string = input()
length_string = len(input_string)

idx = 0
char = input_string[idx]
is_palindrome = 0
while(char == input_string[-1-idx]):
    idx = idx + 1        
    if idx > length_string - 1:
        is_palindrome = 1
        break
    char = input_string[idx]
if is_palindrome:
    print(1)
else:
    print(0)
