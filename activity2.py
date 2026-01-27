def match_words(words):
    ctr = 0
    list = []
    for i in words:
        if len(i) > 1 and i[0] == i[-1]:
            ctr += 1
            list.append(i)
    print(list)
    return ctr
count = match_words(['abc','cfc','aba','1221'])
print("number of words having first and last character same:", count)