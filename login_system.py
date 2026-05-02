#login system

Usename = input("Enter username ")
Passward = input("Enter passward")
if(len(Passward)>=8):
    print("right")
else:
    print("Passward must be of minimum 8 charecters" )
Captcha = "24dgyY"
print(Captcha)
a = input("Enter Captcha")
if(a == "24dgyY"):
    print("Login Successful")
else:
    print("Wrong Credentials")