# trying to create password encryption



# for the encrypton of password we are using the base64 module
import base64

def pass_encode(password):
    encrypt = base64.b64encode(password.encode())
    print(f"the encrypted password is: {encrypt}")

user_pass = input("Enter a password that you want to encode: ")
pass_encode(user_pass)


# what if we'll decode the password using the base 64

def decode_pass(x):
    decodeed = base64.b64decode(x)

    dec= decodeed.decode()
    print(f"the decoded password is {dec}")

a= input("Enter the password you want to decode: ")
decode_pass(a)