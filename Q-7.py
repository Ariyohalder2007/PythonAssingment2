# def textMatch(text):
#     n=len(text)-1
#     c=0
#     for i in range(1, n):
#         if text[i]=='z' or text[i]=='Z':
#             c=1
#         else:
#             c=0
#     if c==1:
#         print('Match Found!!')
#     else:
#         print('No match found!!')
# print(textMatch('HiiZhii'))
# print(textMatch('Hiizhii'))
# print(textMatch('ZHiihiiZ'))

import re
def text_match(text):
        patterns = '\Bz\B'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("The quick brown fox jumps over the lazy dog."))
print(text_match("Python Exercises."))