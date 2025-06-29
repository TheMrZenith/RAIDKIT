# 💣 RAIDKIT - Discord Raid Bot

**⚠️ FOR EDUCATIONAL PURPOSES ONLY. DO NOT USE ON SERVERS WITHOUT PERMISSION.**  
Using this bot on servers without authorization is a violation of Discord's Terms of Service. You could face account bans or legal consequences. Use only in your own servers for testing purposes.

---

## 🚀 Features

- 🔥 **Delete everything**: Channels, categories, roles
- 📢 **Spam messages**: Send a large number of spam messages in all text channels
- 🛠️ **Create spam channels**: Automatically create a large number of channels
- 💥 **Rename the server**: Change the server name to something predefined
- 👢 **Kick all members**: Kicks all members except the bot

---

## 🧠 Requirements

Make sure you have the following:

- **Python 3.10 or higher**  
  You can download Python from [here](https://www.python.org/downloads/).
  
- Install necessary libraries:
  ```bash
  pip install discord.py colorama
  ```

## ⚙️ Setup
1. **Clone or Download the Repo**:
    Download the entire repository or clone it using:
  ```bash
  git clone https://github.com/TheMrZenith/RAIDKIT
  ```

2. **Create a Discord Bot:**
  Go to the [Discord Developer Portal](https://discord.com/developers/applications) and create a bot. Save your bot’s token.

3. **Invite the Bot to Your Server:**
    Make sure the bot has Admin Permissions to perform all the actions. Use this invite link format, replacing YOUR_BOT_ID:
  ```
  https://discord.com/oauth2/authorize?client_id=YOUR_BOT_ID&scope=bot&permissions=8
  ```

4. **Run the Bot:**
- Navigate to the folder where you have the bot file (raidbot.py).
- Use this command to start the bot:

```
python main.py
```

## 📝 How It Works
Once the bot starts, it will:
1. Login to your Discord account using the token provided.
2. Connect to the specified server (guild).
3. Perform the raid actions by executing the following sequence of commands:

* Delete all channels and categories.
* Kick all members (except for the bot).
* Create a large number of channels and roles.
* Rename the server.(Disabled)
* Spam messages across all text channels.

## ⚠️ DISCLAIMER

* This bot is not for malicious use. Use it responsibly and only on servers where you have full permission to do so.
* I am not responsible for any consequences that result from the use of this bot.
