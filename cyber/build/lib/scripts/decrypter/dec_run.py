
from ajay.cyber.scripts.common_functions import key_save_load , os , root , read_key
from ajay.cyber.scripts.commands import DecCommands
def code(directory , *args):
    if len(args) > 0:
        key = args[0]
    else:
        key = key_save_load()
    path = directory

    c = DecCommands()
    while True:
        c.display_folder(path)
        choice = input(": ")
        """"
        provide the path key and starting folder
        """
        try:
            choice = int(choice)
            help_list = ['-h', '--h', '--help', '-H', 'h']
            choice = int(choice)
            if choice == 0:
                path = c.navigate_back(path)
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
                        c.file_decryption(path, key)
                    elif choice == -1:
                        c.folder_decryption(path, key)
            elif int(choice) > 0:
                path = c.go_foward(choice, path, key , "decrypt")
                #c.display_folder(path)
        except ValueError:
            help_list = ['-h', '--h', '--help', '-H', 'h']
            if choice == '-h' or choice in help_list:
                c.ask_help()
            elif choice ==  'b':
                print ("switching from encryption")
                break
            else:
                print("Listng ", path)
                if os.path.isfile(path):
                    path = os.path.dirname(path)
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


#root_dir = os.getcwd()


def dec_main(root_dir , *args):

    code(root_dir)

if __name__ == "__main__":
    defualt_key = read_key("/home/brian/damaged'/Screenshot from 2023-07-25 04-29-07.txt")
    root_dir = root()
    code(root_dir , defualt_key)
