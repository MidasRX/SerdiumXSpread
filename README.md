# SerdiumXSpread

<div align="center">

**A comprehensive Python-based automation toolkit for Discord and Telegram**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey.svg)](https://www.microsoft.com/windows)

</div>

---

## ⚠️ **IMPORTANT LEGAL NOTICE**

**PLEASE READ THIS SECTION CAREFULLY BEFORE USING THIS SOFTWARE**

### Terms of Service Compliance

This software is provided for **educational and research purposes only**. By using this tool, you agree to:

1. **Comply with all applicable laws and regulations** in your jurisdiction
2. **Respect the Terms of Service** of Discord, Telegram, and any other platforms you interact with
3. **Only use this tool on accounts you own** or have explicit written permission to manage
4. **Not use this tool for any illegal activities**, including but not limited to:
   - Harassment, spam, or abuse
   - Unauthorized access to accounts
   - Violation of platform terms of service
   - Any form of cybercrime

### Disclaimer

- **The developers and contributors of this project are NOT responsible** for any misuse of this software
- **Use at your own risk** - Violating platform terms of service may result in account suspension, termination, or legal action
- **This tool is not affiliated with, endorsed by, or connected to Discord Inc. or Telegram FZ-LLC**
- **Automated actions may violate platform terms of service** - Always review platform policies before use

### Responsible Use

This tool is intended for:
- ✅ Testing your own accounts and servers
- ✅ Educational purposes and learning about API interactions
- ✅ Legitimate automation of tasks you have permission to perform
- ✅ Research and development

**DO NOT use this tool to:**
- ❌ Spam or harass users
- ❌ Violate platform terms of service
- ❌ Perform unauthorized actions on accounts you don't own
- ❌ Engage in any illegal activities

---

## 📋 Table of Contents

- [Features](#-features)
- [Installation](#-installation)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Configuration](#-configuration)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)

---

## ✨ Features

### Discord Tools

#### Spreading Functions
- **Spread Message** - Send messages to multiple channels with customizable speed control
- **Spread Embed** - Send rich embeds to multiple channels
- **Spread Everywhere** - Automatically spread messages to all channels across all servers
- **Webhook Spammer** - Spam messages through webhook URLs with speed control
- **Token Leave Servers** - Bulk leave servers using multiple tokens

#### Advanced Token Management
- **Token Nuker** - Comprehensive account management tool
- **Token Editor** - Edit token properties and settings
- **Token Info** - Retrieve detailed information about tokens
- **Token Onliner** - Keep tokens online with custom status
- **Status Rotator** - Rotate between different status types
- **Nitro Checker** - Validate Discord Nitro gift codes
- **Mass DM** - Send direct messages to all friends

### Telegram Tools

- **Spread Message** - Send messages to multiple Telegram channels
- **Spread Link** - Share links across Telegram channels
- **Spread Bot Token** - Manage bot tokens
- **Spread Sticker** - Send stickers to channels
- **Spread Media** - Share media files
- **Spread File** - Distribute files across channels
- **Spread Channel** - Channel management tools

### Email Tools

- **Email Spammer** - Send bulk emails using SMTP or email login
  - Support for Gmail, Yahoo, Hotmail/Outlook, and Proton
  - SMTP configuration support (custom SMTP servers)
  - Email/password login support (automatic SMTP detection)
  - Load accounts from file or enter manually
  - Load recipients from file or enter manually
  - Customizable speed control
  - File format support: `SMTP=host:port:email:password` or `MAILOGIN=provider:email:password`

### Utility Tools

- **Proxy Checker** - Validate proxy servers
- **Proxy Scraper** - Scrape proxies from various sources
- **Token Checker** - Verify Discord token validity
- **Config Editor** - Edit configuration settings
- **Theme Changer** - Customize interface colors (12 themes available)
- **Clear Output/Input** - Manage output and input directories

### Key Features

- 🚀 **Speed Control** - Adjustable delays for all spreading functions (Very Fast, Fast, Normal, Slow, Very Slow, Custom)
- 🔄 **Multiple Channel Support** - Send to single or multiple channels simultaneously
- 📁 **File Management** - Automatic directory and file creation
- 🎨 **Customizable Themes** - 12 different color themes
- 🔐 **Token Management** - Support for file-based or manual token input
- ⚡ **Async Operations** - Efficient asynchronous processing for better performance
- 🛡️ **Error Handling** - Robust error handling and logging

---

## 🚀 Installation

### Prerequisites

- **Python 3.8 or higher** - [Download Python](https://www.python.org/downloads/)
- **Windows OS** (primary support)
- **Internet connection** for downloading dependencies

### Step 1: Clone or Download

```bash
git clone https://github.com/yourusername/SerdiumXSpread.git
cd SerdiumXSpread
```

Or download and extract the ZIP file.

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

**Note:** If you encounter websocket import errors, ensure you have the correct packages installed:
- The `websocket` package conflicts with `websocket-client`
- `websocket-client` is required and should be installed automatically
- `selenium` is required for browser automation features

### Step 3: Configure

1. Edit `config.json` to add any required API keys not mandatory you can skip that lmao (its only for ai bot feature that i will add later 
2. Place your tokens in `Input/tokens.txt` (one per line) (optional)
3. Place your proxies in `Input/proxies.txt` (one per line, format: `ip:port`) (optional)

### Step 4: Run

**Windows:**
```bash
python main.py
```

Or use the provided batch file:
```bash
start.bat
```

---

## 📖 Usage

### First Launch

On first launch, the tool will automatically:
- Create necessary directories (`Output/`, `Input/`)
- Create required output files
- Set up the folder structure

### Main Menu

The main menu provides access to all features:

```
1. Discord Spreader     5. Proxy Scraper
2. Telegram Spreader   6. Token Checker
3. Proxy Checker       7. Config Editor
4. Clear Output        8. Clear Input
                       9. Change Theme
                      10. About
```

### Discord Menu

Access comprehensive Discord tools:

```
1. Spread Message          6. Token Nuker
2. Token Leave Servers     7. Token Editor
3. Webhook Spammer         8. Status Rotator
4. Spread Embed            9. Nitro Checker
5. Spread Everywhere      10. Token Info
                          11. Token Onliner
                          12. Mass DM
```

### Speed Control

Most spreading functions support speed control:

1. **Very Fast** - 0.01s delay (use with caution)
2. **Fast** - 0.1s delay
3. **Normal** - 0.5s delay (recommended)
4. **Slow** - 1s delay
5. **Very Slow** - 2s delay
6. **Custom** - Enter your own delay in seconds

**⚠️ Warning:** Using very fast speeds may trigger rate limits or violate platform terms of service.

### Token Input Methods

Many functions support two token input methods:

1. **From File** - Load tokens from `Input/tokens.txt`
2. **Manual Input** - Enter tokens directly when prompted

### Input Files

- **tokens.txt** - One Discord token per line
- **proxies.txt** - One proxy per line, format: `ip:port` or `ip:port:user:pass`
- **messages.txt** - Message templates (one per line)
- **links.txt** - Links to spread
- **emails.txt** - Recipient email addresses (one per line)
- **email_accounts.txt** - Email sender accounts (see format below)
- **telegram_messages.txt** - Telegram message templates
- **group_id.txt** - Telegram group/channel IDs (one per line)

#### Email Accounts File Format

The `Input/email_accounts.txt` file supports two formats:

**SMTP Format:**
```
SMTP=smtp.example.com:587:sender@example.com:password
SMTP=smtp.gmail.com:465:user@gmail.com:app_password
```

**Email Login Format:**
```
MAILOGIN=gmail:user@gmail.com:app_password
MAILOGIN=yahoo:user@yahoo.com:password
MAILOGIN=hotmail:user@hotmail.com:password
MAILOGIN=proton:user@protonmail.com:password
```

**Supported Providers:**
- `gmail` - Gmail (requires App Password for 2FA accounts)
- `yahoo` - Yahoo Mail
- `hotmail` or `outlook` - Microsoft Outlook/Hotmail
- `proton` - ProtonMail (requires ProtonMail Bridge)

---

## 🔧 Troubleshooting

### Common Issues

#### Import Errors

**Problem:** `ImportError: cannot import name 'WebSocketApp' from 'websocket'`

**Solution:**
```bash
pip uninstall websocket -y
pip install websocket-client selenium
```

#### Module Not Found

**Problem:** `ModuleNotFoundError: No module named 'X'`

**Solution:**
```bash
pip install -r requirements.txt
```

#### Permission Errors

**Problem:** Cannot create files or directories

**Solution:** Run with administrator privileges or check folder permissions

#### Rate Limiting

**Problem:** Getting rate limited by Discord/Telegram

**Solution:**
- Use slower speed settings
- Reduce the number of concurrent operations
- Add delays between requests
- Use proxies (if allowed by platform terms)

### Getting Help

1. Check the error message carefully
2. Review the troubleshooting section
3. Ensure all dependencies are installed
4. Verify your configuration files
5. Check that you're using valid tokens/proxies

---

## 🤝 Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Code Style

- Follow PEP 8 Python style guidelines
- Add comments for complex logic
- Update documentation for new features
- Test your changes before submitting

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Built with Python
- Uses various open-source libraries (see `requirements.txt`)
- Inspired by community automation tools

---

## 📞 Support

For issues, questions, or contributions:
- Open an issue on GitHub
- Review the documentation
- Check existing issues for solutions

---

## ⚠️ Final Reminder

**This tool is for educational purposes only. Always:**
- ✅ Respect platform terms of service
- ✅ Only use on accounts you own
- ✅ Follow all applicable laws
- ✅ Use responsibly and ethically

**The developers are not responsible for misuse of this software.**

---

<div align="center">

**Made with ❤️ for educational purposes**

**Use responsibly and at your own risk**

</div>
