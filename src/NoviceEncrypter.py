from os import path

def Encrypt(filename, key):
	file = open(filename, "r").read().splitlines()
	
	newline = ""
	newfile = str(key)
	
	for line in file:
		for i in range(0, len(line)):
			char = line[i:i+1]
			num = ord(char) + key
			char = chr(num)
			newline += char
		newfile += newline + "\n"
		newline = "" # clear cached data

	return newfile

def Decrypt(filename):
	file = open(filename, "r").read()
	try:
		key = int(file[0])
	except ValueError:
		raise Exception("Cannot decrypt this file! Encryption key not found")
	
	file = file[1:]
	file = file.splitlines()
	
	newline = ""
	newfile = ""
	
	for line in file:
		for i in range(0, len(line)):
			char = line[i:i+1]
			num = ord(char) - key
			char = chr(num)
			newline += char
		newfile += newline + "\n"
		newline = "" # clear cached data

	return newfile

# // MAIN \\ #

if __name__ == "__main__":
	print("Novice Encrypter V1.0.0 (Zohaib Jafar)\n\n")
	choice = 0

	while choice !=1 and choice !=2:
		try:
			print("1. Encrypt a file\n2. Decrypt a file\n")
			choice = int(input("_$ "))
		except ValueError:
			print("Enter a valid number.")

	if choice == 1:
		key = 2 # 2 always works (until it doesn't). You can use random.randint to produce random keys but they're kinda faulty

		filename = input("Enter filename to read: ")

		while not path.exists(filename): # input validation
			print("Filename does not exsist")
			filename = input("Enter filename to read: ")

		encrypted = Encrypt(filename, key)
		encrypted_file = open("encrypted_"+filename, "w")
		encrypted_file.write(encrypted)
		encrypted_file.close()
		exit()
	if choice == 2:
		filename = input("Enter filename to read: ")

		while not path.exists(filename):
			print("Filename does not exist")
			filename = input("Enter filename to read: ")

		decrypted = Decrypt(filename)
		decrypted_file = open("decrypted_"+filename, "w")
		decrypted_file.write(decrypted)
		decrypted_file.close()
		exit()
else:
	pass
