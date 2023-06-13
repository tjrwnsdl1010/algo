abc = input()

if abc.islower():
    print(f"{abc}(ASCII: {ord(abc)}) => {chr(ord(abc)-32)}(ASCII: {ord(abc)-32})")
elif abc.isupper():
    print(f"{abc}(ASCII: {ord(abc)}) => {chr(ord(abc)+32)}(ASCII: {ord(abc)+32})")
else:
    print(ord(abc))