
from ajay.cyber.scripts.common_functions import key_save_load , root , read_key

from ajay.cyber.scripts.commands import EnCommands


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
    if len(args) > 0:
        key = args[0]
    else:
        key = key_save_load()

    c = EnCommands()
    path = directory

    help_list = ['-h' , '--h' , '--help' , '-H' , 'h' , 'H']
    while True:
        choice = input(": ")
        """"
        provide the path key and starting folder
        """
        try:

            choice = int(choice)
            if choice == 0:
                path = c.navigate_back(path)
                c.display_folder(path)
            elif choice == -5:
                c.clear_console()
            elif choice == -2 or choice == -1:
                while key == None:
                    print ("key needed ")
                    will = input ("DO you wish to load the key: (y,n)").lower()
                    if will:
                        key = key_save_load()
                    elif will == 'b':
                        break
                if key != None:
                    if choice == -2:
                        c.file_encryption(path, key)
                    elif choice == -1:
                        c.folder_encryption(path, key)

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


def n():
    print ("KIM")
if __name__ == "__main__":
    defualt_key = read_key("/home/brian/damaged'/Screenshot from 2023-07-25 04-29-07.txt")
    root_dir = root()
    code(root_dir , defualt_key)