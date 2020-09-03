vowels=set('aeiou')
word=input("Please input a word: ")
found=vowels.intersection(set(word))
for vowel in found:
    print(vowel)
