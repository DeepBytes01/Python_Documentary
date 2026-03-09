def main():
    user = input("Enter your username: ")
    hello(user)

def hello(username = "no input"):
    print(f"Hello {username}")

main()