from Helper import *
from Helper.Common.utils import *
import Helper

# Session for token spammer
session = tls_client.Session(client_identifier="chrome_122", random_tls_extension_order=True)
session.keep_alive = True

def send_message(token, channel_id, payload):
    """Send message using token to a channel"""
    global session
    color = Helper.color
    header = {
        'authorization': token
    }
    try:
        r = session.post(f"https://discord.com/api/v8/channels/{channel_id}/messages", json=payload, headers=header)
    except requests.exceptions.RequestException as e:
        print(f"{ld} {Fore.RED}Error occurred with token: {token[:20]}...{Fore.RESET}\n{e}")
        return

    if r.status_code == 200:
        print(f"{lc} {Fore.BLUE}token={Fore.WHITE}{token[:20]}...{Fore.RESET} {Fore.LIGHTBLACK_EX}[{Fore.GREEN}Message sent{Fore.LIGHTBLACK_EX}]")
    else:
        print(f"{lc} {Fore.BLUE}token={Fore.WHITE}{token[:20]}...{Fore.RESET} Failed to send message. -> {Fore.LIGHTBLACK_EX}({r.status_code})")

def send_discord_webhook_message(webhook_url, message, frequency=0.1):
    """Send message via webhook"""
    color = Helper.color
    payload = {
        "content": message
    }
    response = requests.post(webhook_url, json=payload)
    if response.status_code == 204:
        print(f"{lc} {Fore.BLUE}Webhook={Fore.WHITE}{webhook_url[:50]}...{Fore.RESET} {Fore.LIGHTBLACK_EX}[{Fore.GREEN}Message Sent{Fore.LIGHTBLACK_EX}]")
    else:
        print(f"{lc} {Fore.BLUE}Webhook={Fore.WHITE}{webhook_url[:50]}...{Fore.RESET} {Fore.LIGHTBLACK_EX}[{Fore.RED}FAILED: {response.status_code}{Fore.LIGHTBLACK_EX}]")
    time.sleep(frequency)

async def send_message_to_channel(session, token, guild_id, channel_id, message):
    """Send message to a specific channel"""
    url = f'https://discord.com/api/v9/channels/{channel_id}/messages'
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    data = {
        'content': message
    }
    async with session.post(url, headers=headers, json=data) as response:
        if response.status == 200:
            print(f"{lc} Message sent to channel {channel_id} in guild {guild_id}.")

async def send_messages_to_channels(token, message, delay=0.1):
    """Send messages to all channels in all guilds"""
    url = 'https://discord.com/api/v9/users/@me/guilds'
    headers = {
        'Authorization': token
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            if response.status != 200:
                print(f"{ld} {Fore.RED}Failed to fetch guilds. Make sure the token is correct.{Fore.RESET}")
                return
            guilds = await response.json()
            tasks = []
            for guild in guilds:
                guild_id = guild['id']
                async with session.get(f'https://discord.com/api/v9/guilds/{guild_id}/channels', headers=headers) as channels_response:
                    if channels_response.status != 200:
                        continue
                    channels = await channels_response.json()
                    for channel in channels:
                        channel_id = channel['id']
                        channel_type = channel['type']
                        if channel_type != 0:  # Only text channels
                            continue
                        task = send_message_to_channel(session, token, guild_id, channel_id, message)
                        tasks.append(task)
                        if len(tasks) >= 15:
                            await asyncio.gather(*tasks)
                            await asyncio.sleep(delay)  # Add delay between batches
                            tasks = []
            if tasks:
                await asyncio.gather(*tasks)

def leave_server(guild_id, token, count_lock):
    """Leave a server using token"""
    global left, not_inside, inv
    color = Helper.color
    headers = {
        "Authorization": token,
    }
    session = tls_client.Session(client_identifier="chrome_122", random_tls_extension_order=True)
    response = session.delete(f"https://discord.com/api/v9/users/@me/guilds/{guild_id}", headers=headers)

    if response.status_code == 204:
        with count_lock:
            left += 1
        print(f'{lc} {Fore.BLUE}token={Fore.WHITE}{token[:20]}...{Fore.RESET} Left Server: [{Fore.BLUE}{guild_id}{Fore.RESET}]')
    elif response.status_code == 401 or response.status_code == 404:
        with count_lock:
            not_inside += 1
        print(f'{lc} {Fore.BLUE}token={Fore.WHITE}{token[:20]}...{Fore.RESET} Isn\'t in the Guild id: [{Fore.BLUE}{guild_id}{Fore.RESET}]')
    else:
        with count_lock:
            inv += 1
        print(f'{lc} {Fore.BLUE}token={Fore.WHITE}{token[:20]}...{Fore.RESET} Is Invalid or couldn\'t be checked')

# Global counters for leave server
left = 0
not_inside = 0
inv = 0

