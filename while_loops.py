
i = 10
while i < 5:
    print(i)
    i += 1
print()

while True:
    user_name = input("What is your name? (or q to quit) ")
    if user_name == 'q':
        break  # exit loop
    elif user_name == '':
        continue  # go back to top
    print("Hello,", user_name)
