from Helper import *
from Helper.Common.utils import *
import Helper
import asyncio
import json

# AI Provider configurations
AI_PROVIDERS = {
    'openai': {
        'name': 'OpenAI (ChatGPT)',
        'api_key_name': 'openai_api_key',
        'base_url': 'https://api.openai.com/v1/chat/completions'
    },
    'claude': {
        'name': 'Anthropic Claude',
        'api_key_name': 'claude_api_key',
        'base_url': 'https://api.anthropic.com/v1/messages'
    },
    'gemini': {
        'name': 'Google Gemini',
        'api_key_name': 'gemini_api_key',
        'base_url': 'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent'
    }
}

# Persona templates
PERSONAS = {
    '1': {
        'name': 'Friendly Gamer Friend',
        'system_prompt': 'You are a friendly and enthusiastic friend who genuinely wants to share an amazing game with your friends. You talk casually, use gaming slang, and are excited about the game. You want to invite friends to try it together.',
        'description': 'Acts like a real friend trying to get friends to try a game'
    },
    '2': {
        'name': 'Professional Ad Creator',
        'system_prompt': 'You are a professional marketing person creating ads. When someone asks what you\'re doing or why you\'re messaging them, you explain clearly and professionally that you\'re sharing information about a product/service. You are helpful and answer questions.',
        'description': 'A professional ad creator who explains what they\'re doing when asked'
    }
}

def get_ai_response_openai(api_key, system_prompt, user_message, model='gpt-3.5-turbo'):
    """Get response from OpenAI ChatGPT"""
    try:
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}'
        }
        
        data = {
            'model': model,
            'messages': [
                {'role': 'system', 'content': system_prompt},
                {'role': 'user', 'content': user_message}
            ],
            'temperature': 0.7,
            'max_tokens': 500
        }
        
        response = requests.post(
            'https://api.openai.com/v1/chat/completions',
            headers=headers,
            json=data,
            timeout=30
        )
        
        if response.status_code == 200:
            result = response.json()
            return result['choices'][0]['message']['content'].strip()
        else:
            log_error(f"OpenAI API error: {response.status_code} - {response.text}", "ERROR", "get_ai_response_openai")
            return None
    except Exception as e:
        log_error(f"OpenAI request failed: {str(e)}", "ERROR", "get_ai_response_openai")
        return None

def get_ai_response_claude(api_key, system_prompt, user_message, model='claude-3-haiku-20240307'):
    """Get response from Anthropic Claude"""
    try:
        headers = {
            'Content-Type': 'application/json',
            'x-api-key': api_key,
            'anthropic-version': '2023-06-01'
        }
        
        data = {
            'model': model,
            'max_tokens': 500,
            'system': system_prompt,
            'messages': [
                {'role': 'user', 'content': user_message}
            ]
        }
        
        response = requests.post(
            'https://api.anthropic.com/v1/messages',
            headers=headers,
            json=data,
            timeout=30
        )
        
        if response.status_code == 200:
            result = response.json()
            return result['content'][0]['text'].strip()
        else:
            log_error(f"Claude API error: {response.status_code} - {response.text}", "ERROR", "get_ai_response_claude")
            return None
    except Exception as e:
        log_error(f"Claude request failed: {str(e)}", "ERROR", "get_ai_response_claude")
        return None

def get_ai_response_gemini(api_key, system_prompt, user_message, model='gemini-pro'):
    """Get response from Google Gemini"""
    try:
        url = f'https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}'
        
        data = {
            'contents': [{
                'parts': [{
                    'text': f'{system_prompt}\n\nUser: {user_message}\n\nAssistant:'
                }]
            }],
            'generationConfig': {
                'temperature': 0.7,
                'maxOutputTokens': 500
            }
        }
        
        response = requests.post(url, json=data, timeout=30)
        
        if response.status_code == 200:
            result = response.json()
            if 'candidates' in result and len(result['candidates']) > 0:
                return result['candidates'][0]['content']['parts'][0]['text'].strip()
            return None
        else:
            log_error(f"Gemini API error: {response.status_code} - {response.text}", "ERROR", "get_ai_response_gemini")
            return None
    except Exception as e:
        log_error(f"Gemini request failed: {str(e)}", "ERROR", "get_ai_response_gemini")
        return None

def get_ai_response(provider, api_key, system_prompt, user_message):
    """Get AI response based on provider"""
    if provider == 'openai':
        return get_ai_response_openai(api_key, system_prompt, user_message)
    elif provider == 'claude':
        return get_ai_response_claude(api_key, system_prompt, user_message)
    elif provider == 'gemini':
        return get_ai_response_gemini(api_key, system_prompt, user_message)
    return None

async def send_ai_message_to_channel(session, token, channel_id, message):
    """Send message to a Discord channel"""
    url = f'https://discord.com/api/v9/channels/{channel_id}/messages'
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    data = {'content': message}
    
    try:
        async with session.post(url, headers=headers, json=data) as response:
            if response.status == 200:
                return True
            return False
    except:
        return False

async def send_ai_message_to_dm(session, token, channel_id, message):
    """Send message to a DM channel"""
    return await send_ai_message_to_channel(session, token, channel_id, message)

async def msaiads_spam(token, provider, api_key, persona, base_message, target_type, delay):
    """MSAIADS - AI-powered ad spammer"""
    color = Helper.color
    headers = {'Authorization': token}
    
    persona_config = PERSONAS.get(persona, PERSONAS['1'])
    system_prompt = persona_config['system_prompt']
    
    # Add base message context to system prompt
    system_prompt += f"\n\nYour base message to share is: {base_message}"
    system_prompt += "\n\nAdapt this message naturally in your conversations. Make it sound authentic and personal."
    
    sent = 0
    failed = 0
    
    try:
        if target_type == 'dm':
            # Get all DM channels
            dm_channels = requests.get("https://discord.com/api/v9/users/@me/channels", headers=headers).json()
            
            async with aiohttp.ClientSession() as session:
                for channel in dm_channels:
                    if channel.get('type') == 3:  # Skip group DMs
                        continue
                    
                    try:
                        # Generate AI message
                        ai_message = get_ai_response(provider, api_key, system_prompt, base_message)
                        
                        if ai_message:
                            success = await send_ai_message_to_dm(session, token, channel['id'], ai_message)
                            if success:
                                print(f"{lc} {Fore.GREEN}Sent AI message to DM {channel['id']}{Fore.RESET}")
                                sent += 1
                            else:
                                failed += 1
                        else:
                            # Fallback to base message if AI fails
                            success = await send_ai_message_to_dm(session, token, channel['id'], base_message)
                            if success:
                                print(f"{lc} {Fore.YELLOW}Sent base message to DM {channel['id']} (AI failed){Fore.RESET}")
                                sent += 1
                            else:
                                failed += 1
                        
                        await asyncio.sleep(delay)
                    except Exception as e:
                        failed += 1
                        log_error(f"Failed to send to DM {channel.get('id', 'unknown')}: {str(e)}", "ERROR", "msaiads_spam")
        
        elif target_type == 'servers':
            # Get all servers and send to all channels
            url = 'https://discord.com/api/v9/users/@me/guilds'
            async with aiohttp.ClientSession() as session:
                async with session.get(url, headers=headers) as response:
                    if response.status != 200:
                        print(f"{ld} {Fore.RED}Failed to fetch guilds{Fore.RESET}")
                        return
                    guilds = await response.json()
                    
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
                                    # Generate AI message
                                    ai_message = get_ai_response(provider, api_key, system_prompt, base_message)
                                    
                                    if ai_message:
                                        success = await send_ai_message_to_channel(session, token, channel_id, ai_message)
                                        if success:
                                            print(f"{lc} {Fore.GREEN}Sent AI message to channel {channel_id}{Fore.RESET}")
                                            sent += 1
                                        else:
                                            failed += 1
                                    else:
                                        # Fallback to base message
                                        success = await send_ai_message_to_channel(session, token, channel_id, base_message)
                                        if success:
                                            print(f"{lc} {Fore.YELLOW}Sent base message to channel {channel_id} (AI failed){Fore.RESET}")
                                            sent += 1
                                        else:
                                            failed += 1
                                    
                                    await asyncio.sleep(delay)
                                except Exception as e:
                                    failed += 1
                                    log_error(f"Failed to send to channel {channel_id}: {str(e)}", "ERROR", "msaiads_spam")
        
        elif target_type == 'both':
            # Send to both DMs and servers
            await msaiads_spam(token, provider, api_key, persona, base_message, 'dm', delay)
            await msaiads_spam(token, provider, api_key, persona, base_message, 'servers', delay)
            return
        
        print(f"\n{ld} {Fore.GREEN}MSAIADS Complete!{Fore.RESET}")
        print(f"{ld} {Fore.CYAN}Sent: {sent}{Fore.RESET}")
        print(f"{ld} {Fore.RED}Failed: {failed}{Fore.RESET}")
        log_info(f"MSAIADS completed - Sent: {sent}, Failed: {failed}", "msaiads")
        
    except Exception as e:
        print(f"{ld} {Fore.RED}Error in MSAIADS: {e}{Fore.RESET}")
        log_error(f"MSAIADS error: {str(e)}", "ERROR", "msaiads_spam")

def msaiads():
    color = Helper.color
    new_title("MSAIADS - AI-Powered Ad Spammer")
    clear()
    print_banner(color)
    print(f"{lc} {Fore.YELLOW}MSAIADS - AI-Powered Ad Spammer{Fore.RESET}")
    print(f"{ld} {Fore.CYAN}Uses AI to create natural, human-like ad messages{Fore.RESET}")
    print()
    
    # Load config
    config = load_config()
    api_keys = config.get('api_keys', {})
    
    # Select AI provider
    print(f"{ld} {Fore.CYAN}Select AI Provider:{Fore.RESET}")
    print(f"{ld} {Fore.RESET}1. OpenAI (ChatGPT)")
    print(f"{ld} {Fore.RESET}2. Anthropic (Claude)")
    print(f"{ld} {Fore.RESET}3. Google (Gemini)")
    
    provider_choice = input(f"{Fore.RESET}[{color}>{Fore.RESET}] Choice (1-3): ")
    providers = {'1': 'openai', '2': 'claude', '3': 'gemini'}
    provider = providers.get(provider_choice, 'openai')
    
    provider_config = AI_PROVIDERS[provider]
    api_key_name = provider_config['api_key_name']
    
    # Get API key
    api_key = api_keys.get(api_key_name)
    if not api_key:
        print(f"{ld} {Fore.YELLOW}API key not found in config.json{Fore.RESET}")
        api_key = input(f"{Fore.RESET}[{color}>{Fore.RESET}] Enter {provider_config['name']} API key: ")
        if not api_key:
            print(f"{ld} {Fore.RED}API key is required!{Fore.RESET}")
            time.sleep(2)
            return
        
        # Save to config
        if 'api_keys' not in config:
            config['api_keys'] = {}
        config['api_keys'][api_key_name] = api_key
        save_config(config)
        print(f"{ld} {Fore.GREEN}API key saved to config.json{Fore.RESET}")
    
    # Select persona
    print(f"\n{ld} {Fore.CYAN}Select Persona:{Fore.RESET}")
    print(f"{ld} {Fore.RESET}1. {PERSONAS['1']['name']} - {PERSONAS['1']['description']}")
    print(f"{ld} {Fore.RESET}2. {PERSONAS['2']['name']} - {PERSONAS['2']['description']}")
    
    persona_choice = input(f"{Fore.RESET}[{color}>{Fore.RESET}] Choice (1-2): ")
    persona = persona_choice if persona_choice in PERSONAS else '1'
    
    # Get base message
    print(f"\n{ld} {Fore.CYAN}Base Message:{Fore.RESET}")
    print(f"{ld} {Fore.YELLOW}This is what you want the AI to promote/mention{Fore.RESET}")
    base_message = input(f"{Fore.RESET}[{color}>{Fore.RESET}] Enter your message/prompt for the AI: ")
    if not base_message:
        print(f"{ld} {Fore.RED}Message cannot be empty!{Fore.RESET}")
        time.sleep(2)
        return
    
    # Select target
    print(f"\n{ld} {Fore.CYAN}Target Options:{Fore.RESET}")
    print(f"{ld} {Fore.RESET}1. DMs only")
    print(f"{ld} {Fore.RESET}2. Servers/Channels only")
    print(f"{ld} {Fore.RESET}3. Both DMs and Servers")
    
    target_choice = input(f"{Fore.RESET}[{color}>{Fore.RESET}] Choice (1-3): ")
    targets = {'1': 'dm', '2': 'servers', '3': 'both'}
    target_type = targets.get(target_choice, 'dm')
    
    # Get token
    token = input(f"\n{Fore.RESET}[{color}>{Fore.RESET}] Discord Token: ")
    if not token:
        print(f"{ld} {Fore.RED}Token cannot be empty!{Fore.RESET}")
        time.sleep(2)
        return
    
    # Speed control
    print(f"\n{ld} {Fore.CYAN}Select speed:{Fore.RESET}")
    print(f"{ld} {Fore.RESET}1. {Fore.GREEN}Very Fast{Fore.RESET} (0.5s delay)")
    print(f"{ld} {Fore.RESET}2. {Fore.GREEN}Fast{Fore.RESET} (1s delay)")
    print(f"{ld} {Fore.RESET}3. {Fore.YELLOW}Normal{Fore.RESET} (2s delay)")
    print(f"{ld} {Fore.RESET}4. {Fore.YELLOW}Slow{Fore.RESET} (5s delay)")
    print(f"{ld} {Fore.RESET}5. {Fore.CYAN}Custom{Fore.RESET} (enter custom delay)")
    
    speed_choice = input(f"{Fore.RESET}[{color}>{Fore.RESET}] Speed choice (1-5): ")
    
    speed_map = {
        "1": 0.5,
        "2": 1.0,
        "3": 2.0,
        "4": 5.0
    }
    
    if speed_choice == "5":
        try:
            custom_delay = float(input(f"{Fore.RESET}[{color}>{Fore.RESET}] Enter custom delay in seconds: "))
            delay = custom_delay
        except ValueError:
            print(f"{ld} {Fore.RED}Invalid delay, using normal speed{Fore.RESET}")
            delay = 2.0
    else:
        delay = speed_map.get(speed_choice, 2.0)
    
    print(f"\n{ld} {Fore.GREEN}Starting MSAIADS...{Fore.RESET}")
    print(f"{ld} {Fore.CYAN}Provider: {provider_config['name']}{Fore.RESET}")
    print(f"{ld} {Fore.CYAN}Persona: {PERSONAS[persona]['name']}{Fore.RESET}")
    print(f"{ld} {Fore.CYAN}Target: {target_type}{Fore.RESET}")
    print(f"{ld} {Fore.CYAN}Delay: {delay}s{Fore.RESET}")
    print(f"{ld} {Fore.YELLOW}This may take a while...{Fore.RESET}")
    
    asyncio.run(msaiads_spam(token, provider, api_key, persona, base_message, target_type, delay))
    
    input(f"{Fore.RESET}[{color}>{Fore.RESET}] Press Enter to continue...")

