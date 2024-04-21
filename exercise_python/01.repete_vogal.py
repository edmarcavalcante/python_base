"""
Create a program that ask to user to type a or more words and
print each word with its vogal duplicate

ex:
python repete_vogal.py
'Type a word (or enter to exit): Python
Pythoon
'Type a word (or enter to exit): Edmar
EEdmaar
"""

while True:
    word = input("Type a word (or enter to exit): ").strp()
    if word == "":
        break
    else:
        pass
    vogal = ["a","e","i","o","u"]
    new_word = ""
    for i in list(word):
        if i.lower() in vogal:
            
            new_word += i*2
        else:
            new_word += i
    print(new_word.capitalize())


