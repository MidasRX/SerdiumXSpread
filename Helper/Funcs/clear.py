from Helper import *
from Helper.Common.utils import *
import Helper

def clear_output():
    color = Helper.color
    clear()
    print_banner(color)
    print(f"{lc} {Fore.YELLOW}Clear Output Folder{Fore.RESET}")
    print()
    
    confirm = input(f"{Fore.RESET}[{color}>{Fore.RESET}] Are you sure you want to clear the Output folder? (y/n): ")
    if confirm.lower() == 'y':
        if os.path.exists("Output"):
            for root, dirs, files in os.walk("Output"):
                for file in files:
                    try:
                        os.remove(os.path.join(root, file))
                    except:
                        pass
            print(f"{ld} {Fore.GREEN}Output folder cleared!{Fore.RESET}")
        else:
            print(f"{ld} {Fore.RED}Output folder does not exist!{Fore.RESET}")
    else:
        print(f"{ld} {Fore.YELLOW}Operation cancelled{Fore.RESET}")
    
    time.sleep(2)

def clear_input():
    color = Helper.color
    clear()
    print_banner(color)
    print(f"{lc} {Fore.YELLOW}Clear Input Folder{Fore.RESET}")
    print()
    
    confirm = input(f"{Fore.RESET}[{color}>{Fore.RESET}] Are you sure you want to clear the Input folder? (y/n): ")
    if confirm.lower() == 'y':
        if os.path.exists("Input"):
            for root, dirs, files in os.walk("Input"):
                for file in files:
                    try:
                        os.remove(os.path.join(root, file))
                    except:
                        pass
            print(f"{ld} {Fore.GREEN}Input folder cleared!{Fore.RESET}")
        else:
            print(f"{ld} {Fore.RED}Input folder does not exist!{Fore.RESET}")
    else:
        print(f"{ld} {Fore.YELLOW}Operation cancelled{Fore.RESET}")
    
    time.sleep(2)

