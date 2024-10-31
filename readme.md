# WhatsApp Automation Bots

This repository contains two Python-based WhatsApp automation bots created with Selenium. The first bot, **Single MSG to All Bot**, sends a "Hello!" message to all recent WhatsApp contacts. The second bot, **Birthday Bot**, monitors incoming messages and sends a "thanks" reply to anyone who wishes you a "Happy Birthday." In group chats, it replies directly to specific messages as a quoted response.

## Prerequisites

To use these bots, you'll need:
- **Python 3.x** installed on your system
- **Chrome WebDriver** compatible with your version of Chrome ([Download WebDriver here](https://chromedriver.chromium.org/downloads))
- **Selenium** package for Python

Install Selenium by running:
```bash 
pip install selenium
