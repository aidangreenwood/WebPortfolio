# Ask for the word of the day
word = input("\nWhat is the word of the day?: ")

# Ask for the pronunciation
pronounce = input("How do you pronounce it?: ")

# Ask for part of speech
pos = input("What is the part of speech?: ")

# Ask for the definition(s)
definitions = []
definition = input("what are the definitions or definition?: ")
# Tell the code what to split for, split it, then append that split list to the original list
definitions = [d.strip() for d in definition.split(".") if d.strip()]

# Ask for the origin of the word
more_info = []
origin = input("What is the origin?: ")
# Tell the code what to split for, split it, then append that split list to the original list
more_info = [m.strip() for m in origin.split(";") if m.strip()]

# Ask for example sentence(s)
sentences = []
example_sentences = input("What is an or what are some example sentences?: ")
# Tell the code what to split for, split it, then append that split list to the original list
sentences = [s.strip() for s in example_sentences.split(".") if s.strip()]

# Format it into a copyable text
print("\nWord:")
print(word.title())
print(pronounce)
print("Definition:")
print(pos)
for i in definitions:
    print("* ", i.strip().capitalize() + ".")
print("More Information:")
for i in more_info:
    print("* ", i.strip())
print("Sentence example(s):")
for i in sentences:
    print("* ", i.strip().capitalize() + ".")
print()