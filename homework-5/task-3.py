path = 'homework-5/task-3.txt'
data = open(path, 'r')
string = ''

for line in data:
    string += line
data.close

path = 'homework-5/task-3_1.txt'
data = open(path, 'r')
str_2 = ''

for line in data:
    str_2 += line
data.close

def compression(string):
    compress = ''
    prev_char = ''
    count = 1

    for char in string:
        if char != prev_char:
            if prev_char:
                compress += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1

    compress += str(count) + prev_char
    return compress

def decompression(string):
    decompress = ''
    count = ''

    for char in string:
        if char.isdigit():
            count += char
        else:
            decompress += char * int(count)
            count = ''

    return decompress

print(compression(string))
print(decompression(str_2))