def inverted_index(documents):
    index = {}
    for i, doc in enumerate(documents):
        for word in doc.lower().split():
            if word not in index:
                index[word] = set()
            index[word].add(i)
    return index
while True:
    print("Introdu documentele (câte unul pe linie). Scrie 'gata' pentru a termina:")
    documents = []
    while True:
        line = input()
        if line.lower() == "gata":
            break
        documents.append(line)

    print("Indexul inversat este:")
    print(inverted_index(documents))

    cont = input("Vrei să introduci alte documente? (da/nu): ").strip().lower()
    if cont != "da":
        print("La revedere!")
        break
