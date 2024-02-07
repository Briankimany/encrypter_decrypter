import os
import time
from cryptography.fernet import InvalidToken , Fernet
from cyber.scripts.common_functions import directory_separator
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
   
    data =key , un_done , failed_file_count
    def work(path , data = data):
        key , un_done , failed_file_count = data
        decrypt_file(path , key , un_done , failed_file_count)
    
    results_ = list(map(work , path_list))

    end_time = time.time()
    correct_file_count = file_count - failed_file_count
    print (("Time taken {:.2F}").format (end_time - start_time))
    if correct_file_count != file_count:
        print(f"The original number of files was {file_count}")
        print(f"The total number of files decrypted is {correct_file_count}")
    return un_done


def rename_file(full_path):
    try:
        ext = '.encrypted'
        if os.name == 'posix':
            directory_separator = '/'
        else:
            directory_separator = '\\'
        if os.path.isfile(full_path):
            # Split the file name by '.'
            
            path_list = [os.path.dirname(full_path)] + list( os.path.splitext(os.path.basename(full_path)))

            source_dir  =  os.path.dirname(full_path)
            base_name  = os.path.basename(full_path)
            file_name ,file_extension  = os.path.splitext(base_name)
            # Check if 'ext' is in the path_list and remove it
            path = os.path.dirname(full_path)
            if file_extension == ext:
               
               new_name = file_name
                
            else:
                new_name = base_name
            new_file_name =  os.path.join(path, new_name)
            # Rename the file
            os.rename(full_path,new_file_name)
            
            return new_file_name
        else:
            pass

    except Exception as e:
        print(f"Error renaming {full_path}: {e}")
        return None


def decrypt_file(file_path, key , *args):
    global  directory_separator
    if len(args) > 0:
        un_done = args[0]
        failed_file_count = args[1]
   
        failed_file_count += 1
       # print(un_done , failed_file_count)
    try:
        start_time = time.time()
        with open(file_path, "rb") as file:
            encrypted_data = file.read()
        key = Fernet(key)
        decrypted_data = key.decrypt(encrypted_data)
        print(file_path)
        with open (file_path, 'wb') as file:
            file.write(decrypted_data)
    
        end_time = time.time()
        elapsed_time = end_time - start_time
        # print(("File decrypted:Time taken : {:>.2F} S").format(elapsed_time))
        res = rename_file(file_path)
     

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
        print(f"Permssion denied for {file_path}")
        pass
    except  Exception as e:
        pass











    
 


 



          
        
      
        
      

    
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      