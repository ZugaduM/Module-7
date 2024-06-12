file_name = "text_file.txt"
with open(file_name, "r") as file: # оператор with практичнее для использования, так как автоматически закрывает файл после завершения обращения к нему
    print(file.read())
