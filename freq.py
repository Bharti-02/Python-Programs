sentence=input("enter Sentence:")
sentence=sentence.lower()
word_freq={}

for i in sentence:
    if i in word_freq:
        word_freq[i]+=1
    else:
        word_freq[i]=1
        
print("word_freqency:")
for i ,count in word_freq.items():
    print(f"{i}:{count}")

        