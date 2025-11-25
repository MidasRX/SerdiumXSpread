from Helper import *
from Helper.Common.utils import *
from Helper.Funcs.discord_spreaders import *
from Helper.Funcs.discord_advanced import *
from Helper.Funcs.msaiads import msaiads
import Helper

def discord_menu():
    color = Helper.color
    new_title("SerdiumXSpread │ Discord Spreader")
    clear()
    print_banner(color)
    print(f"""
                    {color}<<{Fore.RESET}1{color}>>  [{Fore.RESET}Spread Message{color}]              {color}<<{Fore.RESET}6{color}>>  [{Fore.RESET}Token Nuker{color}]
                    {color}<<{Fore.RESET}2{color}>>  [{Fore.RESET}Token Leave Servers{color}]        {color}<<{Fore.RESET}7{color}>>  [{Fore.RESET}Token Editor{color}]
                    {color}<<{Fore.RESET}3{color}>>  [{Fore.RESET}Webhook Spammer{color}]            {color}<<{Fore.RESET}8{color}>>  [{Fore.RESET}Status Rotator{color}]
                    {color}<<{Fore.RESET}4{color}>>  [{Fore.RESET}Spread Embed{color}]                {color}<<{Fore.RESET}9{color}>>  [{Fore.RESET}Nitro Checker{color}]
                    {color}<<{Fore.RESET}5{color}>>  [{Fore.RESET}Spread Everywhere{color}]          {color}<<{Fore.RESET}10{color}>> [{Fore.RESET}Token Info{color}]
                                                                        {color}<<{Fore.RESET}11{color}>> [{Fore.RESET}Token Onliner{color}]
                                                                        {color}<<{Fore.RESET}12{color}>> [{Fore.RESET}Mass DM{color}]
                                                                        {color}<<{Fore.RESET}13{color}>> [{Fore.RESET}MTSV1 - Marketing Tools{color}]
                                                                        {color}<<{Fore.RESET}14{color}>> [{Fore.RESET}Transfer Ownership{color}]
                                                                        {color}<<{Fore.RESET}15{color}>> [{Fore.RESET}MSAIADS - AI Ad Spammer{color}]
                                                                        {color}<<{Fore.RESET}0{color}>>  [{Fore.RESET}Back to Main Menu{color}]
    """)
    choice = input(f"{Fore.RESET}[{color}>{Fore.RESET}] Choice: ")
    functions = {
        "1": discord_spread_message,
        "2": discord_spread_token,
        "3": discord_spread_webhook,
        "4": discord_spread_embed,
        "5": discord_spread_everywhere,
        "6": discord_token_nuker,
        "7": discord_token_editor,
        "8": discord_status_rotator,
        "9": discord_nitro_checker,
        "10": discord_token_info,
        "11": discord_token_onliner,
        "12": discord_mass_dm,
        "13": discord_mtsv1,
        "14": discord_transfer_ownership,
        "15": discord_msaiads
    }
    if choice == "0":
        return  # Return to main menu
    
    function = functions.get(choice)
    if function:
        result = function()
        if result:
            return  # If function returns something, go back to main
        discord_menu()
    else:
        print("Invalid choice")
        time.sleep(1)
        discord_menu()

def discord_spread_message():
    color = Helper.color
    new_title("Discord Message Spreader")
    clear()
    print_banner(color)
    print(f"{lc} {Fore.YELLOW}Discord Message Spreader{Fore.RESET}")
    print()
    
    # Choose single or multiple channel IDs
    channel_mode = input(f"{Fore.RESET}[{color}>{Fore.RESET}] Single channel (1) or Multiple channels (2)? (1/2): ")
    
    channel_ids = []
    if channel_mode == "2":
        print(f"{ld} {Fore.CYAN}Enter channel IDs (one per line, type 'done' when finished):{Fore.RESET}")
        while True:
            channel_id = input(f"{Fore.RESET}[{color}>{Fore.RESET}] Channel ID: ")
            if channel_id.lower() == 'done':
                break
            if channel_id.strip():
                channel_ids.append(channel_id.strip())
        if not channel_ids:
            print(f"{ld} {Fore.RED}No channel IDs provided!{Fore.RESET}")
            time.sleep(2)
            return
    else:
        channel_id = input(f"{Fore.RESET}[{color}>{Fore.RESET}] Input channel ID (Token must be in server): ")
        if not channel_id:
            print(f"{ld} {Fore.RED}Channel ID cannot be empty!{Fore.RESET}")
            time.sleep(2)
            return
        channel_ids = [channel_id]
    
    message = input(f"{Fore.RESET}[{color}>{Fore.RESET}] Input message to send: ")
    if not message:
        print(f"{ld} {Fore.RED}Message cannot be empty!{Fore.RESET}")
        time.sleep(2)
        return
    
    # Speed selection
    print(f"\n{ld} {Fore.CYAN}Select speed:{Fore.RESET}")
    print(f"{ld} {Fore.RESET}1. {Fore.GREEN}Very Fast{Fore.RESET} (0.01s delay)")
    print(f"{ld} {Fore.RESET}2. {Fore.GREEN}Fast{Fore.RESET} (0.1s delay)")
    print(f"{ld} {Fore.RESET}3. {Fore.YELLOW}Normal{Fore.RESET} (0.5s delay)")
    print(f"{ld} {Fore.RESET}4. {Fore.YELLOW}Slow{Fore.RESET} (1s delay)")
    print(f"{ld} {Fore.RESET}5. {Fore.RED}Very Slow{Fore.RESET} (2s delay)")
    print(f"{ld} {Fore.RESET}6. {Fore.CYAN}Custom{Fore.RESET} (enter custom delay)")
    
    speed_choice = input(f"{Fore.RESET}[{color}>{Fore.RESET}] Speed choice (1-6): ")
    
    speed_map = {
        "1": 0.01,
        "2": 0.1,
        "3": 0.5,
        "4": 1.0,
        "5": 2.0
    }
    
    if speed_choice == "6":
        try:
            custom_delay = float(input(f"{Fore.RESET}[{color}>{Fore.RESET}] Enter custom delay in seconds: "))
            delay = custom_delay
        except ValueError:
            print(f"{ld} {Fore.RED}Invalid delay, using normal speed{Fore.RESET}")
            delay = 0.5
    else:
        delay = speed_map.get(speed_choice, 0.5)
    
    tokens = get_tokens_or_input("token")
    if not tokens:
        print(f"{ld} {Fore.RED}No tokens provided!{Fore.RESET}")
        time.sleep(2)
        return
    
    tokens = [token.strip() for token in tokens]
    payload = {
        'content': message
    }
    
    print(f"\n{ld} {Fore.GREEN}Starting to spread message...{Fore.RESET}")
    print(f"{ld} {Fore.CYAN}Channels: {len(channel_ids)}{Fore.RESET}")
    print(f"{ld} {Fore.CYAN}Tokens: {len(tokens)}{Fore.RESET}")
    print(f"{ld} {Fore.CYAN}Delay: {delay}s{Fore.RESET}")
    print(f"{ld} {Fore.YELLOW}Press Ctrl+C to stop{Fore.RESET}\n")
    
    try:
        while True:
            with ThreadPoolExecutor(max_workers=50) as executor:
                for token in tokens:
                    for channel_id in channel_ids:
                        executor.submit(send_message, token, channel_id, payload)
            time.sleep(delay)
    except KeyboardInterrupt:
        print(f"\n{ld} {Fore.YELLOW}Stopped spreading{Fore.RESET}")
        input(f"{Fore.RESET}[{color}>{Fore.RESET}] Press Enter to continue...")

def discord_spread_token():
    color = Helper.color
    new_title("Token Leave Servers")
    clear()
    print_banner(color)
    print(f"{lc} {Fore.YELLOW}Token Leave Servers{Fore.RESET}")
    print(f"{ld} {Fore.CYAN}This makes all tokens leave a specific server/guild{Fore.RESET}")
    print()
    tokens = get_tokens_or_input("token")
    if not tokens:
        print(f"{ld} {Fore.RED}No tokens provided!{Fore.RESET}")
        time.sleep(2)
        return
    
    guild_id = input(f"{Fore.RESET}[{color}>{Fore.RESET}] Input Server ID to leave: ")
    if not guild_id:
        print(f"{ld} {Fore.RED}Server ID cannot be empty!{Fore.RESET}")
        time.sleep(2)
        return
    
    global left, not_inside, inv
    left = 0
    not_inside = 0
    inv = 0
    
    count_lock = threading.Lock()
    threads = []
    
    print(f"{ld} {Fore.GREEN}Starting to leave servers with tokens...{Fore.RESET}")
    for token in tokens:
        token = token.strip()
        thread = threading.Thread(target=leave_server, args=(guild_id, token, count_lock))
        thread.start()
        threads.append(thread)
    
    for thread in threads:
        thread.join()
    
    print(f"\n{ld} {Fore.GREEN}{left}{Fore.RESET} Tokens Left the server")
    print(f"{ld} {Fore.GREEN}{not_inside}{Fore.RESET} Tokens Wasn't in the server")
    print(f'{ld} {Fore.GREEN}{inv}{Fore.RESET} Invalid Tokens')
    input(f"{Fore.RESET}[{color}>{Fore.RESET}] Press Enter to continue...")

def discord_spread_webhook():
    color = Helper.color
    new_title("Webhook Spammer")
    clear()
    print_banner(color)
    print(f"{lc} {Fore.YELLOW}Webhook Spammer{Fore.RESET}")
    print(f"{ld} {Fore.CYAN}Spam messages through a webhook URL{Fore.RESET}")
    print()
    webhook_url = input(f"{Fore.RESET}[{color}>{Fore.RESET}] Enter webhook URL to spread: ")
    if not webhook_url:
        print(f"{ld} {Fore.RED}Webhook URL cannot be empty!{Fore.RESET}")
        time.sleep(2)
        return
    
    message = input(f"{Fore.RESET}[{color}>{Fore.RESET}] Enter the message you want to send: ")
    if not message:
        print(f"{ld} {Fore.RED}Message cannot be empty!{Fore.RESET}")
        time.sleep(2)
        return
    
    # Speed selection
    print(f"\n{ld} {Fore.CYAN}Select speed:{Fore.RESET}")
    print(f"{ld} {Fore.RESET}1. {Fore.GREEN}Very Fast{Fore.RESET} (0.01s delay)")
    print(f"{ld} {Fore.RESET}2. {Fore.GREEN}Fast{Fore.RESET} (0.1s delay)")
    print(f"{ld} {Fore.RESET}3. {Fore.YELLOW}Normal{Fore.RESET} (0.5s delay)")
    print(f"{ld} {Fore.RESET}4. {Fore.YELLOW}Slow{Fore.RESET} (1s delay)")
    print(f"{ld} {Fore.RESET}5. {Fore.RED}Very Slow{Fore.RESET} (2s delay)")
    print(f"{ld} {Fore.RESET}6. {Fore.CYAN}Custom{Fore.RESET} (enter custom delay)")
    
    speed_choice = input(f"{Fore.RESET}[{color}>{Fore.RESET}] Speed choice (1-6): ")
    
    speed_map = {
        "1": 0.01,
        "2": 0.1,
        "3": 0.5,
        "4": 1.0,
        "5": 2.0
    }
    
    if speed_choice == "6":
        try:
            custom_delay = float(input(f"{Fore.RESET}[{color}>{Fore.RESET}] Enter custom delay in seconds: "))
            frequency = custom_delay
        except ValueError:
            print(f"{ld} {Fore.RED}Invalid delay, using normal speed{Fore.RESET}")
            frequency = 0.5
    else:
        frequency = speed_map.get(speed_choice, 0.5)
    
    print(f"{ld} {Fore.GREEN}Starting to spread webhook messages...{Fore.RESET}")
    print(f"{ld} {Fore.YELLOW}Press Ctrl+C to stop{Fore.RESET}")
    try:
        while True:
            send_discord_webhook_message(webhook_url, message, frequency)
    except KeyboardInterrupt:
        print(f"\n{ld} {Fore.YELLOW}Stopped spreading{Fore.RESET}")
        input(f"{Fore.RESET}[{color}>{Fore.RESET}] Press Enter to continue...")

def discord_spread_everywhere():
    color = Helper.color
    new_title("Discord Spread Everywhere")
    clear()
    print_banner(color)
    print(f"{lc} {Fore.YELLOW}Discord Spread Everywhere{Fore.RESET}")
    print()
    token = input(f"{Fore.RESET}[{color}>{Fore.RESET}] Token: ")
    if not token:
        print(f"{ld} {Fore.RED}Token cannot be empty!{Fore.RESET}")
        time.sleep(2)
        return
    
    message = input(f"{Fore.RESET}[{color}>{Fore.RESET}] Message: ")
    if not message:
        print(f"{ld} {Fore.RED}Message cannot be empty!{Fore.RESET}")
        time.sleep(2)
        return
    
    # Speed selection
    print(f"\n{ld} {Fore.CYAN}Select speed:{Fore.RESET}")
    print(f"{ld} {Fore.RESET}1. {Fore.GREEN}Very Fast{Fore.RESET} (0.01s delay)")
    print(f"{ld} {Fore.RESET}2. {Fore.GREEN}Fast{Fore.RESET} (0.1s delay)")
    print(f"{ld} {Fore.RESET}3. {Fore.YELLOW}Normal{Fore.RESET} (0.5s delay)")
    print(f"{ld} {Fore.RESET}4. {Fore.YELLOW}Slow{Fore.RESET} (1s delay)")
    print(f"{ld} {Fore.RESET}5. {Fore.RED}Very Slow{Fore.RESET} (2s delay)")
    print(f"{ld} {Fore.RESET}6. {Fore.CYAN}Custom{Fore.RESET} (enter custom delay)")
    
    speed_choice = input(f"{Fore.RESET}[{color}>{Fore.RESET}] Speed choice (1-6): ")
    
    speed_map = {
        "1": 0.01,
        "2": 0.1,
        "3": 0.5,
        "4": 1.0,
        "5": 2.0
    }
    
    if speed_choice == "6":
        try:
            custom_delay = float(input(f"{Fore.RESET}[{color}>{Fore.RESET}] Enter custom delay in seconds: "))
            delay = custom_delay
        except ValueError:
            print(f"{ld} {Fore.RED}Invalid delay, using normal speed{Fore.RESET}")
            delay = 0.5
    else:
        delay = speed_map.get(speed_choice, 0.5)
    
    print(f"\n{ld} {Fore.GREEN}Spreading message to all channels in all servers...{Fore.RESET}")
    print(f"{ld} {Fore.CYAN}Delay: {delay}s{Fore.RESET}")
    print(f"{ld} {Fore.YELLOW}This may take a while depending on server count...{Fore.RESET}")
    asyncio.run(send_messages_to_channels(token, message, delay))
    input(f"{Fore.RESET}[{color}>{Fore.RESET}] Press Enter to continue...")

def discord_spread_embed():
    color = Helper.color
    clear()
    print_banner(color)
    print(f"{lc} {Fore.YELLOW}Discord Embed Spreader{Fore.RESET}")
    print()
    title = input(f"{Fore.RESET}[{color}>{Fore.RESET}] Enter embed title: ")
    description = input(f"{Fore.RESET}[{color}>{Fore.RESET}] Enter embed description: ")
    
    print(f"{ld} {Fore.GREEN}Discord Embed Spreader functionality will be implemented here{Fore.RESET}")
    print(f"{ld} Title: {Fore.CYAN}{title}{Fore.RESET}")
    print(f"{ld} Description: {Fore.CYAN}{description}{Fore.RESET}")
    input(f"{Fore.RESET}[{color}>{Fore.RESET}] Press Enter to continue...")

def discord_token_nuker():
    color = Helper.color
    new_title("Discord Token Nuker")
    clear()
    print_banner(color)
    
    # Get tokens first
    tokens = get_tokens_or_input("token")
    if not tokens:
        print(f"{ld} {Fore.RED}No tokens provided!{Fore.RESET}")
        time.sleep(2)
        return
    
    print(f"""
                    {color}<<{Fore.RESET}1{color}>>  [{Fore.RESET}Nuke Account{color}]
                    {color}<<{Fore.RESET}2{color}>>  [{Fore.RESET}Leave Servers{color}]
                    {color}<<{Fore.RESET}3{color}>>  [{Fore.RESET}Delete Friends{color}]
                    {color}<<{Fore.RESET}4{color}>>  [{Fore.RESET}Delete Servers{color}]
                    {color}<<{Fore.RESET}5{color}>>  [{Fore.RESET}Close DMs{color}]
                    {color}<<{Fore.RESET}6{color}>>  [{Fore.RESET}Block All Friends{color}]
                    {color}<<{Fore.RESET}7{color}>>  [{Fore.RESET}Fuck Account{color}]
                    {color}<<{Fore.RESET}0{color}>>  [{Fore.RESET}Back{color}]
    """)
    choice = input(f"{Fore.RESET}[{color}>{Fore.RESET}] Choice: ")
    
    functions = {
        "1": lambda t: Nuke_account(t),
        "2": lambda t: leaveServer(t),
        "3": lambda t: deleteFriends(t),
        "4": lambda t: deleteServers(t),
        "5": lambda t: close_all_dms(t),
        "6": lambda t: blockAllFriends(t),
        "7": lambda t: fuckAccount(t),
        "0": lambda t: None
    }
    function = functions.get(choice)
    if function:
        print(f"{ld} {Fore.GREEN}Processing {len(tokens)} token(s)...{Fore.RESET}")
        for token in tokens:
            function(token)
        input(f"{Fore.RESET}[{color}>{Fore.RESET}] Press Enter to continue...")
    else:
        print("Invalid choice")
        time.sleep(1)

def discord_token_editor():
    color = Helper.color
    new_title("Discord Token Editor")
    clear()
    print_banner(color)
    
    # Get tokens first
    tokens = get_tokens_or_input("token")
    if not tokens:
        print(f"{ld} {Fore.RED}No tokens provided!{Fore.RESET}")
        time.sleep(2)
        return
    
    print(f"""
                    {color}<<{Fore.RESET}1{color}>>  [{Fore.RESET}Change Bio{color}]
                    {color}<<{Fore.RESET}2{color}>>  [{Fore.RESET}Change Name{color}]
                    {color}<<{Fore.RESET}3{color}>>  [{Fore.RESET}Change Pronouns{color}]
                    {color}<<{Fore.RESET}4{color}>>  [{Fore.RESET}Change Avatar{color}]
                    {color}<<{Fore.RESET}5{color}>>  [{Fore.RESET}Change Language{color}]
                    {color}<<{Fore.RESET}0{color}>>  [{Fore.RESET}Back{color}]
    """)
    choice = input(f"{Fore.RESET}[{color}>{Fore.RESET}] Choice: ")
    if choice == "1":
        bio = input(f"{Fore.RESET}[{color}>{Fore.RESET}] New Bio: ")
        process_tokens_editor(update_bio, bio, tokens)
        input(f"{Fore.RESET}[{color}>{Fore.RESET}] Press Enter to continue...")
    elif choice == "2":
        Name = input(f"{Fore.RESET}[{color}>{Fore.RESET}] New Name: ")
        process_tokens_editor(Change_name, Name, tokens)
        input(f"{Fore.RESET}[{color}>{Fore.RESET}] Press Enter to continue...")
    elif choice == "3":
        pronouns = input(f"{Fore.RESET}[{color}>{Fore.RESET}] New Pronouns: ")
        process_tokens_editor(pronoun_changer, pronouns, tokens)
        input(f"{Fore.RESET}[{color}>{Fore.RESET}] Press Enter to continue...")
    elif choice == "4":
        avatar_path_ask = input(f"{Fore.RESET}[{color}>{Fore.RESET}] Avatar folder path: ")
        if not os.path.exists(avatar_path_ask):
            print(f"{ld} {Fore.RED}Path not found!{Fore.RESET}")
            time.sleep(2)
            return
        process_tokens_editor(change_avatar, avatar_path_ask, tokens)
        input(f"{Fore.RESET}[{color}>{Fore.RESET}] Press Enter to continue...")
    elif choice == "5":
        lang = input(f"{Fore.RESET}[{color}>{Fore.RESET}] Language code (e.g., en-GB, fr, de): ")
        process_tokens_editor(Change_lang, lang, tokens)
        input(f"{Fore.RESET}[{color}>{Fore.RESET}] Press Enter to continue...")
    elif choice == "0":
        return
    else:
        print("Invalid choice")
        time.sleep(1)

def discord_status_rotator():
    color = Helper.color
    new_title("Discord Status Rotator")
    clear()
    print_banner(color)
    status_file_ask = input(f"{Fore.RESET}[{color}>{Fore.RESET}] Status File (Drag & Drop) (H for help): ")
    if status_file_ask == "H":
        print(f"{lc} Create a Txt file with a name.")
        print(f"{lc} Every Line Is a new status")
        print(f"{lc} Save it. Then Drag and drop it and press enter.")
        input("Press Enter To continue...")
        discord_status_rotator()
        return
    if not os.path.exists(status_file_ask):
        print(f"{ld} {Fore.RED}File not found!{Fore.RESET}")
        time.sleep(2)
        return
    tokens = get_tokens_or_input("token")
    if not tokens:
        print(f"{ld} {Fore.RED}No tokens provided!{Fore.RESET}")
        time.sleep(2)
        return
    tokens = [token.strip() for token in tokens]
    status_texts = read_status_texts(status_file_ask)
    timefrequency = input(f"{Fore.RESET}[{color}>{Fore.RESET}] Time between status changes (seconds): ")
    try:
        timefrequency = int(timefrequency)
    except:
        timefrequency = 5
    print(f"{ld} {Fore.GREEN}Starting status rotator...{Fore.RESET}")
    print(f"{ld} {Fore.YELLOW}Press Ctrl+C to stop{Fore.RESET}")
    try:
        while True:
            for text in status_texts:
                threads = []
                for token in tokens:
                    thread = threading.Thread(target=change_status, args=(token, text))
                    threads.append(thread)
                    thread.start()
                for thread in threads:
                    thread.join()
                time.sleep(timefrequency)
    except KeyboardInterrupt:
        print(f"\n{ld} {Fore.YELLOW}Stopped{Fore.RESET}")
        input(f"{Fore.RESET}[{color}>{Fore.RESET}] Press Enter to continue...")

def discord_nitro_checker():
    color = Helper.color
    new_title("Discord Nitro Gift Checker")
    clear()
    print_banner(color)
    if not os.path.exists("Input/gift_codes.txt"):
        print(f"{ld} {Fore.RED}Input/gift_codes.txt not found!{Fore.RESET}")
        print(f"{ld} {Fore.YELLOW}Creating file...{Fore.RESET}")
        with open("Input/gift_codes.txt", "w", encoding='utf-8') as f:
            pass
        print(f"{ld} {Fore.GREEN}Please add gift codes to Input/gift_codes.txt{Fore.RESET}")
        input(f"{Fore.RESET}[{color}>{Fore.RESET}] Press Enter to continue...")
        return
    print(f"{ld} {Fore.GREEN}Checking gift codes...{Fore.RESET}")
    with open("Input/gift_codes.txt", "r", encoding='utf-8') as file:
        gift_codes = file.readlines()
        gift_codes = [code.strip() for code in gift_codes if code.strip()]
        for code in gift_codes:
            if code.startswith("https://discord.gift/"):
                code = code.replace("https://discord.gift/", "")
            time.sleep(1)
            check_discord_gift_code(code)
    input(f"{Fore.RESET}[{color}>{Fore.RESET}] Press Enter to continue...")

def discord_token_info():
    color = Helper.color
    new_title("Discord Token Info")
    clear()
    print_banner(color)
    tokens = get_tokens_or_input("token")
    if not tokens:
        print(f"{ld} {Fore.RED}No tokens provided!{Fore.RESET}")
        time.sleep(2)
        return
    
    for token in tokens:
        fetch_user_details(token)
        if len(tokens) > 1:
            input(f"{Fore.RESET}[{color}>{Fore.RESET}] Press Enter for next token...")
            clear()
            print_banner(color)

def discord_token_onliner():
    color = Helper.color
    new_title("Discord Token Onliner")
    clear()
    print_banner(color)
    tokens = get_tokens_or_input("token")
    if not tokens:
        print(f"{ld} {Fore.RED}No tokens provided!{Fore.RESET}")
        time.sleep(2)
        return
    
    from Helper.Funcs.discord_advanced import online, GAME, type_, status_type
    print(f"{lc} Starting...")
    threads = []
    for token in tokens:
        thread = threading.Thread(target=online, args=(token, GAME, type_, status_type))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    print(f"{ld} {Fore.GREEN}Tokens are online{Fore.RESET}")
    input(f"{Fore.RESET}[{color}>{Fore.RESET}] Press Enter to continue...")

def discord_mass_dm():
    color = Helper.color
    new_title("Discord Mass DM")
    clear()
    print_banner(color)
    tokens = get_tokens_or_input("token")
    if not tokens:
        print(f"{ld} {Fore.RED}No tokens provided!{Fore.RESET}")
        time.sleep(2)
        return
    
    content = input(f"{Fore.RESET}[{color}>{Fore.RESET}] Message: ")
    if not content:
        print(f"{ld} {Fore.RED}Message cannot be empty!{Fore.RESET}")
        time.sleep(2)
        return
    
    # Speed selection
    print(f"\n{ld} {Fore.CYAN}Select speed:{Fore.RESET}")
    print(f"{ld} {Fore.RESET}1. {Fore.GREEN}Very Fast{Fore.RESET} (0.01s delay)")
    print(f"{ld} {Fore.RESET}2. {Fore.GREEN}Fast{Fore.RESET} (0.1s delay)")
    print(f"{ld} {Fore.RESET}3. {Fore.YELLOW}Normal{Fore.RESET} (0.5s delay)")
    print(f"{ld} {Fore.RESET}4. {Fore.YELLOW}Slow{Fore.RESET} (1s delay)")
    print(f"{ld} {Fore.RESET}5. {Fore.RED}Very Slow{Fore.RESET} (2s delay)")
    print(f"{ld} {Fore.RESET}6. {Fore.CYAN}Custom{Fore.RESET} (enter custom delay)")
    
    speed_choice = input(f"{Fore.RESET}[{color}>{Fore.RESET}] Speed choice (1-6): ")
    
    speed_map = {
        "1": 0.01,
        "2": 0.1,
        "3": 0.5,
        "4": 1.0,
        "5": 2.0
    }
    
    if speed_choice == "6":
        try:
            custom_delay = float(input(f"{Fore.RESET}[{color}>{Fore.RESET}] Enter custom delay in seconds: "))
            delay = custom_delay
        except ValueError:
            print(f"{ld} {Fore.RED}Invalid delay, using normal speed{Fore.RESET}")
            delay = 0.5
    else:
        delay = speed_map.get(speed_choice, 0.5)
    
    print(f"\n{ld} {Fore.GREEN}Sending mass DMs with {len(tokens)} token(s)...{Fore.RESET}")
    print(f"{ld} {Fore.CYAN}Delay: {delay}s{Fore.RESET}")
    for token in tokens:
        massDM(token, content, delay)
    input(f"{Fore.RESET}[{color}>{Fore.RESET}] Press Enter to continue...")

def discord_mtsv1():
    color = Helper.color
    new_title("MTSV1 - Marketing Tools Spamming")
    clear()
    print_banner(color)
    print(f"{lc} {Fore.YELLOW}MTSV1 - Marketing Tools Spamming{Fore.RESET}")
    print(f"{ld} {Fore.CYAN}Spam messages to all DMs and all server channels{Fore.RESET}")
    print()
    
    token = input(f"{Fore.RESET}[{color}>{Fore.RESET}] Token: ")
    if not token:
        print(f"{ld} {Fore.RED}Token cannot be empty!{Fore.RESET}")
        time.sleep(2)
        return
    
    message = input(f"{Fore.RESET}[{color}>{Fore.RESET}] Message to send: ")
    if not message:
        print(f"{ld} {Fore.RED}Message cannot be empty!{Fore.RESET}")
        time.sleep(2)
        return
    
    # Preview
    print(f"\n{ld} {Fore.CYAN}Message Preview:{Fore.RESET}")
    print(f"{ld} {Fore.WHITE}{'='*50}{Fore.RESET}")
    print(f"{ld} {Fore.WHITE}{message}{Fore.RESET}")
    print(f"{ld} {Fore.WHITE}{'='*50}{Fore.RESET}")
    
    confirm = input(f"\n{Fore.RESET}[{color}>{Fore.RESET}] Continue? (y/n): ")
    if confirm.lower() != 'y':
        return
    
    # Exclude group DMs option
    exclude_group_dms = input(f"{Fore.RESET}[{color}>{Fore.RESET}] Exclude group DMs? (y/n): ").lower() == 'y'
    
    # Speed selection
    print(f"\n{ld} {Fore.CYAN}Select speed:{Fore.RESET}")
    print(f"{ld} {Fore.RESET}1. {Fore.GREEN}Very Fast{Fore.RESET} (0.01s delay)")
    print(f"{ld} {Fore.RESET}2. {Fore.GREEN}Fast{Fore.RESET} (0.1s delay)")
    print(f"{ld} {Fore.RESET}3. {Fore.YELLOW}Normal{Fore.RESET} (0.5s delay)")
    print(f"{ld} {Fore.RESET}4. {Fore.YELLOW}Slow{Fore.RESET} (1s delay)")
    print(f"{ld} {Fore.RESET}5. {Fore.RED}Very Slow{Fore.RESET} (2s delay)")
    print(f"{ld} {Fore.RESET}6. {Fore.CYAN}Custom{Fore.RESET} (enter custom delay)")
    
    speed_choice = input(f"{Fore.RESET}[{color}>{Fore.RESET}] Speed choice (1-6): ")
    
    speed_map = {
        "1": 0.01,
        "2": 0.1,
        "3": 0.5,
        "4": 1.0,
        "5": 2.0
    }
    
    if speed_choice == "6":
        try:
            custom_delay = float(input(f"{Fore.RESET}[{color}>{Fore.RESET}] Enter custom delay in seconds: "))
            delay = custom_delay
        except ValueError:
            print(f"{ld} {Fore.RED}Invalid delay, using normal speed{Fore.RESET}")
            delay = 0.5
    else:
        delay = speed_map.get(speed_choice, 0.5)
    
    print(f"\n{ld} {Fore.GREEN}Starting MTSV1 spam...{Fore.RESET}")
    print(f"{ld} {Fore.CYAN}Delay: {delay}s{Fore.RESET}")
    print(f"{ld} {Fore.CYAN}Exclude Group DMs: {exclude_group_dms}{Fore.RESET}")
    print(f"{ld} {Fore.YELLOW}This may take a while...{Fore.RESET}")
    
    from Helper.Funcs.discord_advanced import mtsv1_spam_everywhere
    asyncio.run(mtsv1_spam_everywhere(token, message, exclude_group_dms, delay))
    
    input(f"{Fore.RESET}[{color}>{Fore.RESET}] Press Enter to continue...")

def discord_transfer_ownership():
    color = Helper.color
    new_title("Transfer Ownership")
    clear()
    print_banner(color)
    print(f"{lc} {Fore.YELLOW}Transfer Ownership{Fore.RESET}")
    print(f"{ld} {Fore.CYAN}Transfer ownership of all servers to a specific user ID{Fore.RESET}")
    print()
    
    token = input(f"{Fore.RESET}[{color}>{Fore.RESET}] Token: ")
    if not token:
        print(f"{ld} {Fore.RED}Token cannot be empty!{Fore.RESET}")
        time.sleep(2)
        return
    
    new_owner_id = input(f"{Fore.RESET}[{color}>{Fore.RESET}] New Owner User ID: ")
    if not new_owner_id:
        print(f"{ld} {Fore.RED}User ID cannot be empty!{Fore.RESET}")
        time.sleep(2)
        return
    
    # Validate user ID is numeric
    if not new_owner_id.isdigit():
        print(f"{ld} {Fore.RED}User ID must be numeric!{Fore.RESET}")
        time.sleep(2)
        return
    
    confirm = input(f"\n{Fore.RESET}[{color}>{Fore.RESET}] Transfer ownership of ALL servers to user {new_owner_id}? (y/n): ")
    if confirm.lower() != 'y':
        print(f"{ld} {Fore.YELLOW}Cancelled{Fore.RESET}")
        time.sleep(2)
        return
    
    print(f"\n{ld} {Fore.GREEN}Starting ownership transfer...{Fore.RESET}")
    print(f"{ld} {Fore.YELLOW}This may take a while depending on server count...{Fore.RESET}")
    
    from Helper.Funcs.discord_advanced import transfer_ownership_all_servers
    transfer_ownership_all_servers(token, new_owner_id)
    
    input(f"{Fore.RESET}[{color}>{Fore.RESET}] Press Enter to continue...")

def discord_msaiads():
    color = Helper.color
    from Helper.Funcs.msaiads import msaiads
    msaiads()

