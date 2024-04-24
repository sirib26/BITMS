password="siri"
uemail="siri@gmail.com"
email=str(input("enter the email:"))
passwd=str(input("enter the password:"))
otp1=1234
'''if(email==uemail and passwd==password):
    print("login successful")
else:
    print("login unsuccesful")'''
if(email==uemail):
    if(passwd==password):
        print("login successful")
        print("otp : 1234")
        otp=int(input("enter the otp"))
        if(otp==otp1):
            print("transcation successful")
        else:
            print("transcation failed")
    else:
        print("login failed due to incorrect password")
else:
    print("login failed due to incorrect email")