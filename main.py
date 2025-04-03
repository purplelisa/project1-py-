s = input()
flag = 'NO'
correct_letters = 'АВЕКМНОРСТУХ'

if 9 <= len(s) <= 10:
    letters = s[0] + s[4:6]
    digits = s[1:4] + s[7:]
    underscore = s[6]

    if digits.isdigit() and underscore == '_':
        flag = 'YES'

    for c in letters:
        if c not in correct_letters:
            flag = 'NO'
            break

print(flag)