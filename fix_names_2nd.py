import os

# Directory source path
path = r'C:\Users\zuradmin\Desktop\Adir\test' # Enter directory path
dir_list = os.listdir(path)

for file in dir_list:
    parent_dir_name = 'False Positive' # Write parent directory name
    gender = 'Male' # Write gender

    old_name = path + '\\' + file

    new_name = path + '\\' + parent_dir_name + '_' + gender + '_' + file

    print('Valid:\n' + old_name + '\n' + new_name + '\n\n')
    os.rename(old_name, new_name)