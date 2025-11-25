from Helper import *
from Helper.Common.utils import *
import Helper

def proxy_checker():
    color = Helper.color
    clear()
    print_banner(color)
    print(f"{lc} {Fore.YELLOW}Proxy Checker Module{Fore.RESET}")
    print(f"{ld} This module checks proxy validity")
    print()
    
    proxies = get_proxies()
    if not proxies:
        print(f"{ld} {Fore.RED}No proxies found in Input/proxies.txt!{Fore.RESET}")
        time.sleep(2)
        return
    
    print(f"{ld} {Fore.GREEN}Found {len(proxies)} proxies to check{Fore.RESET}")
    print(f"{ld} {Fore.GREEN}Proxy Checker functionality will be implemented here{Fore.RESET}")
    input(f"{Fore.RESET}[{color}>{Fore.RESET}] Press Enter to continue...")

