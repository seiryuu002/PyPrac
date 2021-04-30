def master_yoda(sentence):
    words = sentence.split()
    words.reverse()
    print(words)
    new_sentence = ' '.join(words)
    return new_sentence


print(master_yoda("youare wrong"))

