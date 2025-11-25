from Helper import *
from Helper.Common.utils import *
import Helper

def telegram_auth():
    """Authenticate Telegram account using phone number"""
    color = Helper.color
    new_title("Telegram Authentication")
    clear()
    print_banner(color)
    print(f"{lc} {Fore.YELLOW}Telegram Authentication{Fore.RESET}")
    print(f"{ld} {Fore.CYAN}You need API ID and API Hash from https://my.telegram.org{Fore.RESET}")
    print()
    
    try:
        from telethon import TelegramClient
        from telethon.errors import SessionPasswordNeededError
    except ImportError:
        print(f"{ld} {Fore.RED}Telethon is not installed!{Fore.RESET}")
        print(f"{ld} {Fore.YELLOW}Install it with: pip install telethon{Fore.RESET}")
        input(f"{Fore.RESET}[{color}>{Fore.RESET}] Press Enter to continue...")
        return None
    
    api_id = input(f"{Fore.RESET}[{color}>{Fore.RESET}] API ID: ")
    if not api_id or not api_id.isdigit():
        print(f"{ld} {Fore.RED}Invalid API ID!{Fore.RESET}")
        time.sleep(2)
        return None
    
    api_hash = input(f"{Fore.RESET}[{color}>{Fore.RESET}] API Hash: ")
    if not api_hash:
        print(f"{ld} {Fore.RED}API Hash cannot be empty!{Fore.RESET}")
        time.sleep(2)
        return None
    
    phone = input(f"{Fore.RESET}[{color}>{Fore.RESET}] Phone Number (with country code, e.g., +1234567890): ")
    if not phone:
        print(f"{ld} {Fore.RED}Phone number cannot be empty!{Fore.RESET}")
        time.sleep(2)
        return None
    
    # Create session file name based on phone
    session_name = f"telegram_{phone.replace('+', '').replace('-', '').replace(' ', '')}"
    
    try:
        print(f"\n{ld} {Fore.GREEN}Connecting to Telegram...{Fore.RESET}")
        client = TelegramClient(session_name, int(api_id), api_hash)
        client.connect()
        
        if not client.is_user_authorized():
            print(f"{ld} {Fore.YELLOW}Sending code to {phone}...{Fore.RESET}")
            client.send_code_request(phone)
            
            code = input(f"{Fore.RESET}[{color}>{Fore.RESET}] Enter the code you received: ")
            if not code:
                print(f"{ld} {Fore.RED}Code cannot be empty!{Fore.RESET}")
                client.disconnect()
                time.sleep(2)
                return None
            
            try:
                client.sign_in(phone, code)
            except SessionPasswordNeededError:
                password = input(f"{Fore.RESET}[{color}>{Fore.RESET}] Enter your 2FA password: ")
                client.sign_in(password=password)
            
            print(f"{ld} {Fore.GREEN}Successfully authenticated!{Fore.RESET}")
        else:
            print(f"{ld} {Fore.GREEN}Already authenticated!{Fore.RESET}")
        
        # Get user info
        me = client.get_me()
        print(f"{ld} {Fore.CYAN}Logged in as: {me.first_name} {me.last_name or ''} (@{me.username or 'no username'}){Fore.RESET}")
        
        return client
    except Exception as e:
        print(f"{ld} {Fore.RED}Authentication failed: {e}{Fore.RESET}")
        log_error(f"Telegram authentication failed: {str(e)}", "ERROR", "telegram_auth")
        return None

