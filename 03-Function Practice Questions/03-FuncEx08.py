def paper_doll(text):
    new_text = ''
    for i in text:
        new_text += i*3
    return new_text

print(paper_doll('Hello'))
print(paper_doll('mississipi'))
