from file_reader import FileReader

file_reader = FileReader()
file_reader.set_file_path('dados.txt')
print(file_reader.get_file())

file_reader2 = FileReader()
file_reader2.set_file_path('dados.csv')
print(file_reader2.get_file())
