def save_to_file(content, filename): 
    with open(filename, 'w') as file: 
        file.write(content)


def read_file(filename): 
    with open(filename, 'r') as file: 
        return file.read()

from file_operations import save_to_file

save_to_file('Rolf', 'data.txt')
print(read_file('data.txt'))