def single_root_words(root_word, *other_words):
    same_words = []
    z = root_word.lower()
    for i in range(len(other_words)):
        a = str(other_words[i].lower())
        if z in other_words[i].lower():
            same_words.append(a)
        else:
            if other_words[i].lower() in z:
                same_words.append(a)
            else:
                continue
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
