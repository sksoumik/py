def reverse_text(text):
    # base condition
    if text == "":
        return text
    else:
        return text[-1] + reverse_text(text[0:-1])


text = "abcd"
rev = reverse_text(text)
print(rev)