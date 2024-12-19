def merge_string(word1, word2):
    merged_word = ""
    for i in range(0, min(len(word1), len(word2))):
        merged_word = merged_word + word1[i] + word2[i]


    if (len(word1) > len(word2)):
        max_word = word1
    else: 
        max_word = word2

    merged_word = merged_word + max_word[i+1:]
    return merged_word

print(merge_string("ab", "pqrs"))
