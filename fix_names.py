import os

# Directory source path
path = r'C:\wand_backup\NewValidator_Desktop\DONE' # Enter dir path
dir_list = os.listdir(path)

for file in dir_list:
    if '_Valid_Valid' in file:
        old_name = path + '\\' + file
        new_name = old_name.replace('_Valid_Valid', '_Valid')

        print('Valid:\n' + old_name + '\n' + new_name + '\n\n')
        os.rename(old_name, new_name)

    elif('_Valid_Invalid'):
        old_name = path + '\\' + file
        new_name = old_name.replace('_Valid_Invalid', '_Invalid')

        print('Invalid:\n' + old_name + '\n' + new_name + '\n\n')
        os.rename(old_name, new_name)




