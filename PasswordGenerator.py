import random
import string

A = string.ascii_uppercase
B = string.ascii_lowercase
C = string.digits
D = "!@#$%^&*?"
E = string.ascii_letters

len_password = input("Enter the length of a Password : ")

if int(len_password) < 8:
    print("The length of a password must be atleast 8 characters!")
else:
    part_1 = random.choice(A) + random.choice(B) + random.choice(C) + random.choice(D)
    part_2 = ''.join(random.sample(part_1, len(part_1)))
    part_3 = ''.join([random.choice(C + D + E) for i in range(int(len_password) - 4)])
    part_4 = ''.join(random.sample(part_3, len(part_3)))
    part_5 = part_2 + part_4
    password = ''.join(random.sample(part_5, len(part_5)))
    print(password)