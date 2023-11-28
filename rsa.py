#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 00:37:33 2021

@author: sg
"""

from math import gcd
import random
from random import randint
import sys
import time
start_time =time.time()

def encodeMessage(msg):
    encodedMsg = 0

    for char in msg:
        encodedMsg = encodedMsg << 8
        encodedMsg = encodedMsg ^ ord(char)
    return encodedMsg

def getRandomPrime(primeSize):
    x = randint(1 << (primeSize - 1), (1 << primeSize) - 1)
    while not (isPrime(x)):
        x = randint(1 << (primeSize - 1), (1 << primeSize) - 1) 
    return x
    
def isPrime(n):
    if n % 2 == 0:
        return False

    for i in range(1, 40):
        a = random.randint(1, n - 1)
        if isComposite(a, n):
            return False
    return True

def isComposite(a, n):
    
    t,d = decompose(n - 1)
    x = pow(a, d, n)
    
    if x == 1 or x == n - 1:
        return False

    for i in range(1, t):
        x0 = x;
        x = pow(x0, 2, n)
        if x == 1 and x0 != 1 and x0 != n - 1:
            return True
    if x != 1:
        return True
        
    return False

def decompose(n):
    i = 0
    while n & (1 << i) == 0:
        i += 1
    return i, n >> i

def getKeys(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    for i in range(2, phi):
        if gcd(phi,i) == 1:
            e = i
            break
         
    d = multiplicativeInverse(e, phi)
    
    return n, e, d

def multiplicativeInverse(e, phi):
    return extendedEuclid(e, phi)[1] % phi

def extendedEuclid(a, b):
    if b == 0:
        return a, 1, 0
    else: 
        d2, x2, y2 = extendedEuclid(b, a % b)
        d, x, y = d2, y2, x2 - (a // b) * y2
        return d, x, y



try:
    modulusSize = int(sys.argv[1])
        
except:
    modulusSize = 1024

msg = "Hello, World!"

primeSize = modulusSize // 2
p = getRandomPrime(primeSize)
q = getRandomPrime(primeSize)
while p == q:
    q = getRandomPrime(primeSize)

n, e, d = getKeys(p, q)
"""
encodedMsg = encodeMessage(msg)
encryptedMsg = pow(encodedMsg, e, n)
decryptedMsg = pow(encryptedMsg, d, n)
"""
#print("Public key (e, n):")
#print("\te = ", len((bin(e)[2:])))
#print("\tn = ", len((bin(n)[2:])))

pub_key = (bin(e)[2:]) + (bin(n)[2:])
#print("Pub_key:", pub_key)
#print("\nPrivate key (d, n):")
#print("\td = ", len((bin(d)[2:])))
priv_key = (bin(d)[2:]) + (bin(d)[2:])
#print("Priv_key:", priv_key)

print ("execution time in secs:-->", time.time() - start_time)

"""
def append_new_line(file_name, text_to_append):
    # Open the file in append & read mode ('a+')
    with open(file_name, "a+") as file_object:
        # Move read cursor to the start of file.
        file_object.seek(0)
        # If file is not empty then append '\n'
        data = file_object.read(100)
        if len(data) > 0:
            file_object.write("\n")
        # Append text at the end of file
        file_object.write(text_to_append)
append_new_line('RSA_public_key.txt',pub_key )

append_new_line('RSA_private_key.txt',priv_key )

"""

"""
print("\nOriginal message string:\n\t", msg)
print("\nInteger encoded message:\n\t", encodedMsg)
print("\nEncrypted message( C(M) = M^e % n ):\n\t", encryptedMsg)
print("\nDecrypted message( M(C) = C^d % n ):\n\t", decryptedMsg)
if encodedMsg == decryptedMsg:
    print("\nThe decrypted message and the original encoded message match.")
"""