character_name = "Tom"
# character_name = "Linda"
character_age = 50
isMale = True
# isMale = False
if isMale:
    character_gender = "man"
    he_she = "He"
else:
    character_gender = "woman"
    he_she = "She"
print("There once was a " + character_gender + " named " + character_name + ",")
print(he_she.lower() + " was " + str(character_age) + " years old.")
print(he_she + " really liked the name " + character_name + ",")
print("but " + he_she.lower() + " didn't like being " + str(character_age) + ".")
if isMale:
    print(he_she + " was a strong man.")
else:
    print(he_she + " was a pretty woman.")
