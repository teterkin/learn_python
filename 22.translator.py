# Giraffe language = any vowels become g.

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation += "G"
            else:
                translation += "g"
        else:
            translation += letter
    return translation


print(translate("cat"))
print(translate("dog"))
print(translate(input("Enter a phrase: ")))