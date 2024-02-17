
from cyber.scripts.decrypter.dec_run import dec_main
from cyber.scripts.encrypter.enc_run import enc_main
from common_functions import save_load_program_data  ,get_root_dir,enc_help,clear_console , obfuscate_credentials , deobfuscate_credentials
import os

class RunProgram():
    
    def __init__(self) -> None:
        self.starting_directory= os.getcwd()
        self.HELP_OPTIONS = ['-h', '--h', '--help', '-H', 'h', 'H']
    
        
        if os.path.exists("cyber/scripts"):
            os.chdir("cyber/scripts")
        
        self.program_configuration_path= "conf.pkl"
        self.key_path = "key.txt"
        self.program_configuration = save_load_program_data(self.program_configuration_path , mode='rb')
        
        if self.program_configuration != None:
            self.program_configuration  = deobfuscate_credentials(self.program_configuration)
            proposed_path = self.program_configuration['last_path']
            if  proposed_path != None and os.path.exists(proposed_path):
                self.starting_directory  = proposed_path
        else:
            
            self.starting_directory = get_root_dir()
            self.program_configuration = {
                    'username': 'john_doe',
                    'password': 'password123',
                    'email': 'john@example.com',
                    "last_path": self.starting_directory
                    }
            for key  in self.program_configuration.keys():
                if key == 'password':
                    print("Make sure to remember you password cause there is no resetting it ")
                
                default_values = self.program_configuration[key]
                value = input(f"Set {key}:Press enter to leave as default {default_values}: ")
                if value.strip() != "":
                    self.program_configuration[key] = value
                    
            data = obfuscate_credentials(self.program_configuration)
            save_load_program_data(self.program_configuration_path , data=data ,mode='wb')
            
        


    def verify(self , count = 1):
        
        if count > 1:
            print(f"Invalid password Input password\nTrial {count}" )
        else:   
            print(f"Input password\nTrial {count}" )
        password = input(": ")

        if password == 'b':
            return "b"
        return  password.strip() == self.program_configuration['password']
    

    def main(self):
       
        while True:
            try:
                # clear_console()
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
                    save_load_program_data(self.program_configuration_path , data=obfuscate_credentials(self.program_configuration)
                                                  ,mode='wb')
                    
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
        print("veryfying")
      
        count = 1
        while count < 4:
            verified = self.verify(count=count)
            
            
            if not verified and count == 3:
                print("Not authorized\nGoodBye!!!!")
                break 
            elif verified:
                break
            
            elif verified == 'b':
                break
            count +=1
            
        if verified == True:
            self.main()
     


if __name__ == "__main__":
    RunProgram().run()
