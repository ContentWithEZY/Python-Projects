## // password_gen.py \\ ##

import random
import time 

def write_to_file(password, pass_for):
	file = open("passwords.txt", "a")
	file.write(pass_for + " : " + password + "\n")
	file.close()

def password_gen(abc, need_special, lenght, pass_for):
	global password
	numbers = "1234567890"
	abc_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	abc_lower = "abcdefghijklmnopqrstuvwyz"
	special = "!@#$%^&*()_+-="

	if need_special == "y":

		if abc == "1":
			password = ''.join((random.choice(abc_upper + special + numbers) for i in range(int(lenght))))
			write_to_file(password, pass_for)
		if abc == "2":
			password = ''.join((random.choice(abc_lower + special + numbers) for i in range(int(lenght))))
			write_to_file(password, pass_for)
		if abc == "3":
			password = ''.join((random.choice(abc_upper + abc_lower + special + numbers) for i in range(int(lenght))))
			write_to_file(password, pass_for)
	else:

		if abc == "1":
			password = ''.join((random.choice(abc_upper + numbers) for i in range(int(lenght))))
			write_to_file(password, pass_for)
		if abc == "2":
			password = ''.join((random.choice(abc_lower + numbers) for i in range(int(lenght))))
			write_to_file(password, pass_for)
		if abc == "3":
			password = ''.join((random.choice(abc_upper + abc_lower + numbers) for i in range(int(lenght))))
			write_to_file(password, pass_for)

pass_contain_special = input("Does the password need special characters? <y/n> : ")
pass_abc = input("Does the password need <1>UPPERCASE, <2>LOWERCASE or <3>BOTH ? : ")
pass_len = input("Password Lenght : ")
pass_for = input("For what are you using this password ? : ")
password_gen(pass_abc, pass_contain_special, pass_len, pass_for)

