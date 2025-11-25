from Helper import *
from Helper.Common.utils import *
import Helper

def webhook_spreader():
    color = Helper.color
    clear()
    print_banner(color)
    print(f"{lc} {Fore.YELLOW}Webhook Spreader Module{Fore.RESET}")
    print(f"{ld} This module spreads webhooks across multiple channels/servers")
    print()
    
    webhook_url = input(f"{Fore.RESET}[{color}>{Fore.RESET}] Enter webhook URL to spread: ")
    if not webhook_url:
        print(f"{ld} {Fore.RED}Webhook URL cannot be empty!{Fore.RESET}")
        time.sleep(2)
        return
    
    print(f"{ld} {Fore.GREEN}Webhook Spreader functionality will be implemented here{Fore.RESET}")
    input(f"{Fore.RESET}[{color}>{Fore.RESET}] Press Enter to continue...")

