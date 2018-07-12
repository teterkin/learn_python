print("=======")
for letter in "Giraffe Academy":
    print("=  " + letter.upper() + "  =")
print("=======")

friends = ["Jim", "Karen", "Kevin"]
for friend in friends:
    print(friend)

for index in range(10):
    print(index)

print("---")

for idx in range(7, 10):
    print(idx)

for f in range(len(friends)):
    print("Friend " + str(f) + ": " + friends[f])

print("---")

for k in range(5):
    if k == 0:
        print("First iteration!")
    elif k == 4:
        print("Done!")
    else:
        print("+")


