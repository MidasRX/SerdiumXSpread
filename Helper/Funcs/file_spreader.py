from Helper import *
from Helper.Common.utils import *
import Helper

def file_spreader():
    color = Helper.color
    clear()
    print_banner(color)
    print(f"{lc} {Fore.YELLOW}File Spreader Module{Fore.RESET}")
    print(f"{ld} This module spreads files across multiple channels/servers")
    print()
    
    file_path = input(f"{Fore.RESET}[{color}>{Fore.RESET}] Enter file path to spread: ")
    if not os.path.exists(file_path):
        print(f"{ld} {Fore.RED}File not found!{Fore.RESET}")
        time.sleep(2)
        return
    
    print(f"{ld} {Fore.GREEN}File Spreader functionality will be implemented here{Fore.RESET}")
    input(f"{Fore.RESET}[{color}>{Fore.RESET}] Press Enter to continue...")

