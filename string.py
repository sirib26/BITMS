names="balaji srinivasan"
print(names)
print(names[:])
print(names[2:])
print(names[-1:])
print(names[-5:-1])
print(names[::-1])
'''scope resolution operator with only step values reverses string'''

char="siri"
vowels="aeiou"
res=[char for char in char if char in vowels]
print(res)
print(names[::-3])
'''step value starts from reverse and skips 2 values'''
sep='-'.join(names[::2])
print(sep)