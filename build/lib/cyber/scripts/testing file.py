# import os
# import sys
# from scripts.commands import DecCommands , EnCommands  # Replace 'your_module' with your actual module name
# from scripts.common_functions import  read_key
#
# def t_commands():
#     key_path = "/home/brian/damaged'/Screenshot from 2023-07-25 04-29-07.txt"
#     key = read_key(key_path)
#     path = "/home/brian/damaged'"
#
#     print('starting path ', path)
#     c = DecCommands()
#
#     while True:
#         if "pytest" in sys.modules:
#             # Running under pytest, skip input prompt
#             # or provide some default input for testing
#             choice = "default_choice"
#         else:
#             c.display_folder(path)
#
#             choice = input(": ")
#
#         try:
#             help_list = ['-h', '--h', '--help', '-H', 'h']
#
#             choice = int(choice)
#             if choice == 0:
#                 path = c.navigate_back(path)
#                 c.display_folder(path)
#             elif choice == -5:
#                 c.clear_console()
#             elif choice == -2:
#                  c.file_decryption(path, key)
#             elif choice == -1:
#                  c.folder_decryption(path, key)
#             elif int(choice) > 0:
#                 path = c.go_foward(choice , path , key , 'decrypt')
#                # c.display_folder(path)
#         except ValueError:
#             help_list = ['-h', '--h', '--help', '-H', 'h']
#             if choice == '-h' or choice in help_list:
#                 c.ask_help()
#             else:
#                 print("Listing ", path)
#                 if os.path.isfile(path):
#                     path = os.path.dirname(path)
#                 path = c.display_folder(path)
#         except NotADirectoryError:
#             pass
#         except FileNotFoundError:
#             pass
#         except IndexError:
#             print("Index error")
#         except PermissionError:
#             print(f"Permission denied for file {path}")
#             continue
#         except KeyboardInterrupt:
#             print("Goodbye")
#             break
#
# # Uncomment the line below if you want to run the function when this script is executed.
# t_commands()

# didc = {1:"DeCommands" ,
#         2: "EncCommands"}
# def process():
#     v = int(input("HH : "))
#     df = ('c' + '.' + didc[v])
#     print (df)
#
# while True:
#     process()


# import tkinter as tk
# from tkinter import filedialog
# from scripts.common_functions import key_save_load, directory_separator
# from scripts.encrypter.enc_run import enc_main
# from scripts.decrypter.dec_run import dec_main
#
#
# class EncryptionDecryptionApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Encryption and Decryption App")
#
#         self.directory_separator = directory_separator()
#
#         self.label = tk.Label(root, text="Choose an operation:")
#         self.label.pack()
#
#         self.encryption_button = tk.Button(root, text="Encryption", command=self.encryption)
#         self.encryption_button.pack()
#
#         self.decryption_button = tk.Button(root, text="Decryption", command=self.decryption)
#         self.decryption_button.pack()
#
#     def encryption(self):
#         self.root.withdraw()  # Hide the main window
#         starting_directory = self.get_directory()
#         key = self.get_key()
#         enc_main(starting_directory, key)
#
#     def decryption(self):
#         self.root.withdraw()  # Hide the main window
#         starting_directory = self.get_directory()
#         key = self.get_key()
#         dec_main(starting_directory, key)
#
#     def get_directory(self):
#         directory = filedialog.askdirectory(title="Select a directory")
#         return directory
#
#     def get_key(self):
#         key = key_save_load()
#         return key
#
#
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = EncryptionDecryptionApp(root)
#     root.mainloop()


# import tkinter as tk
# from tkinter import filedialog
# from scripts.common_functions import key_save_load, directory_separator
# from scripts.encrypter.enc_run import enc_main
# from scripts.decrypter.dec_run import dec_main
#
# class EncryptionDecryptionApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Encryption and Decryption App")
#         self.directory_separator = directory_separator()
#
#         # Create GUI components here
#         self.operation_label = tk.Label(root, text="Select an operation:")
#         self.operation_label.grid(row=0, column=0, columnspan=2)
#
#         self.operation_var = tk.StringVar(value="Encryption")
#         self.encryption_radio = tk.Radiobutton(root, text="Encryption", variable=self.operation_var, value="Encryption")
#         self.encryption_radio.grid(row=1, column=0, padx=10, pady=5)
#         self.decryption_radio = tk.Radiobutton(root, text="Decryption", variable=self.operation_var, value="Decryption")
#         self.decryption_radio.grid(row=1, column=1, padx=10, pady=5)
#
#         self.directory_label = tk.Label(root, text="Select a directory:")
#         self.directory_label.grid(row=2, column=0, columnspan=2)
#         self.directory_button = tk.Button(root, text="Browse", command=self.get_directory)
#         self.directory_button.grid(row=3, column=0, columnspan=2, padx=10, pady=5)
#
#         self.key_label = tk.Label(root, text="Load encryption/decryption key:")
#         self.key_label.grid(row=4, column=0, columnspan=2)
#         self.key_button = tk.Button(root, text="Load Key", command=self.get_key)
#         self.key_button.grid(row=5, column=0, columnspan=2, padx=10, pady=5)
#
#         self.run_button = tk.Button(root, text="Run", command=self.run_operation)
#         self.run_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)
#
#     def get_directory(self):
#         directory = filedialog.askdirectory(title="Select a directory")
#         # Store the selected directory path
#         self.selected_directory = directory
#
#     def get_key(self):
#         key = key_save_load()
#         # Store the loaded key
#         self.loaded_key = key
#
#     def run_operation(self):
#         selected_operation = self.operation_var.get()
#         if selected_operation == "Encryption":
#             enc_main(self.selected_directory, self.loaded_key)
#         elif selected_operation == "Decryption":
#             dec_main(self.selected_directory, self.loaded_key)
#
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = EncryptionDecryptionApp(root)
#     root.mainloop()
#
#
#
#



'''
 def ed():
    # import tkinter as tk
    # from tkinter import messagebox
    # from tkinter import filedialog
    # from scripts.decrypter.dec_run import dec_main
    # from scripts.encrypter.enc_run import enc_main
    # from scripts.common_functions import root, enc_help, clear_console
    #
    # HELP_OPTIONS = ['-h', '--h', '--help', '-H', 'h', 'H']
    #
    # def main():
    #     def on_decrypt():
    #         starting_directory = root()
    #         result = dec_main(starting_directory)
    #         output_text.insert(tk.END, result + '\n')  # Display the result in the output area
    #
    #     def on_encrypt():
    #         starting_directory = root()
    #         result = enc_main(starting_directory)
    #         output_text.insert(tk.END, result + '\n')  # Display the result in the output area
    #
    #     def on_clear_console():
    #         output_text.delete(1.0, tk.END)  # Clear the output area
    #
    #     def on_help():
    #         help_message = enc_help()
    #         messagebox.showinfo("Help", help_message)
    #
    #     tk_root = tk.Tk()
    #     tk_root.title("Encryption and Decryption Tool")
    #
    #     decrypt_button = tk.Button(tk_root, text="Decrypt", command=on_decrypt)
    #     decrypt_button.pack()
    #
    #     encrypt_button = tk.Button(tk_root, text="Encrypt", command=on_encrypt)
    #     encrypt_button.pack()
    #
    #     clear_console_button = tk.Button(tk_root, text="Clear Console", command=on_clear_console)
    #     clear_console_button.pack()
    #
    #     help_button = tk.Button(tk_root, text="Help", command=on_help)
    #     help_button.pack()
    #
    #     output_text = tk.Text(tk_root, wrap=tk.WORD, width=50, height=10)
    #     output_text.pack()
    #
    #     tk_root.mainloop()
    #
    #
    # def g (*args , j=None):
    #     if j!= None  or len (args):
    #         print (j , args)
    #     elif len (args) > 0 and j!=None:
    #         print (args , j)
    #     else:
    #         print ("NOne")
    #

from scripts.GUI.learning_gui import one_crete_image

import tkinter as tk

root = tk.Tk()

root1 = one_crete_image('/home/brian/Pictures/Untitled Folder/kimani is a guy who love macine leanrning and likes to east food 5_0_9339.jpeg' , root )
root1.mainloop()

'''


import os
import tkinter as tk
from PIL import Image, ImageTk

size = (150, 150)

def create_image(images, index, root):
    global size
    try:
        if 0 <= index < len(images):
            image_path = images[index]
            root.title(image_path)
            print('Path passed:', image_path)
            image = ImageTk.PhotoImage(Image.open(image_path).resize(size=size))
            my_image = tk.Label(root, image=image)
            my_image.grid(row=1, column=1)
            return my_image, image
    except Exception as e:
        print(str(e))
        pass

def image_paths(directory):
    if os.path.isdir(directory):
        try:
            images = [os.path.join(directory, image) for image in os.listdir(directory)]
            return images
        except IsADirectoryError:
            pass
    else:
        return directory

def next_image():
    global images
    global index
    if index < len(images) - 1:
        index += 1
        my_image, image = create_image(images, index, root)
        my_image.configure(image=image)
        my_image.image = image

def previous_image():
    global index
    global images
    if index > 0:
        index -= 1
        my_image, image = create_image(images, index, root)
        my_image.configure(image=image)
        my_image.image = image

def main():
    directory = '/home/brian/Pictures'
    global images
    images = image_paths(directory)
    global index
    index = 0
    global root
    root = tk.Tk()

    next_button = tk.Button(root, text=">> Next", command=next_image)
    next_button.grid(row=0, column=0)

    previous_button = tk.Button(root, text="<< Previous", command=previous_image)
    previous_button.grid(row=0, column=1)

    exit_button = tk.Button(root, text="Kill", command=root.quit, fg='red', bg='blue')
    exit_button.grid(row=9, column=0)

    if images:
        my_image, image = create_image(images, index, root)
        my_image.configure(image=image)
        my_image.image = image

    root.mainloop()

if __name__ == '__main__':
    main()












