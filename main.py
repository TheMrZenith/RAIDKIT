from pathlib import Path
from colorama import Fore
import os 

filepath = Path(__file__).resolve().parent / "src" / "raidbot.py"

def clear(): os.system('cls' if os.name == 'nt' else 'clear')


banner = """
 ██▀███   ▄▄▄       ██▓▓█████▄  ▄▄▄▄    ▒█████  ▄▄▄█████▓   
▓██ ▒ ██▒▒████▄    ▓██▒▒██▀ ██▌▓█████▄ ▒██▒  ██▒▓  ██▒ ▓▒   
▓██ ░▄█ ▒▒██  ▀█▄  ▒██▒░██   █▌▒██▒ ▄██▒██░  ██▒▒ ▓██░ ▒░   
▒██▀▀█▄  ░██▄▄▄▄██ ░██░░▓█▄   ▌▒██░█▀  ▒██   ██░░ ▓██▓ ░    
░██▓ ▒██▒ ▓█   ▓██▒░██░░▒████▓ ░▓█  ▀█▓░ ████▓▒░  ▒██▒ ░    
░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░▓   ▒▒▓  ▒ ░▒▓███▀▒░ ▒░▒░▒░   ▒ ░░      
  ░▒ ░ ▒░  ▒   ▒▒ ░ ▒ ░ ░ ▒  ▒ ▒░▒   ░   ░ ▒ ▒░     ░       
  ░░   ░   ░   ▒    ▒ ░ ░ ░  ░  ░    ░ ░ ░ ░ ▒    ░         
   ░           ░  ░ ░     ░     ░          ░ ░              
                        ░            ░       
                                              By Zsocietyy"""
def main():
    while True:
        try:
          clear()
          print(Fore.MAGENTA + banner)
          token = input(f"{Fore.GREEN}[*]{Fore.MAGENTA} Enter your token: ").strip()
          if not token:
              print(f"{Fore.RED}Error: Token cannot be None.{Fore.RESET}")
              continue

          server_id = input(f"{Fore.GREEN}[*]{Fore.MAGENTA} Enter your server ID: ").strip()
          if not server_id:
              print(f"{Fore.RED}Error: Server ID cannot be None.{Fore.RESET}")
              continue

          if not server_id.isdigit():
              print(f"{Fore.RED}Error: Server ID must be a number.{Fore.RESET}")
              continue
          
          os.system(f"python \"{filepath}\" --token \"{token}\" --guild_id {server_id}")

        except KeyboardInterrupt:
           print(f"{Fore.RED}Process interrupted. Exiting...{Fore.RESET}")
           exit(1)
      

if __name__ == "__main__":
  main()
