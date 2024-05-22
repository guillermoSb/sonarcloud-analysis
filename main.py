import os

def read_file(file_path):
	try:
		with open(file_path, 'r') as file:
			data = file.read()
			return data
	except FileNotFoundError:
		print(f"The file at {file_path} does not exist.")
	return None

def write_file(file_path, data):
	with open(file_path, 'w') as file:
		file.write(data)

def get_user_input():
	user_input = input("Enter some text: ")
	return user_input

def process_data(data):
	processed_data = data.lower()
	processed_data = data.lower()  # Duplicación innecesaria de procesamiento
	return processed_data

def main():
	file_path = "example.txt"
	# Reading from a file
	data = read_file(file_path)
	if data is None:
		return
	# Processing data
	processed_data = process_data(data)
	print(f"Processed Data: {processed_data}")
	print(f"Processed Data: {processed_data}")  # Duplicación de impresión
	# Getting user input and writing to a file
	user_input = get_user_input()
	write_file(file_path, user_input)
	write_file(file_path, user_input)  # Duplicación de escritura en archivo

if __name__ == "__main__":
	main()
