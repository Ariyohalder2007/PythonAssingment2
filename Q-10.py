l=['Place', 'kingdom', 'Palace']
count=0
for i in l:
    word=i.lower()
    if word[0]=='p':
        count+=1
if count>1:
    print('Match Found')
else:
    print('No Match Found!!!')