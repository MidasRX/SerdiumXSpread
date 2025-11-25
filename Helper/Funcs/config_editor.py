from Helper import *
from Helper.Common.utils import *
import Helper

def config_editor():
    color = Helper.color
    clear()
    print_banner(color)
    print(f"{lc} {Fore.YELLOW}Config Editor Module{Fore.RESET}")
    print(f"{ld} This module allows you to edit configuration settings")
    print()
    
    config = load_config()
    print(f"{ld} Current configuration:")
    for key, value in config.items():
        print(f"{ld}   {key}: {value}")
    
    print(f"{ld} {Fore.GREEN}Config Editor functionality will be implemented here{Fore.RESET}")
    input(f"{Fore.RESET}[{color}>{Fore.RESET}] Press Enter to continue...")

