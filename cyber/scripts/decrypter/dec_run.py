
from cyber.scripts.common_functions import key_save_load , os , get_root_dir , read_key
from cyber.scripts.commands import DecCommands


def code(directory , key_path = None):

    
    path = directory
    c = DecCommands()
    if key_path!= None and os.path.exists(key_path):
        key = read_key(key_path)
    else:
        key = key_save_load(directory)
        
    while True:
        
        if os.path.exists(path):
            c.display_folder(path)
        choice = input(": ")
        """"
        provide the path key and starting folder
        """
        try:
            if choice != '':
                choice = int(choice)
            help_list = ['-h', '--h', '--help', '-H', 'h']
            choice = int(choice)
            if choice == 0:
                path = c.navigate_back(path)
            elif choice == -5:
                c.clear_console()
            elif choice == -2 or choice == -1:
                if key == None:
                    try:
                        print ("key needed " , key)
                        will = input ("Do you wish to load the key: (y,n)").lower()
                        if will == 'n':
                            pass
                        else:
                            key = key_save_load(path=path)
                    except Exception as e:
                        pass


                if key != None:
                    if choice == -2:
                        c.file_decryption(path, key)
                    elif choice == -1:
                        c.folder_decryption(path, key)
                else:
                    print ("Unset key")
            elif int(choice) > 0:
                path = c.go_foward(choice, path, key , "decrypt")

        except ValueError:
            help_list = ['-h', '--h', '--help', '-H', 'h']
            if choice == '-h' or choice in help_list:
                c.ask_help()
            elif choice ==  'b':
                print ("switching from decryption")

                break
            else:
                print('*', path)
                if os.path.isfile(path):
                    path = os.path.dirname(path)
                    
            

        except NotADirectoryError:
            pass

        except FileNotFoundError:
            pass

        except IndexError:
            print("index error ")

        except PermissionError:
            print(f"Permission denied for file {path}")
            continue
        except KeyboardInterrupt:
            print("Good bye")
            break
    directory  = path
    return directory

#root_dir = os.getcwd()


def dec_main(root_dir ,key_path):

    return code(root_dir , key_path=key_path)

if __name__ == "__main__":

    root_dir = get_root_dir()
    code(root_dir )
