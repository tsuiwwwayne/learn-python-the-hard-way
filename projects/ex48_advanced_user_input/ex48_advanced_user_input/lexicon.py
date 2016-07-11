# Learn Python the Hard Way
# Exercise 48 - Advanced User Input, Lexicon

direction = ["north", "south", "east", "west",
              "down", "up", "left", "right", "back"]

verb = ["go", "stop", "kill", "eat"]

stop = ["the", "in", "of", "from", "at", "it"]

noun = ["door", "bear", "princess", "cabinet"]

lexicons = [direction, verb, stop, noun]
lexicons_names = ["direction", "verb", "stop", "noun"]

def scan(sentence):
    words = sentence.split()
    result = []
    index_position = 0
    for word in words:

        found_word = False

        # check if it is a valid number
        if not found_word:
            try:
                number = int(word)
                result.append(("number", number))
                found_word = True
            except ValueError:
                pass


        # check amongst list of list of approved words
        if not found_word:
            for lexicon in lexicons:
                name = lexicons_names[index_position]
                if word in lexicon:
                    found_word = True
                    result.append((name, word))
                else:
                    pass
                index_position += 1
            index_position = 0

        # if word is not an approved word and not an valid number, the word is not valid
        if not found_word:
            result.append(("error", word))

    return result
