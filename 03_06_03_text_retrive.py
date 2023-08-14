def text_retrieve(text):
    with open('03_06_03_generator_sample.txt', 'r') as f:
        for row in f:
            if text in row:
                yield row


retriever = text_retrieve('関数')
for text in text_retrieve('関数'):
    print(text)