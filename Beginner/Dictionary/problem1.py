'''Create a list of your friends' names. The list should have at least 5 names.
Create a list of tuples. Each tuple should contain a friend's name and the length
of the name.
For example, if someone’s name is Aditya, the tuple would be: ('Aditya', 6)'''


friends = ["Aryan", "Suman", "Priya", "Rohit", "Anjali"]

friends_with_length = []
for name in friends:        # yahan for loop bahar liya
    friends_with_length.append((name, len(name)))

print(friends_with_length)
