from Helper import *
from Helper.Common.utils import *
import Helper
import threading

# Global counters
valid_count = 0
invalid_count = 0
locked_count = 0
nitro_count = 0
mail_verified_count = 0
phone_verified_count = 0
full_verified_count = 0
unclaimed_count = 0
total_checked = 0

def check_token_verification(token):
    """Check token verification status"""
    global mail_verified_count, phone_verified_count, full_verified_count, unclaimed_count
    headers = {'Authorization': token}
    
    try:
        response = requests.get('https://discord.com/api/v10/users/@me', headers=headers, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            email_verification = data.get('verified', False)
            phone_verification = bool(data.get('phone'))
            
            if email_verification and phone_verification:
                full_verified_count += 1
                return "Full Verified"
            elif email_verification:
                mail_verified_count += 1
                return "Mail Verified"
            elif phone_verification:
                phone_verified_count += 1
                return "Phone Verified"
            else:
                unclaimed_count += 1
                return "Unclaimed"
        elif response.status_code == 401:
            return "Invalid"
        else:
            return "Error"
    except Exception as e:
        log_error(f"Error checking verification for token {token[:20]}...: {str(e)}", "ERROR", "check_token_verification")
        return "Error"

def check_boosts(token):
    """Check server boost count"""
    headers = {'Authorization': token}
    
    try:
        response = requests.get('https://discord.com/api/v9/users/@me/guilds/premium/subscription/slots', headers=headers, timeout=10)
        if response.status_code == 200:
            boosts = len(response.json())
            return boosts
        return 0
    except Exception as e:
        log_error(f"Error checking boosts for token {token[:20]}...: {str(e)}", "ERROR", "check_boosts")
        return 0

def check_token(token, count_lock):
    """Check a single token"""
    global valid_count, invalid_count, locked_count, nitro_count, total_checked
    color = Helper.color
    headers = {'Authorization': token}
    
    try:
        # Check if token is valid
        response = requests.get('https://discord.com/api/v9/users/@me', headers=headers, timeout=10)
        
        if response.status_code == 200:
            # Check if token is unlocked
            try:
                settings_response = requests.get("https://discordapp.com/api/v6/users/@me/settings", headers=headers, timeout=10)
                if settings_response.status_code == 200:
                    with count_lock:
                        valid_count += 1
                        total_checked += 1
                    
                    user_data = response.json()
                    premium_type = user_data.get('premium_type', 0)
                    verification = check_token_verification(token)
                    boosts = check_boosts(token)
                    
                    nitro_status = f"{Style.BRIGHT}{Fore.RED}NO_NITRO" if premium_type == 0 else f"{Style.BRIGHT}{Fore.GREEN}NITRO"
                    if premium_type != 0:
                        with count_lock:
                            nitro_count += 1
                    
                    print(f'{lc} {Fore.BLUE}token={Fore.WHITE}{token[:20]}...{Fore.RESET} {Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.GREEN}VALID{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET} {Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.BLUE}{boosts}_BOOSTS{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET} {Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.BLUE}{nitro_status}{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET} {Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.BLUE}{verification}{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET} {Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.GREEN}UNLOCKED{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}')
                    log_info(f"Token {token[:20]}... is VALID - Nitro: {premium_type != 0}, Boosts: {boosts}, Verification: {verification}", "token_checker")
                else:
                    with count_lock:
                        locked_count += 1
                        total_checked += 1
                    print(f'{lc} {Fore.BLUE}token={Fore.WHITE}{token[:20]}...{Fore.RESET} {Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.YELLOW}LOCKED{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}')
                    log_warning(f"Token {token[:20]}... is LOCKED (status code: {settings_response.status_code})", "token_checker")
            except Exception as e:
                with count_lock:
                    locked_count += 1
                    total_checked += 1
                print(f'{lc} {Fore.BLUE}token={Fore.WHITE}{token[:20]}...{Fore.RESET} {Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.YELLOW}LOCKED{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}')
                log_error(f"Error checking token lock status {token[:20]}...: {str(e)}", "ERROR", "token_checker")
        elif response.status_code == 401:
            with count_lock:
                invalid_count += 1
                total_checked += 1
            print(f'{lc} {Fore.BLUE}token={Fore.WHITE}{token[:20]}...{Fore.RESET} {Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.RED}INVALID{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}')
            log_warning(f"Token {token[:20]}... is INVALID", "token_checker")
        else:
            with count_lock:
                invalid_count += 1
                total_checked += 1
            print(f'{lc} {Fore.BLUE}token={Fore.WHITE}{token[:20]}...{Fore.RESET} {Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.RED}ERROR: {response.status_code}{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}')
            log_error(f"Token {token[:20]}... check failed with status code: {response.status_code}", "ERROR", "token_checker")
    except requests.exceptions.Timeout:
        with count_lock:
            invalid_count += 1
            total_checked += 1
        print(f'{lc} {Fore.BLUE}token={Fore.WHITE}{token[:20]}...{Fore.RESET} {Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.RED}TIMEOUT{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}')
        log_error(f"Token {token[:20]}... check timed out", "ERROR", "token_checker")
    except Exception as e:
        with count_lock:
            invalid_count += 1
            total_checked += 1
        print(f'{lc} {Fore.BLUE}token={Fore.WHITE}{token[:20]}...{Fore.RESET} {Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.RED}ERROR{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}')
        log_error(f"Error checking token {token[:20]}...: {str(e)}", "ERROR", "token_checker")

def token_checker():
    color = Helper.color
    new_title("Token Checker")
    clear()
    print_banner(color)
    print(f"{lc} {Fore.YELLOW}Token Checker{Fore.RESET}")
    print()
    
    tokens = get_tokens_or_input("token")
    if not tokens:
        print(f"{ld} {Fore.RED}No tokens provided!{Fore.RESET}")
        log_warning("No tokens provided for checking", "token_checker")
        time.sleep(2)
        return
    
    global valid_count, invalid_count, locked_count, nitro_count, mail_verified_count, phone_verified_count, full_verified_count, unclaimed_count, total_checked
    
    # Reset counters
    valid_count = 0
    invalid_count = 0
    locked_count = 0
    nitro_count = 0
    mail_verified_count = 0
    phone_verified_count = 0
    full_verified_count = 0
    unclaimed_count = 0
    total_checked = 0
    
    print(f"{ld} {Fore.GREEN}Checking {len(tokens)} token(s)...{Fore.RESET}")
    print()
    
    count_lock = threading.Lock()
    threads = []
    
    for token in tokens:
        token = token.strip()
        if not token:
            continue
        thread = threading.Thread(target=check_token, args=(token, count_lock))
        thread.start()
        threads.append(thread)
        time.sleep(0.1)  # Small delay to avoid rate limits
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()
    
    # Print summary
    print()
    print(f"{ld} {Fore.CYAN}{'='*50}{Fore.RESET}")
    print(f"{ld} {Fore.GREEN}Token Check Summary:{Fore.RESET}")
    print(f"{ld} {Fore.CYAN}Total Checked: {total_checked}{Fore.RESET}")
    print(f"{ld} {Fore.GREEN}Valid: {valid_count}{Fore.RESET}")
    print(f"{ld} {Fore.RED}Invalid: {invalid_count}{Fore.RESET}")
    print(f"{ld} {Fore.YELLOW}Locked: {locked_count}{Fore.RESET}")
    print(f"{ld} {Fore.MAGENTA}Nitro: {nitro_count}{Fore.RESET}")
    print(f"{ld} {Fore.BLUE}Full Verified: {full_verified_count}{Fore.RESET}")
    print(f"{ld} {Fore.BLUE}Mail Verified: {mail_verified_count}{Fore.RESET}")
    print(f"{ld} {Fore.BLUE}Phone Verified: {phone_verified_count}{Fore.RESET}")
    print(f"{ld} {Fore.BLUE}Unclaimed: {unclaimed_count}{Fore.RESET}")
    print(f"{ld} {Fore.CYAN}{'='*50}{Fore.RESET}")
    
    log_info(f"Token check completed - Valid: {valid_count}, Invalid: {invalid_count}, Locked: {locked_count}, Nitro: {nitro_count}", "token_checker")
    
    input(f"{Fore.RESET}[{color}>{Fore.RESET}] Press Enter to continue...")

