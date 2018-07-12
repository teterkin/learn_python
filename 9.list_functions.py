lucky_numbers = [42, 8, 15, 16, 23, 4]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.extend(lucky_numbers)
print(friends)
for idx in range(6):
    friends.pop()
print(friends)
friends.append("Creed")
friends.insert(1, "Kelly")
friends.remove("Jim")
print(friends)
print(friends.index("Oscar"))
friends.append("Oscar")
print(friends)
print(friends.count("Oscar"))
friends.sort()
print(friends)
friends2 = friends.copy()
print(friends2)
friends.clear()
print(friends)
lucky_numbers.reverse()  # It is not sorting, it just reverses.
print(lucky_numbers)
lucky_numbers.sort()  # This one is sorting
print(lucky_numbers)
