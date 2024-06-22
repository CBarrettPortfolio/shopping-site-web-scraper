## A7X Merchandise Discord Notifier

This Python script scrapes the Avenged Sevenfold merchandise website and sends a Discord notification when new items are added. It's a handy tool for fans who want to stay up-to-date on the latest A7X merch drops.

### Features

- **Web Scraping:** Uses `requests` and `BeautifulSoup` to fetch and parse HTML content from the A7X merchandise website.
- **New Item Detection:** Tracks previously seen items and identifies newly added products.
- **Discord Notifications:** Sends notifications to a specified Discord channel, mentioning a designated role to alert fans.
- **GUI for Testing:** Includes a simple Tkinter GUI to trigger test notifications. 

### Requirements

- Python 3.7+
- `discord.py`
- `requests`
- `beautifulsoup4`
- `tkinter`

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/CBarrettPortfolio/shopping-site-web-scraper
   ```
2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

### Configuration

1. **Discord Bot Setup:**
   - Create a Discord bot and obtain its token.
   - Create a Discord channel for the notifications.
   - (Optional) Create a Discord role to mention in the notifications.
2. **Code Modifications:**
   - Open the `main.py` file.
   - Replace the placeholder values (`0`) for `channel_id` and `role_id` with your actual Discord channel and role IDs.
   - Replace `'YOUR_DISCORD_BOT_TOKEN'` with your Discord bot token.
   - **Important:** Store your bot token securely and never commit it to version control. Consider using environment variables for this purpose.

### Usage

1. Run the script:
   ```bash
   python main.py
   ```
2. The script will connect to Discord and start monitoring the A7X merchandise website.
3. When new items are detected, a notification will be sent to your configured Discord channel.

### Disclaimer

This project is intended for educational purposes and personal use only. Web scraping can be against the terms of service of some websites. Use this script responsibly and at your own risk.
