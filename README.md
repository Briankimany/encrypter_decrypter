# SecureFile - Encrypt and Decrypt Your Files and Folders

## Introduction

SecureFile is a Python script that provides a straightforward way to encrypt and decrypt your files and folders, ensuring the security of your data. 
It offers a command-line interface (CLI) for navigating directories, selecting items for encryption/decryption, and performing the respective operations. 
SecureFile is compatible with Unix-like systems (Linux, macOS) and Windows platforms.

## Common Features

- **Cross-Platform Compatibility:** SecureFile works seamlessly on Unix-like systems (Linux, macOS) and Windows.
- **Directory Traversal:** The script can traverse directories and subdirectories to locate files for encryption or decryption.
- **Interactive CLI:** SecureFile offers an interactive CLI for navigating directories and making choices.
- **Mixed Content Handling:** It handles directories with mixed content, including encrypted and unencrypted files.
- **Error Handling:** SecureFile includes error handling for various scenarios, such as invalid input and file permissions.
- **Time Tracking:** The script measures and displays the time taken for encryption or decryption operations.



Installation and Environment Setup
Option 1: Using a Virtual Environment (Recommended)

    Create a Virtual Environment
    We strongly recommend creating a virtual environment to isolate your project's dependencies.
    This helps prevent conflicts with system-wide packages:
        


   1: # Create a virtual environment
        python -m venv venv

        # Activate the virtual environment
        source venv/bin/activate  # On Linux/macOS
        # or
        venv\Scripts\activate  # On Windows


        
        #Installing the requirements 
        pip install -r requirements.txt
    
   2: Installing Dependencies in the Base Environment

        Warning: Installing dependencies in the base Python environment is not advisable as it may conflict with system-wide packages and cause issues with other projects.

        Install Dependencies in the Base Environment:

        If you choose to install dependencies in the base environment, you can do so using the following command:

        bash

        pip install -r requirements.txt



Run Your Project:

You can now run your project as usual.

bash

python main.py



## Download Executable Files and Binaries

In this project, you can download executable files and binaries for different operating systems to use alongside the Python scripts.

### Linux

You can download the Linux executable file from the following link:
- [Linux Executable](https://example.com/linux-executable)

After downloading, place the executable file in your project directory and ensure it's named "my_executable_linux."

### Windows

You can download the Windows executable file from the following link:
- [Windows Executable](https://example.com/windows-executable.exe)

After downloading, place the executable file in your project directory and ensure it's named "my_executable_windows."

**Note**: These executable files are meant to complement the Python scripts in this project and enhance compatibility with various operating systems.





## Usage

Use SecureFile to encrypt or decrypt your files and folders with ease. Follow the instructions below for usage:
    
### Options

- `-b, --break`: Switch roles (encryption to decryption or vice versa).
- `-h, --help`: Show this help message and exit.
- `-1, --encrypt/decrypt-folder`: Encrypt or decrypt the current folder.
- `-2, --encrypt/decrypt-file [filename]`: Encrypt or decrypt a specific file.
- `-5, --clear-console`: Clear the console for improved readability.


# Example: Encrypt files and folders in the current directory.
# Choose '2' for encryption and follow the prompts.
# You can specify a root directory when prompted or use the current directory.
# Encrypted files will be saved in the 'encrypted' subdirectory.
python main.py

# Example: Decrypt files and folders in the current directory.
# Choose '1' for decryption and follow the prompts.
# You will need the decryption key for this operation.
python main.py

# Example: Encrypt files in a specific directory.
# Choose '2' for encryption and specify the root directory when prompted.
# Encrypted files will be saved in the 'encrypted' subdirectory of the specified directory.
python main.py

# Example: Decrypt files in a specific directory.
# Choose '1' for decryption and specify the root directory when prompted.
# You will need the decryption key for this operation.
python main.py

# Example: Clear the console screen for improved readability.
# Choose '-5' to clear the console output.
python main.py

# Example: Display help information.
# Choose 'h', '-h', '--h', '--help', 'H', or 'h' for help.
python main.py

# To exit the script, you can press Ctrl+C or enter 'b' when prompted.



## Disclaimer

SecureFile is intended for educational purposes and should not be used for any malicious activities. Using it for unauthorized encryption or decryption of files may be illegal. Always consult with law enforcement or a cybersecurity expert before attempting any encryption or decryption.

Note: Ransomware techniques are illegal and unethical. This script is provided for educational purposes only and should be used responsibly and ethically.

