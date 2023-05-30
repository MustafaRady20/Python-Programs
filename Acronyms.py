# acronym is a short form of a word created of a long words or phrases
# such as NLP for Natural Language Processing


user_input = str(input("Enter a Phrase...!")).strip()
words = user_input .split(" ")
acronym = ""

for i in words:
    acronym += i[0].upper()

print(acronym)
