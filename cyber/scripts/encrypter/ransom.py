
import os
import time
from cryptography.fernet  import Fernet


def encrypt_file(file_path, key):
    file_count = 0
    try:
        start = time.time()
        with open(file_path, "rb") as file:
            # Read the contents of the file
            file_data = file.read()
        # Encrypt the file data
        fernet = Fernet(key)
        encrypted_data = fernet.encrypt(file_data)
        # Write the encrypted data back to the file
        with open(file_path, "wb") as file:
            file.write(encrypted_data)
        file_count = file_count + 1 
        if os.name == 'posix':
            directory_separator = '/'
        else:
            directory_separator = '\\'
        new_path = os.rename(file_path, file_path + ".encrypted")
        end_time = time.time()
        print (("{} encrypted  Time taken {:>b.2F} ").format(file_path,end_time- start))
        return  file_count
    except PermissionError:
        print(f"Skipping file {file_path}: permission denied")
        pass
    except Exception as e:
        pass
     

def enc_traverse_directory(directory, key):
    file_count = 0
    # Traverse through directory and encrypt files
    start_time = time.time()
    for root, dirs, files in os.walk(directory):
        if files:
            for file in files:
                file_path = os.path.join(root, file)
                encrypt_file(file_path, key)
                file_count = file_count + 1
                if os.name == 'posix':
                    directory_separator = '/'
                else:
                    directory_separator = '\\'

                if os.path.exists(file_path):
                    os.rename(file_path, file_path + ".encrypted")

                print("File encrypted successfully:", file_path)
    print(f"The total number of files encrypted is {file_count}")
    end_time = time.time()
    elapsed = end_time - start_time
    print(('Total time taken  {:.2F} S').format(elapsed))


