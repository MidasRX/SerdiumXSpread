from Helper import *
from Helper.Common.utils import *

Files = [
    'Log.txt'
]

dirs = [
    'Spreads',
    'Spreads/Files',
    'Spreads/Messages',
    'Spreads/Links',
    'Spreads/Emails',
    'Spreads/Webhooks',
    'Proxies',
    'Proxies/Scraped'
]

def StartupTool():
    # Check if everything already exists - if so, skip startup
    all_exist = True
    
    # Check main directories
    if not os.path.exists(f"Output"):
        all_exist = False
    if not os.path.exists(f"Input"):
        all_exist = False
    
    # Check subdirectories
    for dir in dirs:
        if not os.path.exists(f"Output/{dir}"):
            all_exist = False
            break
    
    # Check output files
    for file in Files:
        if not os.path.exists(f"Output/{file}"):
            all_exist = False
            break
    
    # Check input files
    default_input_files = ['tokens.txt', 'proxies.txt', 'messages.txt', 'links.txt', 'emails.txt']
    for file in default_input_files:
        if not os.path.exists(f"Input/{file}"):
            all_exist = False
            break
    
    # If everything exists, skip startup
    if all_exist:
        return
    
    # Otherwise, run startup (only creates missing items, no "EXISTS ALREADY" messages)
    new_title("SerdiumXSpread Startup")
    if not os.path.exists(f"Output"):
        os.makedirs(f"Output")
        print(f"{lc} {Fore.BLUE}Folder={Fore.WHITE}Output{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.GREEN}CREATED{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}")
        time.sleep(0.3)
    
    if not os.path.exists(f"Input"):
        os.makedirs(f"Input")
        print(f"{lc} {Fore.BLUE}Folder={Fore.WHITE}Input{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.GREEN}CREATED{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}")
        time.sleep(0.3)
    
    for dir in dirs:
        if not os.path.exists(f"Output/{dir}"):
            os.makedirs(f"Output/{dir}")
            print(f"{lc} {Fore.BLUE}Folder={Fore.WHITE}{dir}{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.GREEN}CREATED{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}")
            time.sleep(0.3)
    
    for file in Files:
        if not os.path.exists(f"Output/{file}"):
            with open(f"Output/{file}", 'w', encoding="utf-8") as f:
                pass
            print(f"{lc} {Fore.BLUE}File={Fore.WHITE}{file}{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.GREEN}CREATED{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}")
            time.sleep(0.3)
    
    # Create default input files if they don't exist
    default_input_files = ['tokens.txt', 'proxies.txt', 'messages.txt', 'links.txt', 'emails.txt', 'telegram_messages.txt', 'group_id.txt', 'email_accounts.txt']
    for file in default_input_files:
        if not os.path.exists(f"Input/{file}"):
            with open(f"Input/{file}", 'w', encoding="utf-8") as f:
                pass
            print(f"{lc} {Fore.BLUE}File={Fore.WHITE}Input/{file}{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.GREEN}CREATED{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}")
            time.sleep(0.3)

