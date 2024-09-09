import demoji

text = input("Enter text with emojify: ")

emojis = demoji.findall(text)

if emojis:
    print("Emojis found:", emojis)
else:
    print("No emojis found.")
