# Reddit Scraper Readme

## Overview

This is a simple Python script for scraping Reddit posts from a specific subreddit using the `requests` library to make HTTP requests to Reddit's website. This README provides instructions on how to use the script effectively.

## Prerequisites

Before running the script, make sure you have the following prerequisites installed on your system:

- Python 3.x
- `requests` library
  - You can install it using pip: `pip install requests`

## Getting Started

1. Clone or download this repository to your local machine.

2. Customize Your Scraper:
   - Open `main.py` in a text editor of your choice.
   - Modify the `subreddit_url` variable to the URL of the subreddit you want to scrape.

3. Run the Script:
   - Open a terminal or command prompt in the project folder.
   - Run the script by executing the following command: `python scraper.py`
   - The script will fetch the HTML content of the subreddit's page and parse it to extract posts.

4. Results:
   - The scraped posts will be displayed in the terminal or saved to a local csv file name `data.csv` file, depending on how you configure the script.

## Note

- Please use this script responsibly and respect Reddit's terms of service and rules.
- Be aware that scraping Reddit's website directly may be subject to rate limiting or IP blocking if done excessively.

Happy scraping! If you encounter any issues or have questions, feel free to open an issue or contact the author.

---

**Disclaimer:** This script is for educational purposes only and should be used in accordance with Reddit's terms of service and rules. The author is not responsible for any misuse or violation of Reddit's policies.