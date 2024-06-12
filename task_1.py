from pprint import pprint

file_name = "text_file.txt"
my_file = open(file_name, "r")
pprint(my_file.read())
my_file.close()
