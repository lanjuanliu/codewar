def smash(words):
    i=0
    b=''
    while i<len(words):
            b+=" "+words[i]
            i+=1
    return "'"+b+"'"
print(smash(["hello"]))