# Imports
import os
import shutil

# Source directory of 'before' files
before_path = r'C:\Users\USER\OneDrive - vayyar.com\Desktop\before11' # Enter source 'before' path
before_dir_list = os.listdir(before_path)

# Source directory 'after' files
after_path = r'C:\Users\USER\OneDrive - vayyar.com\Desktop\after11' # Enter source 'after' path
after_dir_list = os.listdir(after_path)

# Destination directory of valid files
valid_before_path = r'C:\Users\USER\OneDrive - vayyar.com\Desktop\valid after check\before' # Enter dest 'before' path
valid_after_path = r'C:\Users\USER\OneDrive - vayyar.com\Desktop\valid after check\after' # Enter dest 'after' path


for beforeFile in before_dir_list:
    for afterFile in after_dir_list:
        if beforeFile.split('.')[0] in afterFile:
            # 'before' paths
            before_source_path = before_path + '\\' + beforeFile
            before_dest_path = valid_before_path + '\\' + beforeFile
            # 'after' paths
            after_source_path = after_path + '\\' + afterFile
            after_dest_path = valid_after_path + '\\' + afterFile

            print(beforeFile + ': is Valid')
            shutil.move(before_source_path, before_dest_path)
            shutil.move(after_source_path, after_dest_path)

            continue

        elif beforeFile.split('.')[0] not in afterFile:
            print('...')