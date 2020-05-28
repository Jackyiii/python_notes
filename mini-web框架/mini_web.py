import time

def login():
	return "login %s"%time.ctime()

def resgiter():
	return "welcome to our site: %s"%time.ctime()

def profil():
	return "welcome to our site: %s"%time.ctime()

def application(file_name):
	if file_name=="/login.py":
		return login()
	elif file_name=="/resgiter":
		return resgiter()
	elif file_name=="/profil":
		return profil()
	else:
		return "not found"