vowels=['a','e','i','o','u']
word=input("please input a word: ")
found=[]
for letter in word:
    if letter in vowels:
        found.append(letter)
for vowel in found:
    print(vowel)
