text = input()

text_dict = {}
for ch in text:
    if ch in text_dict:
        text_dict[ch]+=1
    else:
        text_dict[ch]=1

for key,value in sorted(text_dict.items()):
    print(f'{key}: {value} time/s')