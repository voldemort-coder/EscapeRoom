def word_frequency(text):
    text=text.lower()
    words=text.split()
    freq={}                              #creeaza un dictionr gol
    for word in words:
        if word in freq:
            freq[word] +=1
        else:
            freq[word]=1
    return freq
while True:
    text = input("Scrie un text: ")
    print(word_frequency(text))