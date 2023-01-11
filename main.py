import bcrypt
print("Enter password")
password = input().encode('utf-8')
hashpassword = bcrypt.hashpw(password,bcrypt.gensalt())
print("Hashpassword",'\n',hashpassword)
