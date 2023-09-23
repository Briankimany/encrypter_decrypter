
from cyber.scripts.common_functions import key_save_load, get_root_dir , read_key

from cyber.scripts.commands import EnCommands


paths_list =[]
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
def code(directory , *args):

    c = EnCommands()
    key = key_save_load(directory)
    path = directory

    help_list = ['-h' , '--h' , '--help' , '-H' , 'h' , 'H']
    while True:
        choice = input(": ")
        """"
        provide the path key and a starting folder
        """
        try:

            choice = int(choice)
            if choice == 0:
                path = c.navigate_back(path)
                c.display_folder(path)
            elif choice == -5:
                c.clear_console()
            elif choice == -2 or choice == -1:
                if key == None:
                    try:
                        print ("key needed ")
                        will = input ("Do you wish to load the key: (y,n)").lower()
                        if will.strip() == 'b':
                            break
                        else:
                            key = key_save_load(path)
                    except Exception as e:
                        pass
                if key != None:
                    if choice == -2:
                        c.file_encryption(path, key)
                    elif choice == -1:
                        c.folder_encryption(path, key)
                else:
                    print("Unset key")

            elif int(choice) > 0:
                path = c.go_foward(choice, path, key , "encrypt")
                c.display_folder(path)
        except ValueError:
            if choice == '-h' or choice in help_list:
                c.ask_help()
            elif choice ==  'b':
                print ("switching from encryption")
                break
            else:
                print("Listing ")
                path = c.display_folder(path)
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


def enc_main(root_dir ,*args):
    code(root_dir)


if __name__ == "__main__":

    root_dir = get_root_dir()
    code(root_dir)