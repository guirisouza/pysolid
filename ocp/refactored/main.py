from file_reader import FileReader

file_reader = FileReader()
file_reader.set_file_path('dados.csv')
print(file_reader.read_file())

