import random

passlen = int(input("Enter the length of password.."))
alphabet = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

password = "".join(random.sample(alphabet,passlen))

print(password)
