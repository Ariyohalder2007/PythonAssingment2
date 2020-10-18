s='Ariyo eye egg ariyo '

def Find(s):
    word=''
    for i in s:
        if i!=' ':
            word+=i
        elif i==' ':
            if len(word) > 3:
                print(word)
            word=''

Find(s)