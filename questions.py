string = "Hello World"
rev = string[::-1]
print(rev)

string = "madam"
if(string == string[::-1]):
    print("Palindrome")
else:
    print("Not palindrome")

string = "Programming"
vowels = 'aeiouAEIOU'
count = sum(1 for char in string if char in vowels)
print(count)

import string
input = "Hello,world!"
new = ''.join(char for char in input if char not in string.punctuation)
print(new)

sentence = "python programming is fun and engaging"
longest_word = max(sentence.split(), key=len)
print(longest_word)

sentence = "python programming is fun and engaging"
word = sentence.split()
long = " "
for i in word:
    if len(i) > len(long):
        long = i
print(long)

lists = [[1, 2, 3], [2, 3, 4], [4, 5, 3]]
common = lists[0]
for lst in lists[1:]:
    common = [x for x in common if x in lst]
print(common)

def pascal_triangle(n):
    prev = [1]
    print(prev)
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(prev[j-1] + prev[j])
        row.append(1)
        print(row)
        prev = row

pascal_triangle(5)

string = "Hello World"
position = [index for index, char in enumerate(string) if char == "o"]
print(position)

string = "Hello World"
character = "o"
position = []
index = string.find(character)
while index != -1:
    position.append(index)
    index = string.find(character, index + 1)
print(position)

string = "hello world"
position = []
for i in range(len(string)):
    if string[i] == "o":
        position.append(i)
print(position)

string.find("o")

string = "hello"
common = [index for index, char in enumerate(string) if char == "l"]
print(common)

string = "oscar man shrestha"
occurance = []
for i in range(len(string)):
    if string[i] == "a":
        occurance.append(i)
print(occurance)

def second_largest(n):
    largest = max(n)
    n = [x for x in n if x != largest]
    return max(n)

print(second_largest([1, 2, 3, 4]))

def unique_list(n):
    seen = set()
    return [x for x in n if x not in seen and not seen.add(x)]

print(unique_list([1, 2, 2, 3, 4]))

data = (1, [2, 3], 4)
data[1][0] = 5
data[1][1] = 6
print(data)

def flatten_tuple(tup):
    return tuple(item for sub in tup for item in sub)

tup = ((1, 2), (3, (4, 5)))
print(flatten_tuple(tup))
