def word_split(phrase, list_of_word, output = None):
    if output is None:
        output = []
    
    for word in list_of_word:
        if phrase.startswith(word):
            output.append(word)

            return word_split(phrase[len(word): ], list_of_word, output)
    
    return output

print(word_split('themanran', ['the', 'ran', 'man']))

