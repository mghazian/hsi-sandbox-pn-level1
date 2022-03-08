# 2:45:57 Emoji Converter
message = input(">>> ")

emoji_mapping = {
    ")": ":happy:",
    "(": ":sad:",
    "@": ":angry:"
}

words = message.split(" ")
print(message)
print(words)

output = ""
for w in words:
    output = output + emoji_mapping.get(w, w) + " "

print (output)