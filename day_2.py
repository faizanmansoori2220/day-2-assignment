# -*- coding: utf-8 -*-
"""day 2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18-WQLyjY87HPMq_3UaufE3kSCsFA6deD
"""

#Delete all occurrences of an element in a list

l= [int(x) for x in input("enter elements: ").split()]
element = 1
for i in l:
	if(i == element):
		l.remove(i)
print(l)

#Check whether a string is a pangram.

import string

def ispangram(sentence, alphabet=string.ascii_lowercase): 
    return set(alphabet) <= set(sentence.lower()) 

print(ispangram(input('Sentence: ')))

#otp project

import math, random
def generateOTP() :
	digits = "0123456789"
	OTP = ""
	for i in range(4) :
		OTP += digits[math.floor(random.random() * 10)]
	return OTP

print("OTP of 4 digits:", generateOTP())

