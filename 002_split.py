name = input("Enter name: ").strip().title()
first, last = name.split(" ") #first arg stored in first, second arg stored in last
full_name = first + last
print(f"Hello!, {first}")
print(f"Hello!, {full_name}")