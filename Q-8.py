a=input("Enter the num: ")
def numMatch(num):
    try:
        if int(num):
            print('It is a number')
    except:
        print('Not a number')
    
numMatch(a)
