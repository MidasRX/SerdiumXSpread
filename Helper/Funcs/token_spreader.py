from Helper import *
from Helper.Common.utils import *
import Helper

def token_spreader():
    color = Helper.color
    clear()
    print_banner(color)
    print(f"{lc} {Fore.YELLOW}Token Spreader Module{Fore.RESET}")
    print(f"{ld} This module spreads tokens across multiple channels/servers")
    print()
    
    tokens = get_tokens()
    if not tokens:
        print(f"{ld} {Fore.RED}No tokens found in Input/tokens.txt!{Fore.RESET}")
        time.sleep(2)
        return
    
    print(f"{ld} {Fore.GREEN}Found {len(tokens)} tokens{Fore.RESET}")
    print(f"{ld} {Fore.GREEN}Token Spreader functionality will be implemented here{Fore.RESET}")
    input(f"{Fore.RESET}[{color}>{Fore.RESET}] Press Enter to continue...")

