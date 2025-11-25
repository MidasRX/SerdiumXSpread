from Helper import *
from Helper.Common.utils import *
import Helper

def message_spreader():
    color = Helper.color
    clear()
    print_banner(color)
    print(f"{lc} {Fore.YELLOW}Message Spreader Module{Fore.RESET}")
    print(f"{ld} This module spreads messages across multiple channels/servers")
    print()
    
    message = input(f"{Fore.RESET}[{color}>{Fore.RESET}] Enter message to spread: ")
    if not message:
        print(f"{ld} {Fore.RED}Message cannot be empty!{Fore.RESET}")
        time.sleep(2)
        return
    
    print(f"{ld} {Fore.GREEN}Message Spreader functionality will be implemented here{Fore.RESET}")
    input(f"{Fore.RESET}[{color}>{Fore.RESET}] Press Enter to continue...")

