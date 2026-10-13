import random
import string 

pass_len = 12
charValues = string.ascii_letteres + string.punctuation + string.digits

password = ""
for i in range(pass_len):
  password +=  "".join[random.choice(charValues)]

printt("Your random password is", password)
