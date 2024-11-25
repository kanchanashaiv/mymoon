fname=input("enter a file name")
word_count=0
with open (fname,"r")as f:
    for line in f:
        words=line.split()
        word_count+=len(words)
print(f"number of words in the file is :{word_count}")
