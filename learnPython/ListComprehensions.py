
#List Comprehensions is a very powerful tool, which creates a new list based on another list, in a single, readable line.
#For example, let's say we need to create a list of integers which specify the length of each word in a certain sentence, but only if the word is not the word "the".

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
wordLengths = []
for word in words:
    if word != "the":
        wordLengths.append(len(word))
print(words)
print(wordLengths)

#using list comprehension
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
wordLengths = [len(word) for word in words if word != "the"]
print(words)
print(wordLengths)

#exercise
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = [int(number) for number in numbers if number >= 0 ]
print(newlist)

#solution
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = [int(x) for x in numbers if x > 0]
print(newlist)