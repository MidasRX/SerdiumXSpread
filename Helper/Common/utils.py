from Helper import *

def clear():
    os.system("cls")

def get_tokens():
    if os.path.exists("Input/tokens.txt"):
        with open("Input/tokens.txt", "r", encoding="utf-8") as file:
            tokens = file.readlines()
            return [token.strip() for token in tokens if token.strip()]
    return []

def get_tokens_or_input(prompt="Token"):
    """Get tokens from file or user input"""
    try:
        import Helper
        color = Helper.color
    except:
        color = Fore.LIGHTCYAN_EX
    
    choice = input(f"{Fore.RESET}[{color}>{Fore.RESET}] Use Input/tokens.txt (1) or Enter token manually (2)? (1/2): ")
    
    if choice == "2":
        token = input(f"{Fore.RESET}[{color}>{Fore.RESET}] Enter {prompt}: ")
        if not token:
            return []
        return [token.strip()]
    else:
        tokens = get_tokens()
        if not tokens:
            print(f"{ld} {Fore.RED}No tokens found in Input/tokens.txt!{Fore.RESET}")
            manual = input(f"{Fore.RESET}[{color}>{Fore.RESET}] Enter token manually? (y/n): ")
            if manual.lower() == 'y':
                token = input(f"{Fore.RESET}[{color}>{Fore.RESET}] Enter {prompt}: ")
                if token:
                    return [token.strip()]
        return tokens

def get_proxies():
    if os.path.exists("Input/proxies.txt"):
        with open("Input/proxies.txt", "r", encoding="utf-8") as file:
            proxies = file.readlines()
            return [proxy.strip() for proxy in proxies if proxy.strip()]
    return []

def log_error(error_message, error_type="ERROR", function_name=""):
    """Log errors and problems to Log.txt"""
    try:
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [{error_type}]"
        if function_name:
            log_entry += f" [{function_name}]"
        log_entry += f" {error_message}\n"
        
        # Ensure Output directory exists
        if not os.path.exists("Output"):
            os.makedirs("Output")
        
        with open("Output/Log.txt", "a", encoding="utf-8") as log_file:
            log_file.write(log_entry)
    except Exception as e:
        # If logging fails, at least print it
        print(f"Failed to write to log: {e}")

def log_info(info_message, function_name=""):
    """Log info messages to Log.txt"""
    log_error(info_message, "INFO", function_name)

def log_warning(warning_message, function_name=""):
    """Log warnings to Log.txt"""
    log_error(warning_message, "WARNING", function_name)

def new_title(title):
    os.system(f"title {title}")

def load_config():
    if os.path.exists('config.json'):
        with open('config.json', 'r', encoding="utf-8") as f:
            config = json.load(f)
            return config
    return {}

def save_config(config):
    with open('config.json', 'w', encoding="utf-8") as f:
        json.dump(config, f, indent=4)

def GetFormattedProxy(filename):
    if os.path.exists(filename):
        proxy = random.choice(open(filename, encoding="cp437").read().splitlines()).strip()
        if '@' in proxy:
            return proxy
        elif len(proxy.split(':')) == 2:
            return proxy
        else:
            if '.' in proxy.split(':')[0]:
                return ':'.join(proxy.split(':')[2:]) + '@' + ':'.join(proxy.split(':')[:2])
            else:
                return ':'.join(proxy.split(':')[:2]) + '@' + ':'.join(proxy.split(':')[2:])
    return None

def generate_password():
    return secrets.token_hex(16)

def get_headers(token=None):
    headers = {
        "authority": "discord.com",
        "accept": "*/*",
        "accept-language": "en-US",
        "connection": "keep-alive",
        "content-type": "application/json",
        "origin": "https://discord.com",
        "referer": "https://discord.com/",
        'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="122"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        "x-debug-options": "bugReporterEnabled",
        "x-discord-locale": "en-US",
        "x-discord-timezone": "America/New_York",
        "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDExIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDUiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTc5ODgyLCJuYXRpdmVfYnVpbGRfbnVtYmVyIjozMDMwNiwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ==",
    }
    if token:
        headers["authorization"] = token
    return headers

lc = f"{Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.LIGHTCYAN_EX}S{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}"
ld = f"{Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.LIGHTCYAN_EX}-{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}"

banner = f'''{Fore.LIGHTCYAN_EX}
                    ███████╗███████╗██████╗ ██████╗ ██╗██╗   ██╗███╗   ███╗    ██╗  ██╗    ███████╗██████╗ ███████╗ █████╗ ██████╗ ██████╗ 
                    ██╔════╝██╔════╝██╔══██╗██╔══██╗██║██║   ██║████╗ ████║    ╚██╗██╔╝    ██╔════╝██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔══██╗
                    ███████╗█████╗  ██████╔╝██║  ██║██║██║   ██║██╔████╔██║     ╚███╔╝     ███████╗██████╔╝█████╗  ███████║██║  ██║██║  ██║
                    ╚════██║██╔══╝  ██╔══██╗██║  ██║██║██║   ██║██║╚██╔╝██║     ██╔██╗     ╚════██║██╔═══╝ ██╔══╝  ██╔══██║██║  ██║██║  ██║
                    ███████║███████╗██║  ██║██████╔╝██║╚██████╔╝██║ ╚═╝ ██║    ██╔╝ ██╗    ███████║██║     ███████╗██║  ██║██████╔╝██████╔╝
                    ╚══════╝╚══════╝╚═╝  ╚═╝╚═════╝ ╚═╝ ╚═════╝ ╚═╝     ╚═╝    ╚═╝  ╚═╝    ╚══════╝╚═╝     ╚══════╝╚═╝  ╚═╝╚═════╝ ╚═════╝ 
                                                                    SerdiumX Spread Tool v1.0.0
    '''

def print_banner(color=Fore.LIGHTCYAN_EX):
    print(f'''{color}
                    ███████╗███████╗██████╗ ██████╗ ██╗██╗   ██╗███╗   ███╗    ██╗  ██╗    ███████╗██████╗ ███████╗ █████╗ ██████╗ ██████╗ 
                    ██╔════╝██╔════╝██╔══██╗██╔══██╗██║██║   ██║████╗ ████║    ╚██╗██╔╝    ██╔════╝██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔══██╗
                    ███████╗█████╗  ██████╔╝██║  ██║██║██║   ██║██╔████╔██║     ╚███╔╝     ███████╗██████╔╝█████╗  ███████║██║  ██║██║  ██║
                    ╚════██║██╔══╝  ██╔══██╗██║  ██║██║██║   ██║██║╚██╔╝██║     ██╔██╗     ╚════██║██╔═══╝ ██╔══╝  ██╔══██║██║  ██║██║  ██║
                    ███████║███████╗██║  ██║██████╔╝██║╚██████╔╝██║ ╚═╝ ██║    ██╔╝ ██╗    ███████║██║     ███████╗██║  ██║██████╔╝██████╔╝
                    ╚══════╝╚══════╝╚═╝  ╚═╝╚═════╝ ╚═╝ ╚═════╝ ╚═╝     ╚═╝    ╚═╝  ╚═╝    ╚══════╝╚═╝     ╚══════╝╚═╝  ╚═╝╚═════╝ ╚═════╝ 
                                                                    SerdiumX Spread Tool v1.0.0
    ''')

