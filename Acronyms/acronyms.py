import os
import os.path 

def find_in_file(file_path, acronym):
    result = ''
    if os.path.exists(file_path):
        with open(file_path) as file:
            for line in file:
                if acronym in line:
                   result = line
                   break    
    else:
        print("Source file doesn't exists")
        exit()

    return result

def insert_new_acronym(file_path, acronym):
    description = input("What's stands for? ")
    with open(file_path, 'a') as file:
        file.write('\n'+ acronym.upper() + ' ' + description)

    print('Acronym Added -->', acronym.upper() + ' ' + description)

def get_file_name():
    filename = input('Type source file name (Enter for default index.txt)? ') 
    if len(filename) == 0:
        filename = 'input'

    filename =  '\\' + filename + '.txt'
    return filename

def get_acronym_to_lookup():
    acronym = input('Type a acronym to lookup? ')
    return acronym

def main():
    repeat_process = 'y'

    while repeat_process == 'y':
        os.system('cls')
        file_full_path = os.path.dirname(__file__) + get_file_name()
        acronym_to_lookup = get_acronym_to_lookup()

        result = find_in_file(file_full_path, acronym_to_lookup)

        if len(result) == 0:
           response = input('\33[31m' + "The acronym wasn't included in the file\n"  + '\33[0m' + "Do you want to add it to the file (Y/N)? ")
           if response.upper() == 'Y':
              insert_new_acronym(file_full_path, acronym_to_lookup)
        else:
            print(acronym_to_lookup, "-->", result)
        
        repeat_process = input('Want to check another acronym (y/n) ? ')
        repeat_process = repeat_process.lower()

    os.system('cls')

# Main program
main()