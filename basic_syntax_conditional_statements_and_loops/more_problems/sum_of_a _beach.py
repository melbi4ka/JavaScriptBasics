str_word = input().lower()
counter = 0

if "water" in str_word:
    result = str_word.count("water")
    counter += result
if "sand" in str_word:
    result = str_word.count("sand")
    counter += result
if "fish" in str_word:
    result = str_word.count("fish")
    counter += result
if "sun" in str_word:
    result = str_word.count("sun")
    counter += result

print(counter)
