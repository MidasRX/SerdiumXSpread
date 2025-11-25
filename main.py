from Helper import *
from Helper.Common.utils import *
import Helper

clear()

# Use color from Helper module
color = Helper.color

def change_theme():
    global color
    import Helper
    clear()
    print_banner(color)
    print(f"""
{color}<<{Fore.RESET}1{color}>>  [{Fore.RESET}Light Cyan (Standard){color}]
{color}<<{Fore.RESET}2{color}>>  [{Fore.RESET}Light Blue{color}]
{color}<<{Fore.RESET}3{color}>>  [{Fore.RESET}Light Red{color}]
{color}<<{Fore.RESET}4{color}>>  [{Fore.RESET}Light Green{color}]
{color}<<{Fore.RESET}5{color}>>  [{Fore.RESET}Light Magenta{color}]
{color}<<{Fore.RESET}6{color}>>  [{Fore.RESET}Light Yellow{color}]
{color}<<{Fore.RESET}7{color}>>  [{Fore.RESET}Cyan{color}]
{color}<<{Fore.RESET}8{color}>>  [{Fore.RESET}Blue{color}] 
{color}<<{Fore.RESET}9{color}>>  [{Fore.RESET}Red{color}]
{color}<<{Fore.RESET}10{color}>> [{Fore.RESET}Green{color}]
{color}<<{Fore.RESET}11{color}>> [{Fore.RESET}Magenta{color}]
{color}<<{Fore.RESET}12{color}>> [{Fore.RESET}Yellow{color}]
    """)
    choice = input(f"{Fore.RESET}[{color}>{Fore.RESET}] Choice: ")
    colors = {
        "1": Fore.LIGHTCYAN_EX,
        "2": Fore.LIGHTBLUE_EX,
        "3": Fore.LIGHTRED_EX,
        "4": Fore.LIGHTGREEN_EX,
        "5": Fore.LIGHTMAGENTA_EX,
        "6": Fore.LIGHTYELLOW_EX,
        "7": Fore.CYAN,
        "8": Fore.BLUE,
        "9": Fore.RED,
        "10": Fore.GREEN,
        "11": Fore.MAGENTA,
        "12": Fore.YELLOW
    }
    selected_color = colors.get(choice)
    if selected_color:
        color = selected_color
        Helper.color = selected_color  # Update global color in Helper module
    else:
        print("Invalid choice")
        time.sleep(1)

def main():
    global color
    color = Helper.color  # Sync color from Helper module
    new_title("SerdiumXSpread │ Main Menu")
    clear()
    print_banner(color)
    print(f"""
                    {color}<<{Fore.RESET}1{color}>>  [{Fore.RESET}Discord Spreader{color}]            {color}<<{Fore.RESET}5{color}>>  [{Fore.RESET}Proxy Scraper{color}]
                    {color}<<{Fore.RESET}2{color}>>  [{Fore.RESET}Telegram Spreader{color}]          {color}<<{Fore.RESET}6{color}>>  [{Fore.RESET}Token Checker{color}]
                    {color}<<{Fore.RESET}3{color}>>  [{Fore.RESET}Proxy Checker{color}]              {color}<<{Fore.RESET}7{color}>>  [{Fore.RESET}Email Spammer{color}]
                    {color}<<{Fore.RESET}4{color}>>  [{Fore.RESET}Clear Output{color}]                {color}<<{Fore.RESET}8{color}>>  [{Fore.RESET}Config Editor{color}]
                                                                        {color}<<{Fore.RESET}9{color}>>  [{Fore.RESET}Clear Input{color}]
                                                                        {color}<<{Fore.RESET}10{color}>> [{Fore.RESET}Change Theme{color}]
                                                                        {color}<<{Fore.RESET}11{color}>> [{Fore.RESET}About{color}]
    """)
    choice = input(f"{Fore.RESET}[{color}>{Fore.RESET}] Choice: ")
    functions = {
        "1": discord_menu,
        "2": telegram_menu,
        "3": proxy_checker,
        "4": clear_output,
        "5": proxy_scraper,
        "6": token_checker,
        "7": email_spammer,
        "8": config_editor,
        "9": clear_input,
        "10": change_theme,
        "11": about
    }
    function = functions.get(choice)
    if function:
        result = function()
        if result is None:  # If function returns None, go back to main menu
            main()
    else:
        print("Invalid choice")
        time.sleep(1)
        main()

StartupTool()
os.system("mode con cols=135 lines=24")
main()

