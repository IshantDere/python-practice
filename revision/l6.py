words = ["apple", "banana", "orange", "grape", "umbrella", "fig", "kiwi", "elephant", "apricot"]

vowel_words = []
long_words = []

for j in words:
   first = j[0].lower()
   
   if first in ['a', 'e', 'i', 'o', 'u']:
    vowel_words.append(j)

# print(vowel_words)

    if len(j) > 5:
        long_words.append(j)

# print(long_words)

print("original word:", words, len(words))
print("vowel words:", vowel_words, len(vowel_words))
print("word more than 5 letters:", long_words, len(long_words))