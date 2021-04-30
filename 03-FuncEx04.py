def old_macdonald(name):
    text = []
    for i in range(len(name)):
        if i == 0 or i == 3:
            text.append(name[i].upper())
        else:
            text.append(name[i])
    return ''.join(text)


print(old_macdonald('macdonald'))
