message='Message is impossible' \
        'wwqerty'
count={}

for ch in message:
    count.setdefault(ch,0)
    count[ch]=count[ch]+1

print(count)