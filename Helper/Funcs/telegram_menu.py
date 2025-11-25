from Helper import *
from Helper.Common.utils import *
from Helper.Funcs.telegram_auth import telegram_auth
from Helper.Funcs.telegram_tools import auto_forward_messages, nuke_telegram_account
import Helper
import asyncio

def telegram_menu():
    color = Helper.color
    new_title("SerdiumXSpread │ Telegram Spreader")
    clear()
    print_banner(color)
    print(f"""
                    {color}<<{Fore.RESET}1{color}>>  [{Fore.RESET}Auto Forward{color}]               {color}<<{Fore.RESET}4{color}>>  [{Fore.RESET}Account Nuker{color}]
                    {color}<<{Fore.RESET}2{color}>>  [{Fore.RESET}Spread Message{color}]           {color}<<{Fore.RESET}5{color}>>  [{Fore.RESET}Spread Media{color}]
                    {color}<<{Fore.RESET}3{color}>>  [{Fore.RESET}Spread Link{color}]                {color}<<{Fore.RESET}6{color}>>  [{Fore.RESET}Spread File{color}]
                                                                        {color}<<{Fore.RESET}0{color}>>  [{Fore.RESET}Back to Main Menu{color}]
    """)
    choice = input(f"{Fore.RESET}[{color}>{Fore.RESET}] Choice: ")
    functions = {
        "1": telegram_auto_forward,
        "2": telegram_spread_message,
        "3": telegram_spread_link,
        "4": telegram_account_nuker,
        "5": telegram_spread_media,
        "6": telegram_spread_file
    }
    if choice == "0":
        return  # Return to main menu
    
    function = functions.get(choice)
    if function:
        result = function()
        if result:
            return  # If function returns something, go back to main
        telegram_menu()
    else:
        print("Invalid choice")
        time.sleep(1)
        telegram_menu()

def telegram_spread_message():
    color = Helper.color
    clear()
    print_banner(color)
    print(f"{lc} {Fore.YELLOW}Telegram Message Spreader{Fore.RESET}")
    print()
    message = input(f"{Fore.RESET}[{color}>{Fore.RESET}] Enter message to spread: ")
    if not message:
        print(f"{ld} {Fore.RED}Message cannot be empty!{Fore.RESET}")
        time.sleep(2)
        return
    
    print(f"{ld} {Fore.GREEN}Telegram Message Spreader functionality will be implemented here{Fore.RESET}")
    print(f"{ld} Message: {Fore.CYAN}{message}{Fore.RESET}")
    input(f"{Fore.RESET}[{color}>{Fore.RESET}] Press Enter to continue...")

def telegram_spread_link():
    color = Helper.color
    clear()
    print_banner(color)
    print(f"{lc} {Fore.YELLOW}Telegram Link Spreader{Fore.RESET}")
    print()
    link = input(f"{Fore.RESET}[{color}>{Fore.RESET}] Enter link to spread: ")
    if not link:
        print(f"{ld} {Fore.RED}Link cannot be empty!{Fore.RESET}")
        time.sleep(2)
        return
    
    print(f"{ld} {Fore.GREEN}Telegram Link Spreader functionality will be implemented here{Fore.RESET}")
    print(f"{ld} Link: {Fore.CYAN}{link}{Fore.RESET}")
    input(f"{Fore.RESET}[{color}>{Fore.RESET}] Press Enter to continue...")

def telegram_spread_bot_token():
    color = Helper.color
    clear()
    print_banner(color)
    print(f"{lc} {Fore.YELLOW}Telegram Bot Token Spreader{Fore.RESET}")
    print()
    bot_token = input(f"{Fore.RESET}[{color}>{Fore.RESET}] Enter bot token to spread: ")
    if not bot_token:
        print(f"{ld} {Fore.RED}Bot token cannot be empty!{Fore.RESET}")
        time.sleep(2)
        return
    
    print(f"{ld} {Fore.GREEN}Telegram Bot Token Spreader functionality will be implemented here{Fore.RESET}")
    print(f"{ld} Bot Token: {Fore.CYAN}{bot_token[:20]}...{Fore.RESET}")
    input(f"{Fore.RESET}[{color}>{Fore.RESET}] Press Enter to continue...")

def telegram_spread_sticker():
    color = Helper.color
    clear()
    print_banner(color)
    print(f"{lc} {Fore.YELLOW}Telegram Sticker Spreader{Fore.RESET}")
    print()
    sticker_id = input(f"{Fore.RESET}[{color}>{Fore.RESET}] Enter sticker ID/file to spread: ")
    if not sticker_id:
        print(f"{ld} {Fore.RED}Sticker ID cannot be empty!{Fore.RESET}")
        time.sleep(2)
        return
    
    print(f"{ld} {Fore.GREEN}Telegram Sticker Spreader functionality will be implemented here{Fore.RESET}")
    print(f"{ld} Sticker: {Fore.CYAN}{sticker_id}{Fore.RESET}")
    input(f"{Fore.RESET}[{color}>{Fore.RESET}] Press Enter to continue...")

def telegram_spread_media():
    color = Helper.color
    clear()
    print_banner(color)
    print(f"{lc} {Fore.YELLOW}Telegram Media Spreader{Fore.RESET}")
    print()
    media_path = input(f"{Fore.RESET}[{color}>{Fore.RESET}] Enter media file path to spread: ")
    if not os.path.exists(media_path):
        print(f"{ld} {Fore.RED}Media file not found!{Fore.RESET}")
        time.sleep(2)
        return
    
    print(f"{ld} {Fore.GREEN}Telegram Media Spreader functionality will be implemented here{Fore.RESET}")
    print(f"{ld} Media: {Fore.CYAN}{media_path}{Fore.RESET}")
    input(f"{Fore.RESET}[{color}>{Fore.RESET}] Press Enter to continue...")

def telegram_spread_file():
    color = Helper.color
    clear()
    print_banner(color)
    print(f"{lc} {Fore.YELLOW}Telegram File Spreader{Fore.RESET}")
    print()
    file_path = input(f"{Fore.RESET}[{color}>{Fore.RESET}] Enter file path to spread: ")
    if not os.path.exists(file_path):
        print(f"{ld} {Fore.RED}File not found!{Fore.RESET}")
        time.sleep(2)
        return
    
    print(f"{ld} {Fore.GREEN}Telegram File Spreader functionality will be implemented here{Fore.RESET}")
    print(f"{ld} File: {Fore.CYAN}{file_path}{Fore.RESET}")
    input(f"{Fore.RESET}[{color}>{Fore.RESET}] Press Enter to continue...")

def telegram_auto_forward():
    color = Helper.color
    new_title("Telegram Auto Forward")
    clear()
    print_banner(color)
    print(f"{lc} {Fore.YELLOW}Telegram Auto Forward{Fore.RESET}")
    print(f"{ld} {Fore.CYAN}Automatically forward messages from one chat to multiple destinations{Fore.RESET}")
    print()
    
    # Authenticate
    client = telegram_auth()
    if not client:
        return
    
    try:
        source_chat_id = input(f"{Fore.RESET}[{color}>{Fore.RESET}] Source Group/Channel ID (numeric ID only): ")
        if not source_chat_id:
            print(f"{ld} {Fore.RED}Source chat ID cannot be empty!{Fore.RESET}")
            client.disconnect()
            time.sleep(2)
            return
        
        # Validate it's numeric
        try:
            int(source_chat_id)
        except ValueError:
            print(f"{ld} {Fore.RED}Source chat ID must be numeric!{Fore.RESET}")
            print(f"{ld} {Fore.YELLOW}Tip: Use @userinfobot in Telegram to get chat IDs{Fore.RESET}")
            client.disconnect()
            time.sleep(2)
            return
        
        # Destination options
        print(f"\n{ld} {Fore.CYAN}Destination Options:{Fore.RESET}")
        print(f"{ld} {Fore.RESET}1. Forward to all groups/channels")
        print(f"{ld} {Fore.RESET}2. Load from Input/group_id.txt")
        print(f"{ld} {Fore.RESET}3. Enter IDs manually")
        
        dest_choice = input(f"{Fore.RESET}[{color}>{Fore.RESET}] Choice (1-3): ")
        
        destination_chat_ids = []
        forward_to_all = False
        
        if dest_choice == "1":
            forward_to_all = True
            print(f"{ld} {Fore.GREEN}Will forward to all groups/channels{Fore.RESET}")
        elif dest_choice == "2":
            # Load from file
            if os.path.exists("Input/group_id.txt"):
                with open("Input/group_id.txt", "r", encoding="utf-8") as f:
                    lines = f.readlines()
                    for line in lines:
                        line = line.strip()
                        if line and line.isdigit():
                            destination_chat_ids.append(line)
                    if destination_chat_ids:
                        print(f"{ld} {Fore.GREEN}Loaded {len(destination_chat_ids)} ID(s) from file{Fore.RESET}")
                    else:
                        print(f"{ld} {Fore.YELLOW}No valid IDs found in file!{Fore.RESET}")
                        client.disconnect()
                        time.sleep(2)
                        return
            else:
                print(f"{ld} {Fore.RED}File Input/group_id.txt not found!{Fore.RESET}")
                client.disconnect()
                time.sleep(2)
                return
        elif dest_choice == "3":
            # Enter manually
            print(f"{ld} {Fore.CYAN}Enter destination IDs (one per line, press Enter twice to finish):{Fore.RESET}")
            while True:
                dest_id = input(f"{Fore.RESET}[{color}>{Fore.RESET}] ID (or press Enter to finish): ")
                if not dest_id:
                    break
                if dest_id.isdigit():
                    destination_chat_ids.append(dest_id)
                    print(f"{ld} {Fore.GREEN}Added ID: {dest_id}{Fore.RESET}")
                else:
                    print(f"{ld} {Fore.RED}Invalid ID (must be numeric)!{Fore.RESET}")
            
            if not destination_chat_ids:
                print(f"{ld} {Fore.RED}No valid IDs entered!{Fore.RESET}")
                client.disconnect()
                time.sleep(2)
                return
        else:
            print(f"{ld} {Fore.RED}Invalid choice!{Fore.RESET}")
            client.disconnect()
            time.sleep(2)
            return
        
        # Custom message option
        print(f"\n{ld} {Fore.CYAN}Custom Message Options:{Fore.RESET}")
        print(f"{ld} {Fore.RESET}1. Load from Input/telegram_messages.txt")
        print(f"{ld} {Fore.RESET}2. Enter message directly")
        print(f"{ld} {Fore.RESET}3. No custom message (just forward)")
        
        message_choice = input(f"{Fore.RESET}[{color}>{Fore.RESET}] Choice (1-3): ")
        
        custom_message = None
        if message_choice == "1":
            # Load from file
            if os.path.exists("Input/telegram_messages.txt"):
                with open("Input/telegram_messages.txt", "r", encoding="utf-8") as f:
                    lines = f.readlines()
                    if lines:
                        custom_message = "".join(lines).strip()
                        print(f"{ld} {Fore.GREEN}Loaded message from file{Fore.RESET}")
                        print(f"{ld} {Fore.CYAN}Preview: {custom_message[:50]}...{Fore.RESET}")
                    else:
                        print(f"{ld} {Fore.YELLOW}File is empty, no custom message will be sent{Fore.RESET}")
            else:
                print(f"{ld} {Fore.YELLOW}File not found, no custom message will be sent{Fore.RESET}")
        elif message_choice == "2":
            # Enter directly
            custom_message = input(f"{Fore.RESET}[{color}>{Fore.RESET}] Enter custom message: ")
            if not custom_message:
                print(f"{ld} {Fore.YELLOW}No message entered, no custom message will be sent{Fore.RESET}")
                custom_message = None
        else:
            print(f"{ld} {Fore.CYAN}No custom message will be sent{Fore.RESET}")
        
        print(f"\n{ld} {Fore.GREEN}Starting auto-forward...{Fore.RESET}")
        print(f"{ld} {Fore.CYAN}Source ID: {source_chat_id}{Fore.RESET}")
        if forward_to_all:
            print(f"{ld} {Fore.CYAN}Destinations: All groups/channels{Fore.RESET}")
        else:
            print(f"{ld} {Fore.CYAN}Destinations: {len(destination_chat_ids)} ID(s){Fore.RESET}")
        if custom_message:
            print(f"{ld} {Fore.CYAN}Custom message: {custom_message[:50]}...{Fore.RESET}")
        print(f"{ld} {Fore.YELLOW}Press Ctrl+C to stop{Fore.RESET}")
        
        asyncio.run(auto_forward_messages(client, source_chat_id, destination_chat_ids, custom_message, forward_to_all))
    except KeyboardInterrupt:
        print(f"\n{ld} {Fore.YELLOW}Stopped auto-forward{Fore.RESET}")
    except Exception as e:
        print(f"{ld} {Fore.RED}Error: {e}{Fore.RESET}")
        log_error(f"Auto-forward error: {str(e)}", "ERROR", "telegram_auto_forward")
    finally:
        try:
            client.disconnect()
        except:
            pass
        input(f"{Fore.RESET}[{color}>{Fore.RESET}] Press Enter to continue...")

def telegram_account_nuker():
    color = Helper.color
    new_title("Telegram Account Nuker")
    clear()
    print_banner(color)
    print(f"{lc} {Fore.YELLOW}Telegram Account Nuker{Fore.RESET}")
    print(f"{ld} {Fore.RED}WARNING: This will delete all messages and leave all groups!{Fore.RESET}")
    print()
    
    confirm = input(f"{Fore.RESET}[{color}>{Fore.RESET}] Are you sure? Type 'YES' to continue: ")
    if confirm != 'YES':
        print(f"{ld} {Fore.YELLOW}Cancelled{Fore.RESET}")
        time.sleep(2)
        return
    
    # Authenticate
    client = telegram_auth()
    if not client:
        return
    
    try:
        print(f"\n{ld} {Fore.RED}Starting account nuke...{Fore.RESET}")
        asyncio.run(nuke_telegram_account(client))
    except Exception as e:
        print(f"{ld} {Fore.RED}Error: {e}{Fore.RESET}")
        log_error(f"Account nuker error: {str(e)}", "ERROR", "telegram_account_nuker")
    finally:
        try:
            client.disconnect()
        except:
            pass
        input(f"{Fore.RESET}[{color}>{Fore.RESET}] Press Enter to continue...")

