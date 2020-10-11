def textMatch(text):
    t1="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    c=0
    t2=t1.lower()
    n= len(text)
    for i in range(0, n-1):
        for j in t2:
            if j == text[0]:
                c=1
        if text[i]=="_":
            for k in t2:
                if text[i+1]==k:
                    c=2
    if c==2:
        print('Match Found!!')
    else:
        print("No match Found!!")

textMatch("Hello_world")
textMatch("Hello_Wrld")