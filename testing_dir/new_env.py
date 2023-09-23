

from cyber.scripts.common_functions import process_directory


f = process_directory(input('ENer dir'))
full_path = "/home/brian/PycharmProjects/pyinstaller/git_hub/file-encryption-and-decryption/testing_dir/full.txt"
for i in f:
    with open (i  , 'r') as f:
        cont = f.read()
    with open (full_path , 'a') as f:
        f.write(cont)