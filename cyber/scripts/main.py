
from cyber.scripts.decrypter.dec_run import dec_main
from cyber.scripts.encrypter.enc_run import enc_main
from cyber.scripts.common_functions import get_root_dir,enc_help,clear_console,save_load_program_data
import os


class RunProgram():
    
    def __init__(self) -> None:
        self.HELP_OPTIONS = ['-h', '--h', '--help', '-H', 'h', 'H']
        self.program_configuration_path= "conf.json"
        
        self.program_configuration = save_load_program_data(self.program_configuration_path , mode='r')
        
        proposed_path = self.program_configuration['last_path']
        if  os.path.exists(proposed_path):
             self.starting_directory  = proposed_path
        else:
            self.starting_directory = get_root_dir()
            
        self.key_path = "/home/brian/Desktop/encrypter_decrypter/key2.txt"


    def verify(self):
        print("Veryfy its you 1 == ?" )
        print("8%#8\t"*100)
        return True
    

    def main(self):
        while True:
            try:
                clear_console()
                choice = input("Decrypt = 1\nEncrypt = 2\n>:")
                if choice not in self.HELP_OPTIONS and choice != '-5' and choice != 'b':
                    
                    if choice == '1':
                        process = "Decryption"
                        prev_dest = dec_main(self.starting_directory ,  key_path = self.key_path)
                        self.program_configuration['last_path'] = prev_dest
                        self.starting_directory = prev_dest
                        
                    elif choice == '2':
                        process = "Encryption"
                        prev_dest = enc_main(self.starting_directory , key_path = self.key_path)
                        self.program_configuration['last_path'] = prev_dest
                        self.starting_directory = prev_dest
                        
                elif choice == 'b':
                    self.program_configuration = save_load_program_data(self.program_configuration_path , data=self.program_configuration,mode='w')
                    break
                elif choice == '-5':
                    print("Clearing screen" , self.program_configuration)
                    clear_console()
                elif choice in self.HELP_OPTIONS:
                    print("#" * 20)
                    print(enc_help())
                else:
                    pass
            except KeyboardInterrupt:
                break
            except UnboundLocalError:
                pass

    
    def run(self):
        print("Beryfying")
        
        if self.verify:
            self.main()
        else:
            print("Not authorized\nGoodBye!!!!")
        




if __name__ == "__main__":
    RunProgram().run()
