def adminAuth():
	print("Welcome admin!")
def user():
	print("Welcome user!")
admin = False
username = input("Username: ")
password = input("Password: ")
if username =="admin" and password == "admin":
	admin = True
if admin:
	adminAuth()
else:
	user()

