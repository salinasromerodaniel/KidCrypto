import struct
import fileinput
import math


lines = []
for line in fileinput.input():
    lines.append(line)
option = lines[0].strip()
a = int (lines[1].strip())
b = int (lines[2].strip())
A = int (lines[3].strip())
B = int (lines[4].strip())
message = int (lines[5].strip())

M = (a*b) - 1
e = (A * M) + a
d = (B * M) + b
n = int (((e * d) - 1) / M)


def Encrypt(message, e, n):
    ciphertext = (message * e) % n
    return ciphertext

def Decrypt(message, d, n):
    plaintext = (message * d) % n
    return plaintext

if (option == 'E'):
    print(Encrypt(message, e, n))
else:
    print(Decrypt(message, d, n))

