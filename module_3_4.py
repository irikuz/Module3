def single_root_words(root_word, *other_words):
    root_word = root_word.lower()
    same_words = []
    for word in other_words:
        word = word.lower()
        if root_word in word or word.startswith(root_word + ' ') or word.endswith(
                ' ' + root_word) or word == root_word or word in root_word:
            same_words.append(word)
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
