import time
import pyotp
import qrcode

key=pyotp.random_base32()
print(key)

key = "MySecretKeyShouldHaveEnoughCharacters"
totp=pyotp.TOTP(key)
print(totp.now())

input = input("Enter the otp:")
print(totp.verify(input))

counter=0
hotp = pyotp.HOTP(key)
print(hotp.at(0))
print(hotp.at(1))
print(hotp.at(2))
print(hotp.at(3))
print(hotp.at(4))

for _ in range(5):
    print(hotp.verify(input("Enter Code:"), counter))
    counter+=1

uri = pyotp.totp.TOTP(key).provisioning_uri(name="ChinniPavani", issuer_name="2fa Project")
print(uri)
qrcode.make(uri).save("totp.png")

totp = pyotp.TOTP(key)
while True:
    print(totp.verify(input("enter code:")))