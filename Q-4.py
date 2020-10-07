import re
a='khhhchk6787670123'
b='@@!@#@#$$%$%&&*(***^$$^%^^*(**'
def check_str(string):
    charRe = re.compile(r'[^a-zA-Z0-9.]')
    string = charRe.search(string)
    return not bool(string)
print(check_str(a))
print(check_str(b))