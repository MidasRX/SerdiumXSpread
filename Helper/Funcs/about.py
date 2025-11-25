from Helper import *
from Helper.Common.utils import *
import Helper

def about():
    color = Helper.color
    clear()
    print_banner(color)
    print(f"""
{lc} {Fore.YELLOW}About SerdiumXSpread{Fore.RESET}
{ld} Version: {Fore.GREEN}1.0.0{Fore.RESET}
{ld} Author: {Fore.GREEN}SerdiumX{Fore.RESET}
{ld} Description: {Fore.CYAN}A powerful spreading tool for various content types{Fore.RESET}
{ld} 
{ld} Features:
{ld}   • File Spreading
{ld}   • Token Spreading
{ld}   • Message Spreading
{ld}   • Link Spreading
{ld}   • Email Spreading
{ld}   • Webhook Spreading
{ld}   • Proxy Management
{ld}   • Token Checking
    """)
    input(f"{Fore.RESET}[{color}>{Fore.RESET}] Press Enter to continue...")

