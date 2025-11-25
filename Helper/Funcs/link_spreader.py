from Helper import *
from Helper.Common.utils import *
import Helper

def link_spreader():
    color = Helper.color
    clear()
    print_banner(color)
    print(f"{lc} {Fore.YELLOW}Link Spreader Module{Fore.RESET}")
    print(f"{ld} This module spreads links across multiple channels/servers")
    print()
    
    link = input(f"{Fore.RESET}[{color}>{Fore.RESET}] Enter link to spread: ")
    if not link:
        print(f"{ld} {Fore.RED}Link cannot be empty!{Fore.RESET}")
        time.sleep(2)
        return
    
    print(f"{ld} {Fore.GREEN}Link Spreader functionality will be implemented here{Fore.RESET}")
    input(f"{Fore.RESET}[{color}>{Fore.RESET}] Press Enter to continue...")

