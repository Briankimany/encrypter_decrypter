
from cyber.scripts.decrypter.dec_run import dec_main
from cyber.scripts.encrypter.enc_run import enc_main
from cyber.scripts.common_functions import (
    root,
    enc_help,
    clear_console
)

HELP_OPTIONS = ['-h', '--h', '--help', '-H', 'h', 'H']
def main():
    while True:
        try:
            choice = input("Decrypt = 1\nEncrypt = 2\n:")
            if choice not in HELP_OPTIONS and choice != '-5' and choice != 'b':
                starting_directory = root()
                if choice == '1':
                    process = "Decryption"
                    dec_main(starting_directory)
                elif choice == '2':
                    process = "Encryption"
                    enc_main(starting_directory)
            elif choice == 'b':
                break
            elif choice == '-5':
                print("Clearing screen")
                clear_console()
            elif choice in HELP_OPTIONS:
                print("#" * 20)
                print(enc_help())
        except KeyboardInterrupt:
            break
        except UnboundLocalError:
            pass

if __name__ == "__main__":
    main()
