def leetspeak_variants(word):
    subs = {
        'a': ['4', '@'],
        'e': ['3'],
        'i': ['1', '!'],
        'o': ['0'],
        's': ['5', '$'],
        't': ['7']
    }

    variants = set([word])

    for i, char in enumerate(word):
        if char.lower() in subs:
            for replacement in subs[char.lower()]:
                new_word = word[:i] + replacement + word[i+1:]
                variants.add(new_word)

    return variants
