from Helper import *
from Helper.Common.utils import *
import Helper
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import re

# SMTP settings for different providers
SMTP_CONFIGS = {
    'gmail': {
        'smtp_server': 'smtp.gmail.com',
        'smtp_port': 587,
        'smtp_port_ssl': 465
    },
    'yahoo': {
        'smtp_server': 'smtp.mail.yahoo.com',
        'smtp_port': 587,
        'smtp_port_ssl': 465
    },
    'hotmail': {
        'smtp_server': 'smtp-mail.outlook.com',
        'smtp_port': 587,
        'smtp_port_ssl': 465
    },
    'outlook': {
        'smtp_server': 'smtp-mail.outlook.com',
        'smtp_port': 587,
        'smtp_port_ssl': 465
    },
    'proton': {
        'smtp_server': '127.0.0.1',
        'smtp_port': 1025,
        'smtp_port_ssl': 465
    }
}

def parse_email_file(filename):
    """Parse email file with SMTP= or MAILOGIN= format"""
    emails = []
    if not os.path.exists(filename):
        return emails
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                
                # Parse SMTP= format: SMTP=host:port:user:pass
                if line.startswith('SMTP='):
                    smtp_data = line[5:].strip()
                    parts = smtp_data.split(':')
                    if len(parts) >= 4:
                        emails.append({
                            'type': 'smtp',
                            'host': parts[0],
                            'port': int(parts[1]) if parts[1].isdigit() else 587,
                            'email': parts[2],
                            'password': parts[3]
                        })
                
                # Parse MAILOGIN= format: MAILOGIN=provider:email:password
                elif line.startswith('MAILOGIN='):
                    login_data = line[9:].strip()
                    parts = login_data.split(':')
                    if len(parts) >= 3:
                        provider = parts[0].lower()
                        if provider in SMTP_CONFIGS:
                            emails.append({
                                'type': 'maillogin',
                                'provider': provider,
                                'email': parts[1],
                                'password': parts[2]
                            })
    except Exception as e:
        log_error(f"Error parsing email file: {str(e)}", "ERROR", "parse_email_file")
    
    return emails

def send_email_smtp(host, port, email, password, to_email, subject, message, use_ssl=False):
    """Send email using SMTP configuration"""
    color = Helper.color
    try:
        msg = MIMEMultipart()
        msg['From'] = email
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))
        
        if use_ssl:
            server = smtplib.SMTP_SSL(host, port)
        else:
            server = smtplib.SMTP(host, port)
            server.starttls()
        
        server.login(email, password)
        server.send_message(msg)
        server.quit()
        
        print(f"{lc} {Fore.GREEN}Email sent to {to_email} via SMTP{Fore.RESET}")
        return True
    except Exception as e:
        print(f"{lc} {Fore.RED}Failed to send to {to_email}: {str(e)}{Fore.RESET}")
        log_error(f"SMTP send failed to {to_email}: {str(e)}", "ERROR", "send_email_smtp")
        return False

def send_email_maillogin(provider, email, password, to_email, subject, message):
    """Send email using email/password login"""
    color = Helper.color
    
    if provider not in SMTP_CONFIGS:
        print(f"{lc} {Fore.RED}Unsupported provider: {provider}{Fore.RESET}")
        return False
    
    config = SMTP_CONFIGS[provider]
    
    try:
        msg = MIMEMultipart()
        msg['From'] = email
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))
        
        # Try TLS first (port 587)
        try:
            server = smtplib.SMTP(config['smtp_server'], config['smtp_port'])
            server.starttls()
            server.login(email, password)
            server.send_message(msg)
            server.quit()
            print(f"{lc} {Fore.GREEN}Email sent to {to_email} via {provider}{Fore.RESET}")
            return True
        except:
            # Try SSL (port 465)
            try:
                server = smtplib.SMTP_SSL(config['smtp_server'], config['smtp_port_ssl'])
                server.login(email, password)
                server.send_message(msg)
                server.quit()
                print(f"{lc} {Fore.GREEN}Email sent to {to_email} via {provider} (SSL){Fore.RESET}")
                return True
            except Exception as e:
                raise e
                
    except Exception as e:
        print(f"{lc} {Fore.RED}Failed to send to {to_email} via {provider}: {str(e)}{Fore.RESET}")
        log_error(f"Email send failed to {to_email} via {provider}: {str(e)}", "ERROR", "send_email_maillogin")
        return False

def email_spammer():
    color = Helper.color
    new_title("Email Spammer")
    clear()
    print_banner(color)
    print(f"{lc} {Fore.YELLOW}Email Spammer{Fore.RESET}")
    print(f"{ld} {Fore.CYAN}Spam emails using SMTP or email login{Fore.RESET}")
    print()
    
    # Get recipient emails
    print(f"{ld} {Fore.CYAN}Recipient Options:{Fore.RESET}")
    print(f"{ld} {Fore.RESET}1. Load from Input/emails.txt (one email per line)")
    print(f"{ld} {Fore.RESET}2. Enter email manually")
    
    recipient_choice = input(f"{Fore.RESET}[{color}>{Fore.RESET}] Choice (1-2): ")
    
    recipient_emails = []
    if recipient_choice == "1":
        if os.path.exists("Input/emails.txt"):
            with open("Input/emails.txt", "r", encoding="utf-8") as f:
                for line in f:
                    email = line.strip()
                    if email and '@' in email:
                        recipient_emails.append(email)
            if recipient_emails:
                print(f"{ld} {Fore.GREEN}Loaded {len(recipient_emails)} recipient(s) from file{Fore.RESET}")
            else:
                print(f"{ld} {Fore.RED}No valid emails found in file!{Fore.RESET}")
                time.sleep(2)
                return
        else:
            print(f"{ld} {Fore.RED}File Input/emails.txt not found!{Fore.RESET}")
            time.sleep(2)
            return
    else:
        email = input(f"{Fore.RESET}[{color}>{Fore.RESET}] Enter recipient email: ")
        if email and '@' in email:
            recipient_emails.append(email)
        else:
            print(f"{ld} {Fore.RED}Invalid email!{Fore.RESET}")
            time.sleep(2)
            return
    
    # Get sender configuration
    print(f"\n{ld} {Fore.CYAN}Sender Configuration:{Fore.RESET}")
    print(f"{ld} {Fore.RESET}1. Load from Input/email_accounts.txt (SMTP= or MAILOGIN= format)")
    print(f"{ld} {Fore.RESET}2. Enter manually")
    
    sender_choice = input(f"{Fore.RESET}[{color}>{Fore.RESET}] Choice (1-2): ")
    
    sender_accounts = []
    if sender_choice == "1":
        sender_accounts = parse_email_file("Input/email_accounts.txt")
        if sender_accounts:
            print(f"{ld} {Fore.GREEN}Loaded {len(sender_accounts)} account(s) from file{Fore.RESET}")
        else:
            print(f"{ld} {Fore.RED}No valid accounts found in file!{Fore.RESET}")
            time.sleep(2)
            return
    else:
        # Manual entry
        print(f"\n{ld} {Fore.CYAN}Account Type:{Fore.RESET}")
        print(f"{ld} {Fore.RESET}1. SMTP (host:port:email:password)")
        print(f"{ld} {Fore.RESET}2. Email Login (Gmail/Yahoo/Hotmail/Proton)")
        
        account_type = input(f"{Fore.RESET}[{color}>{Fore.RESET}] Choice (1-2): ")
        
        if account_type == "1":
            smtp_input = input(f"{Fore.RESET}[{color}>{Fore.RESET}] Enter SMTP (host:port:email:password): ")
            parts = smtp_input.split(':')
            if len(parts) >= 4:
                sender_accounts.append({
                    'type': 'smtp',
                    'host': parts[0],
                    'port': int(parts[1]) if parts[1].isdigit() else 587,
                    'email': parts[2],
                    'password': parts[3]
                })
            else:
                print(f"{ld} {Fore.RED}Invalid SMTP format!{Fore.RESET}")
                time.sleep(2)
                return
        else:
            print(f"\n{ld} {Fore.CYAN}Select Provider:{Fore.RESET}")
            print(f"{ld} {Fore.RESET}1. Gmail")
            print(f"{ld} {Fore.RESET}2. Yahoo")
            print(f"{ld} {Fore.RESET}3. Hotmail/Outlook")
            print(f"{ld} {Fore.RESET}4. Proton")
            
            provider_choice = input(f"{Fore.RESET}[{color}>{Fore.RESET}] Choice (1-4): ")
            providers = {'1': 'gmail', '2': 'yahoo', '3': 'hotmail', '4': 'proton'}
            provider = providers.get(provider_choice, 'gmail')
            
            email = input(f"{Fore.RESET}[{color}>{Fore.RESET}] Email: ")
            password = input(f"{Fore.RESET}[{color}>{Fore.RESET}] Password: ")
            
            sender_accounts.append({
                'type': 'maillogin',
                'provider': provider,
                'email': email,
                'password': password
            })
    
    # Get message details
    subject = input(f"\n{Fore.RESET}[{color}>{Fore.RESET}] Email Subject: ")
    if not subject:
        subject = "No Subject"
    
    print(f"\n{ld} {Fore.CYAN}Message Options:{Fore.RESET}")
    print(f"{ld} {Fore.RESET}1. Load from Input/messages.txt")
    print(f"{ld} {Fore.RESET}2. Enter message directly")
    
    message_choice = input(f"{Fore.RESET}[{color}>{Fore.RESET}] Choice (1-2): ")
    
    message = ""
    if message_choice == "1":
        if os.path.exists("Input/messages.txt"):
            with open("Input/messages.txt", "r", encoding="utf-8") as f:
                message = f.read().strip()
            if message:
                print(f"{ld} {Fore.GREEN}Loaded message from file{Fore.RESET}")
            else:
                print(f"{ld} {Fore.YELLOW}File is empty{Fore.RESET}")
                message = input(f"{Fore.RESET}[{color}>{Fore.RESET}] Enter message: ")
        else:
            message = input(f"{Fore.RESET}[{color}>{Fore.RESET}] Enter message: ")
    else:
        message = input(f"{Fore.RESET}[{color}>{Fore.RESET}] Enter message: ")
    
    if not message:
        print(f"{ld} {Fore.RED}Message cannot be empty!{Fore.RESET}")
        time.sleep(2)
        return
    
    # Speed control
    print(f"\n{ld} {Fore.CYAN}Select speed:{Fore.RESET}")
    print(f"{ld} {Fore.RESET}1. {Fore.GREEN}Very Fast{Fore.RESET} (0.1s delay)")
    print(f"{ld} {Fore.RESET}2. {Fore.GREEN}Fast{Fore.RESET} (0.5s delay)")
    print(f"{ld} {Fore.RESET}3. {Fore.YELLOW}Normal{Fore.RESET} (1s delay)")
    print(f"{ld} {Fore.RESET}4. {Fore.YELLOW}Slow{Fore.RESET} (2s delay)")
    print(f"{ld} {Fore.RESET}5. {Fore.RED}Very Slow{Fore.RESET} (5s delay)")
    print(f"{ld} {Fore.RESET}6. {Fore.CYAN}Custom{Fore.RESET} (enter custom delay)")
    
    speed_choice = input(f"{Fore.RESET}[{color}>{Fore.RESET}] Speed choice (1-6): ")
    
    speed_map = {
        "1": 0.1,
        "2": 0.5,
        "3": 1.0,
        "4": 2.0,
        "5": 5.0
    }
    
    if speed_choice == "6":
        try:
            custom_delay = float(input(f"{Fore.RESET}[{color}>{Fore.RESET}] Enter custom delay in seconds: "))
            delay = custom_delay
        except ValueError:
            print(f"{ld} {Fore.RED}Invalid delay, using normal speed{Fore.RESET}")
            delay = 1.0
    else:
        delay = speed_map.get(speed_choice, 1.0)
    
    # Start spamming
    print(f"\n{ld} {Fore.GREEN}Starting email spam...{Fore.RESET}")
    print(f"{ld} {Fore.CYAN}Recipients: {len(recipient_emails)}{Fore.RESET}")
    print(f"{ld} {Fore.CYAN}Sender accounts: {len(sender_accounts)}{Fore.RESET}")
    print(f"{ld} {Fore.CYAN}Delay: {delay}s{Fore.RESET}")
    print()
    
    sent = 0
    failed = 0
    account_index = 0
    
    for recipient in recipient_emails:
        if account_index >= len(sender_accounts):
            account_index = 0
        
        account = sender_accounts[account_index]
        success = False
        
        if account['type'] == 'smtp':
            success = send_email_smtp(
                account['host'],
                account['port'],
                account['email'],
                account['password'],
                recipient,
                subject,
                message
            )
        elif account['type'] == 'maillogin':
            success = send_email_maillogin(
                account['provider'],
                account['email'],
                account['password'],
                recipient,
                subject,
                message
            )
        
        if success:
            sent += 1
        else:
            failed += 1
        
        account_index += 1
        time.sleep(delay)
    
    print(f"\n{ld} {Fore.GREEN}Email spam complete!{Fore.RESET}")
    print(f"{ld} {Fore.CYAN}Sent: {sent}{Fore.RESET}")
    print(f"{ld} {Fore.RED}Failed: {failed}{Fore.RESET}")
    
    log_info(f"Email spam completed - Sent: {sent}, Failed: {failed}", "email_spammer")
    
    input(f"{Fore.RESET}[{color}>{Fore.RESET}] Press Enter to continue...")

