def to_alternating_case(string):
    i=0
    while i<len(string):
        if string[i].islower():
            print(string[i].upper(),end="")
        else:
            print(string[i].lower(),end="")
        i+=1
to_alternating_case("heLLo woRlD")



