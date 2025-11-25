__title__ = 'SerdiumXSpread'
__author__ = 'SerdiumX'
__copyright__ = 'SerdiumX Spread Tool'
__version__ = '1.0.0'

import re
import os
import time
import threading
import requests
import concurrent.futures
import json
import urllib.request
import socket
import base64
import codecs
import random
import string
import httpx
import tls_client
import secrets
import ctypes
import websocket
import sys
import aiohttp
import asyncio
import pytz
import shutil
import tempfile
import subprocess
import http

# Lazy import for undetected_chromedriver to avoid conflicts
# Import will be attempted when first accessed via get_uc() function
_uc_module = None
_uc_import_error = None

def get_uc():
    """Lazy import for undetected_chromedriver. Returns the module or None if import failed."""
    global _uc_module, _uc_import_error
    if _uc_module is None and _uc_import_error is None:
        try:
            import undetected_chromedriver
            _uc_module = undetected_chromedriver
        except (ImportError, Exception) as e:
            _uc_import_error = e
            _uc_module = None
    return _uc_module

# For backward compatibility, create a proxy object
class UcProxy:
    def __getattr__(self, name):
        uc = get_uc()
        if uc is None:
            raise ImportError(
                "undetected_chromedriver not available. "
                "The 'websocket' package conflicts with 'websocket-client'. "
                "Run 'python fix_websocket.py' to fix this issue."
            ) from _uc_import_error
        return getattr(uc, name)
    
    def __call__(self, *args, **kwargs):
        uc = get_uc()
        if uc is None:
            raise ImportError(
                "undetected_chromedriver not available. "
                "The 'websocket' package conflicts with 'websocket-client'. "
                "Run 'python fix_websocket.py' to fix this issue."
            ) from _uc_import_error
        return uc(*args, **kwargs)

uc = UcProxy()

try:
    import tkinter as tk
except ImportError:
    tk = None

from tkinter import filedialog
from faker import Faker
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, Style
from datetime import datetime
from tls_client import Session
from pathlib import Path
from base64 import b64decode
from Crypto.Cipher import AES
from win32crypt import CryptUnprotectData
from os import getlogin, listdir
from json import loads
from re import findall
from os.path import isfile, join
from bs4 import BeautifulSoup
from pytube import YouTube
from urllib.parse import urlparse, urljoin
from urllib.request import urlretrieve

# Import functions from Funcs
from .Funcs.file_spreader import file_spreader
from .Funcs.token_spreader import token_spreader
from .Funcs.message_spreader import message_spreader
from .Funcs.link_spreader import link_spreader
from .Funcs.email_spreader import email_spreader
from .Funcs.proxy_scraper import proxy_scraper
from .Funcs.token_checker import token_checker
from .Funcs.proxy_checker import proxy_checker
from .Funcs.webhook_spreader import webhook_spreader
from .Funcs.config_editor import config_editor
from .Funcs.clear import clear_output, clear_input
from .Funcs.start import StartupTool
from .Funcs.about import about
from .Funcs.discord_menu import discord_menu
from .Funcs.telegram_menu import telegram_menu
from .Funcs.email_spammer import email_spammer

banner = f'''{Fore.LIGHTCYAN_EX}
                    ███████╗███████╗██████╗ ██████╗ ██╗██╗   ██╗███╗   ███╗    ██╗  ██╗    ███████╗██████╗ ███████╗ █████╗ ██████╗ ██████╗ 
                    ██╔════╝██╔════╝██╔══██╗██╔══██╗██║██║   ██║████╗ ████║    ╚██╗██╔╝    ██╔════╝██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔══██╗
                    ███████╗█████╗  ██████╔╝██║  ██║██║██║   ██║██╔████╔██║     ╚███╔╝     ███████╗██████╔╝█████╗  ███████║██║  ██║██║  ██║
                    ╚════██║██╔══╝  ██╔══██╗██║  ██║██║██║   ██║██║╚██╔╝██║     ██╔██╗     ╚════██║██╔═══╝ ██╔══╝  ██╔══██║██║  ██║██║  ██║
                    ███████║███████╗██║  ██║██████╔╝██║╚██████╔╝██║ ╚═╝ ██║    ██╔╝ ██╗    ███████║██║     ███████╗██║  ██║██████╔╝██████╔╝
                    ╚══════╝╚══════╝╚═╝  ╚═╝╚═════╝ ╚═╝ ╚═════╝ ╚═╝     ╚═╝    ╚═╝  ╚═╝    ╚══════╝╚═╝     ╚══════╝╚═╝  ╚═╝╚═════╝ ╚═════╝ 
                                                                    SerdiumX Spread Tool v{__version__}
    '''

os.system("title SerdiumXSpread")

# Global color variable for theme
color = Fore.LIGHTCYAN_EX

