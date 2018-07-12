is_rich = True
is_happy = True

if is_rich and is_happy:
    print("You are rich and happy. That's nice!")
elif is_rich and not is_happy:
    print("You are rich, but not happy.")
elif not is_rich and is_happy:
    print("You are poor, but happy. Good for you.")
else:
    print("Sorry. You are poor and sad.")


