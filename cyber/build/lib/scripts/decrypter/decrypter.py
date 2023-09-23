import os
import time
from cryptography.fernet import InvalidToken , Fernet
from ajay.cyber.scripts.common_functions import directory_separator
restricted_directories = [
    "/etc",
    "/bin",
    "/sbin",
    "/usr",
    "/var",
    "C:\\Windows",
    "C:\\Program Files",
    "C:\\Program Files (x86)",
    "C:\\System Volume Information"
]




directory_separator = directory_separator()
def decrypt_multiple_files(key , path_list):
    un_done = []
    file_count = len(path_list)
    failed_file_count = 0
    start_time = time.time()
    for path in path_list:
        decrypt_file(path , key , un_done , failed_file_count)
    end_time = time.time()
    correct_file_count = file_count - failed_file_count
    print (("Time taken {}").format (end_time - start_time))
    print(f"The original number of files was {file_count}")
    print(f"The total number of files decrypted is {correct_file_count}")
    return un_done


def rename_file(full_path):
    try:
        ext = 'encrypted'
        if os.name == 'posix':
            directory_separator = '/'
        else:
            directory_separator = '\\'
        if os.path.isfile(full_path):
            # Split the file name by '.'
            path_list = full_path.split('.')
            # Check if 'ext' is in the path_list and remove it
            path = os.path.dirname(full_path)
            if ext in path_list:
                path_list.remove(ext)
            # Construct the new file name
            if len(path_list[-1].split(directory_separator)) > 1:
                extension = ''
            else:
                extension = path_list[-1]
            new_name = path_list[0] + '.' + extension
            # Rename the file
            os.rename(full_path, os.path.join(path, new_name))
            # print(f"Renamed: {full_path} to {new_name}")
        else:
            pass

    except Exception as e:
        print(f"Error renaming {full_path}: {e}")


def decrypt_file(file_path, key , *args):
    global  directory_separator
    if len(args) > 0:
        un_done = args[0]
        failed_file_count = args[1]
        un_done.append(file_path)
        failed_file_count += 1
       # print(un_done , failed_file_count)
    try:
        start_time = time.time()
        with open(file_path, "rb") as file:
            encrypted_data = file.read()
        key = Fernet(key)
        decrypted_data = key.decrypt(encrypted_data)
        with open (file_path, 'wb') as file:
            file.write(decrypted_data)
        print ("File decrypted")
        end_time = time.time()
        elapsed_time = end_time - start_time
        print("Time taken for decryption:", elapsed_time, "seconds")
        rename_file(file_path)

    except InvalidToken:
        half_file_path = (file_path.split(directory_separator)[-1])
        if len(args)> 0:
            un_done = args[0]
            failed_file_count = args[1]
            un_done.append(file_path)
            failed_file_count+=1

        print (f"Invaid key  for file {half_file_path}")
        pass
    except PermissionError:
        pass










    
 


 



          
        
      
        
      

    
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      