import time
import requests
from bs4 import BeautifulSoup
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Set up undetected ChromeDriver
driver = uc.Chrome()

# Base URL of the news portal
base_url = 'https://ekantipur.com/'

# Fetch the page content
response = requests.get(base_url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find all news titles, descriptions, and links
news_items = soup.find_all('article')

trending_news = None

# Get the first news article as trending (or apply custom logic)
for news in news_items:
    title = news.find('h2').text if news.find('h2') else "No title"
    description = news.find('p').text if news.find('p') else "No description"
    link = news.find('a')['href'] if news.find('a') else None
    if link and not link.startswith('http'):
        link = base_url + link

    if link:
        news_response = requests.get(link)
        news_soup = BeautifulSoup(news_response.content, 'html.parser')
        date = news_soup.find(
            'span', class_='detail-date').text if news_soup.find('span', 'detail-date') else "No date"

        trending_news = {
            'title': title,
            'description': description,
            'link': link,
            'date': date
        }
        break


def twitter_login():
    try:
        driver.get('https://x.com/login')
        username_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, 'text')))
        username_input.send_keys('BellaSmith61635')
        username_input.send_keys(Keys.RETURN)
        time.sleep(2)

        password_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, 'password')))
        password_input.send_keys('bellasmithh@2024!')
        password_input.send_keys(Keys.RETURN)
        time.sleep(5)

    except Exception as e:
        print(f"An error occurred during login: {e}")


try:
    twitter_login()

    if trending_news:
        driver.get('https://x.com/home')
        tweet_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@aria-label="Tweet"]')))
        tweet_button.click()

        tweet_content = f"Trending News: {trending_news['title']}\n{trending_news['description']}\nRead more: {trending_news['link']}"

        tweet_text_area = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.public-DraftStyleDefault-block')))
        tweet_text_area.click()
        tweet_text_area.send_keys(tweet_content)

        tweet_submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//div[@data-testid="tweetButtonInline"]')))
        tweet_submit_button.click()

        print("Tweet posted successfully!")
    else:
        print("No trending news found.")

except Exception as e:
    print(f"An error occurred during tweeting: {e}")

finally:
    driver.quit()
