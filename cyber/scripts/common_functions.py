from cryptography.fernet import Fernet
import os
import tkinter as tk
from tkinter import filedialog
def directory_separator():
    if os.name == 'posix':
        directory_separator = '/'
    else:
        directory_separator = '\\'

    return directory_separator



def get_root_dir():
    directory_sep = directory_separator()
    root_dir_choice = input(
        f"Enter (r) to start from root directory\nPress enter start from ({os.getcwd()})")
    if root_dir_choice.lower() == "r":
        if os.name == 'posix':
            directory = '/'
        else:
            directory = 'C:\\'

    else:
        directory = os.getcwd()

    return  directory
def enc_help():

    help_messsage = """
    📜 File Encryption Utility Help 📜

    Encrypt/Decrypt your files and folders with ease! Use this script to secure your data.
    See below for usage instructions and examples.

    Usage:
    - `python encryption_script.py [root_directory]`

    Options:
    
    - `-b, --break`                    to swich role
    - `-h, --help`                     Show this help message and exit
    - `-1, --encrypt/decrypt-folder`   current folder
    - `-2, --encrypt/decrypt-file`     a file
    - `-5,  clear console`             clear console

    Examples:
    - `python encryption_script.py /home/user/Documents`
    - `python encryption_script.py /home/user/Documents -1`
    - `python encryption_script.py /home/user/Documents -2 file.txt`
    """

    return help_messsage



def check_content(path):
    """"
    Returns true if folder has both files and folders
    """
    mixed_content = False

    with os.scandir(path) as entries:
        for entry in entries:
            if entry.is_file():
                # print (f"{entry} is file")
                mixed_content = True
            elif entry.is_dir():

                mixed_content = False

    if mixed_content:

        return True
    else:

        return False

def clear_console():
    # Clear console output based on operating system
    os.system('cls' if os.name == 'nt' else 'clear')


paths_list = []
un_done = []

def process_directory(path):
    global paths_list
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isfile(item_path):
            paths_list.append(item_path)
            # print(f"Found file: {item_path}")
            # Do something with the file...
        elif os.path.isdir(item_path):
            # print(f"Found directory: {item_path}")
            process_directory(item_path)  # Recursively process subdirectories
        else:
            print(f"Found unknown item: {item_path}")
    return (paths_list)




def read_path(directory):
    try:
        root = tk.Tk()
        root.withdraw()
        
        root.configure(bg='purple')
        root.geometry('800x600')

        file_path = filedialog.askopenfilename(filetypes=[("All Files", "*.*")], initialdir=directory, title=directory)

        root.destroy()
        return file_path

    except KeyboardInterrupt:
        print("good bye")




def read_key(*args):
        print (len(args))
        if len(args) == 1:
            
            key_path = args[0]
              
        elif len (args) == 0:
            key_path = read_path(os.getcwd())


        print("Reading key from >>", key_path)

        with open(key_path, 'rb') as file:
            contents = file.read()

        return  contents


def read_single_file(*args):
    try:
        global root_dir
        root = tk.Tk()

        if args:
            root_dir = args[0]

        root.title("Reading single file")
        root.withdraw()
        root.configure(bg='purple')
        root.geometry('800x600')

        file_path = filedialog.askopenfilename(
            filetypes=[("All Files", "*.*")],
            initialdir=root_dir,
            title="Select file"
        )

        root.destroy()  # Close the Tkinter window and exit the program
        return file_path
    except KeyboardInterrupt:
        print("good bye")


def write_key_to_file(key , *args):
    try:
        root = tk.Tk()
       
        root.withdraw()
        root.configure(bg='purple')
        root.geometry('800x600')

        # Adjust initialdir based on the operating system
        if len(args)> 0:
            initialdir = args[0]
        else:
            if os.name == 'posix':
                initialdir = '/'
            elif os.name == 'nt':
                initialdir = 'C:\\'

        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("All Files", "*.*")],
                                                 initialdir=initialdir, title="Select file to save to")
        if file_path:
            print("Selected file:", file_path)
            with open(file_path, 'wb') as file:
                file.write(key)
                print("""
                      +------------------+
                      |  Key written     |
                      |  successfully!   |
                      +------------------+
                """)
       

        root.destroy()  # Close the Tkinter window and exit the program

    except KeyboardInterrupt:
        print("key not saved")


def key_save_load(path):
    save_key = (input("Generate new key (y)\nLoad key now (r)\nPress enter to skip\nchoice?/>>")).lower()
    if save_key == 'y':
        key = Fernet.generate_key()
        if os.path.exists(path):
            write_key_to_file(key , path)

        else:
            key = None

    elif save_key == 'r':
        key_path = read_single_file(path)
        key = read_key(key_path)
    else :
        key = None
    return key


if __name__ == "__main__":
    start = get_root_dir()
    print (f"This is the starting\n{start}")

    key = key_save_load(start)
    print(key)