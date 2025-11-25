from Helper import *
from Helper.Common.utils import *
import Helper
import asyncio

async def auto_forward_messages(client, source_chat_id, destination_chat_ids, custom_message=None, forward_to_all=False):
    """Auto-forward messages from source to multiple destinations with optional custom message"""
    color = Helper.color
    
    try:
        from telethon import events
        
        # Convert source to integer if it's a numeric string
        try:
            source_chat_id = int(source_chat_id)
        except ValueError:
            pass  # Keep as string if it's a username
        
        # Convert destination IDs to integers
        destination_ids = []
        for dest_id in destination_chat_ids:
            try:
                destination_ids.append(int(dest_id))
            except ValueError:
                destination_ids.append(dest_id)  # Keep as string if it's a username
        
        # If forward to all, get all groups/channels
        if forward_to_all:
            try:
                dialogs = await client.get_dialogs()
                for dialog in dialogs:
                    entity = dialog.entity
                    # Only add groups and channels, not private chats
                    if hasattr(entity, 'megagroup') or hasattr(entity, 'broadcast') or hasattr(entity, 'id'):
                        if hasattr(entity, 'id'):
                            destination_ids.append(entity.id)
                print(f"{ld} {Fore.CYAN}Found {len(destination_ids)} groups/channels to forward to{Fore.RESET}")
            except Exception as e:
                print(f"{ld} {Fore.RED}Failed to get all groups: {e}{Fore.RESET}")
                log_error(f"Failed to get all groups: {str(e)}", "ERROR", "auto_forward")
        
        @client.on(events.NewMessage(chats=source_chat_id))
        async def handler(event):
            for dest_id in destination_ids:
                try:
                    # Forward the original message
                    await client.forward_messages(dest_id, event.message)
                    print(f"{lc} {Fore.GREEN}Forwarded to {dest_id}{Fore.RESET}")
                    
                    # Send custom message if provided
                    if custom_message:
                        try:
                            await client.send_message(dest_id, custom_message)
                            print(f"{lc} {Fore.CYAN}Sent custom message to {dest_id}{Fore.RESET}")
                        except Exception as e:
                            print(f"{lc} {Fore.YELLOW}Failed to send custom message to {dest_id}: {e}{Fore.RESET}")
                            log_error(f"Failed to send custom message to {dest_id}: {str(e)}", "WARNING", "auto_forward")
                except Exception as e:
                    print(f"{lc} {Fore.RED}Failed to forward to {dest_id}: {e}{Fore.RESET}")
                    log_error(f"Failed to forward to {dest_id}: {str(e)}", "ERROR", "auto_forward")
        
        print(f"{ld} {Fore.GREEN}Auto-forward started! Press Ctrl+C to stop{Fore.RESET}")
        print(f"{ld} {Fore.CYAN}Source: {source_chat_id}{Fore.RESET}")
        print(f"{ld} {Fore.CYAN}Destinations: {len(destination_ids)} group(s)/channel(s){Fore.RESET}")
        if custom_message:
            print(f"{ld} {Fore.CYAN}Custom message enabled{Fore.RESET}")
        await client.run_until_disconnected()
    except Exception as e:
        print(f"{ld} {Fore.RED}Error in auto-forward: {e}{Fore.RESET}")
        log_error(f"Auto-forward error: {str(e)}", "ERROR", "auto_forward")

async def nuke_telegram_account(client):
    """Nuke Telegram account - delete all messages, leave all groups"""
    color = Helper.color
    new_title("Telegram Account Nuker")
    
    print(f"{ld} {Fore.YELLOW}Starting account nuke...{Fore.RESET}")
    print(f"{ld} {Fore.RED}This will delete all messages and leave all groups/channels!{Fore.RESET}")
    
    deleted_dialogs = 0
    left_groups = 0
    deleted_messages = 0
    errors = 0
    
    try:
        # Get all dialogs
        dialogs = await client.get_dialogs()
        
        for dialog in dialogs:
            try:
                entity = dialog.entity
                
                # Delete all messages in dialog
                try:
                    messages = await client.get_messages(entity, limit=None)
                    for message in messages:
                        try:
                            await message.delete()
                            deleted_messages += 1
                            if deleted_messages % 10 == 0:
                                print(f"{lc} {Fore.CYAN}Deleted {deleted_messages} messages...{Fore.RESET}")
                        except Exception as e:
                            errors += 1
                            log_error(f"Failed to delete message: {str(e)}", "ERROR", "nuke_telegram")
                except Exception as e:
                    log_error(f"Failed to get messages from {entity.title if hasattr(entity, 'title') else 'unknown'}: {str(e)}", "ERROR", "nuke_telegram")
                
                # Leave groups and channels
                if hasattr(entity, 'megagroup') or hasattr(entity, 'broadcast'):
                    try:
                        await client.delete_dialog(entity)
                        left_groups += 1
                        print(f"{lc} {Fore.GREEN}Left: {entity.title if hasattr(entity, 'title') else 'Unknown'}{Fore.RESET}")
                    except Exception as e:
                        errors += 1
                        log_error(f"Failed to leave {entity.title if hasattr(entity, 'title') else 'unknown'}: {str(e)}", "ERROR", "nuke_telegram")
                else:
                    # Delete private chat
                    try:
                        await client.delete_dialog(entity)
                        deleted_dialogs += 1
                        print(f"{lc} {Fore.GREEN}Deleted dialog: {entity.title if hasattr(entity, 'title') else 'Unknown'}{Fore.RESET}")
                    except Exception as e:
                        errors += 1
                        log_error(f"Failed to delete dialog: {str(e)}", "ERROR", "nuke_telegram")
                
            except Exception as e:
                errors += 1
                log_error(f"Error processing dialog: {str(e)}", "ERROR", "nuke_telegram")
        
        print(f"\n{ld} {Fore.GREEN}Nuke Complete!{Fore.RESET}")
        print(f"{ld} {Fore.CYAN}Deleted Dialogs: {deleted_dialogs}{Fore.RESET}")
        print(f"{ld} {Fore.CYAN}Left Groups: {left_groups}{Fore.RESET}")
        print(f"{ld} {Fore.CYAN}Deleted Messages: {deleted_messages}{Fore.RESET}")
        print(f"{ld} {Fore.RED}Errors: {errors}{Fore.RESET}")
        
        log_info(f"Account nuke completed - Dialogs: {deleted_dialogs}, Groups: {left_groups}, Messages: {deleted_messages}, Errors: {errors}", "nuke_telegram")
        
    except Exception as e:
        print(f"{ld} {Fore.RED}Nuke failed: {e}{Fore.RESET}")
        log_error(f"Account nuke failed: {str(e)}", "ERROR", "nuke_telegram")

