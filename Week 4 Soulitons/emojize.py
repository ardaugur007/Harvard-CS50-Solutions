import emoji

text = input("Input: ")

textmoji = emoji.emojize(text, language = 'alias')
print("Output:", textmoji)
