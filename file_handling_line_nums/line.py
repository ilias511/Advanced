with open("text.txt","r") as file,open('result.txt','w') as result:
    index = 1
    marks = {'.','?','!',',',':',';','-','-','‘',"'"}
    lines = file.read().splitlines()
    for line in lines:
        letters = 0
        punctuation_marks = 0
        for ch in line:
            if ch in marks:
                punctuation_marks+=1
            elif ch.isalpha():
                letters+=1
        result.write (f"Line {index}: {line.strip()} ({letters})({punctuation_marks})")
        result.write('\n')
        index+=1