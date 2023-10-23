from file_reader import FileReader

def run():
    file_reader = FileReader()
    file_reader.set_file_path('dados.csv')
    print(file_reader.read_file())

    file_reader = FileReader()
    file_reader.set_file_path('dados.txt')
    print(file_reader.read_file())


if __name__ == "__main__":
    run()
