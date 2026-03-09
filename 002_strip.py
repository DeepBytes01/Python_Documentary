print("Not stripped!")
name = input("Enter your name: ")
print(f"Hello!, {name}")

print("Stripped!")
name = input("Enter your name: ")
name = name.strip() #strip white space
print(f"Hello!, {name}")