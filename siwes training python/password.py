#login_details = {
#   "username": "roqeebat",
 #   "password": "password01"

#}
#user_name = input("Enter your username: ")
#pass_word = input("Enter your password: ")
#if user_name == login_details["username"] and pass_word == login_details["password"]:
 #   print("Login Successful")
#else:
 #   print("Incorrect Username or Password")


login = {
    
}
print("\n Create Facebook Account Below \n")

login["full_name"] = input("Full_Name: ")
login["pass_word"] = input("Create a Password: ")
login["phone_number"] = input("Enter your Number: ")
login["code"] = int(input("Code sent to your Number: "))
login["user_name"] = input("Enter your Username: ")

print("\n You Have Created Your Facebook Account Successfully\n")

user_name = input("Enter your username: ")
pass_word = input("Enter your password: ")
if user_name == login["user_name"] and pass_word == login["pass_word"]:
    print("Login Successful")
else:
    print("Incorrect Username or Password")
