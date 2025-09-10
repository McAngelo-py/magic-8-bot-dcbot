# 🎱 Magic 8 Ball Discord Bot

A fun Discord bot that answers your yes/no questions just like a classic Magic 8 Ball! Ask any question and get mystical responses with beautiful embed formatting.

## ✨ Features

- 🔮 **20 Classic Magic 8 Ball Responses** - All the traditional answers you know and love
- 💬 **Multiple Ways to Ask** - Use commands or mention the bot directly
- 🎨 **Beautiful Embeds** - Nicely formatted responses with colors and emojis
- ❓ **Question Detection** - Automatically responds when mentioned with questions
- 🛡️ **Error Handling** - Helpful error messages and guidance

## 🚀 Quick Start

### 1. Prerequisites
- Python 3.8 or higher
- A Discord account
- Basic knowledge of creating Discord bots

### 2. Discord Bot Setup
1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Click "New Application" and give it a name
3. Go to the "Bot" section in the left sidebar
4. Click "Add Bot"
5. Copy the bot token (you'll need this later)
6. Under "Privileged Gateway Intents", enable:
   - Message Content Intent

### 3. Installation

1. **Clone or download this project**
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   - Copy `.env.example` to `.env`
   - Replace `your_bot_token_here` with your actual bot token
   ```
   DISCORD_BOT_TOKEN=your_actual_bot_token_here
   ```

4. **Run the bot:**
   ```bash
   python magic8ball_bot.py
   ```

### 4. Invite Bot to Server
1. In Discord Developer Portal, go to "OAuth2" > "URL Generator"
2. Select scopes: `bot`
3. Select bot permissions: `Send Messages`, `Use Slash Commands`, `Embed Links`
4. Copy the generated URL and open it to invite the bot to your server

## 📦 Deployment

### 🔧 Git Setup

1. **Initialize Git repository:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Magic 8 Ball Discord Bot"
   ```

2. **Push to GitHub:**
   ```bash
   git remote add origin https://github.com/yourusername/magic8ball-bot.git
   git branch -M main
   git push -u origin main
   ```

### ☁️ Free Hosting Options

#### **Railway** ⭐ *Recommended*
1. Connect your GitHub repository to [Railway](https://railway.app)
2. Add environment variable: `DISCORD_TOKEN=your_bot_token`
3. Deploy automatically - Railway will detect the `railway.json` config

#### **Heroku**
1. Install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
2. Login and create app:
   ```bash
   heroku login
   heroku create your-magic8ball-bot
   ```
3. Set environment variable:
   ```bash
   heroku config:set DISCORD_TOKEN=your_bot_token
   ```
4. Deploy:
   ```bash
   git push heroku main
   ```

#### **Render**
1. Connect GitHub repo to [Render](https://render.com)
2. Create a new "Web Service"
3. Set build command: `pip install -r requirements.txt`
4. Set start command: `python magic8ball_bot.py`
5. Add environment variable: `DISCORD_TOKEN=your_bot_token`

### 📋 Deployment Files Included
- **`.gitignore`** - Excludes sensitive files from Git
- **`Procfile`** - Heroku deployment configuration
- **`railway.json`** - Railway deployment configuration
- **`.env.example`** - Template for environment variables

## 🎮 How to Use

### Method 1: Slash Commands (Recommended - Works Immediately!)
```
/8ball question:Will I have a good day?
/8ball question:Should I study tonight?
/8ball question:Is it going to rain tomorrow?
```

### Method 2: Traditional Commands (Requires Message Content Intent)
```
!8ball Will I have a good day?
!magic8ball Should I study tonight?
!ask Is it going to rain tomorrow?
```

### Method 3: Mention the Bot (Requires Message Content Intent)
```
@Magic8Ball Will I pass my exam?
@Magic8Ball Should I go out tonight?
```

### Get Help
```
/help
!help_8ball
```

## 🎱 Magic 8 Ball Responses

The bot includes an expanded collection of responses with humor and variety:

**Positive Responses (18):** Classic answers like "It is certain" and "Yes definitely", plus fun additions like "✨ Absolutely!", "🚀 Launch into action!", "🌈 Rainbow of possibilities ahead", and "🎯 Bulls-eye! Go for it!"

**Non-committal Responses (13):** Traditional responses like "Ask again later" and "Cannot predict now", enhanced with creative options like "🌫️ The mists of time obscure the answer", "🎲 The dice are still rolling", and "💭 The answer lies within you"

**Negative Responses (12):** Standard answers like "My reply is no" and "Very doubtful", expanded with expressive responses like "❌ Not in this lifetime", "⛈️ Storm clouds gather", and "🛑 Stop right there"

**Humorous "No Answer" Responses (20):** Fun responses when the magic 8 ball can't or won't answer, including "🤷 I'm just a magic 8 ball, not a miracle worker", "😴 The magic 8 ball is taking a nap", "🔋 Battery low, answer unclear", "🍕 Ask me after I finish this pizza", and "🦄 Even unicorns don't know this one"

**Total: 63 unique responses** for maximum variety and entertainment!

## 📁 Project Structure

```
magic8ball-discord-bot/
├── magic8ball_bot.py      # Main bot file
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
├── .env                  # Your actual environment variables (create this)
└── README.md             # This file
```

## 🛠️ Customization

You can easily customize the bot by:

- **Adding more responses:** Edit the `MAGIC_8_BALL_RESPONSES` list in `magic8ball_bot.py`
- **Changing colors:** Modify the embed color (`0x800080` = purple)
- **Adding new commands:** Follow the existing command structure
- **Changing the prefix:** Modify `command_prefix='!'` in the bot setup

## 🔧 Troubleshooting

**Bot doesn't respond:**
- Make sure the bot has proper permissions in your server
- Check that Message Content Intent is enabled
- Verify your bot token is correct

**Import errors:**
- Make sure you installed all requirements: `pip install -r requirements.txt`
- Check your Python version (3.8+ required)

**Permission errors:**
- Ensure the bot has "Send Messages" and "Embed Links" permissions
- Check channel-specific permissions

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Feel free to fork this project and submit pull requests for improvements!

---

**Have fun asking the Magic 8 Ball your burning questions! 🔮✨**