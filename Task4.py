import requests
from bs4 import BeautifulSoup

def scrape_news_headlines(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if request was successful
    if response.status_code == 200:
        # Parse HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all headlines
        headlines = soup.find_all('h3', class_='gs-c-promo-heading__title')
        
        # Extract text from headlines
        headlines_text = [headline.get_text() for headline in headlines]
        
        return headlines_text
    else:
        print("Error:", response.status_code)
        return None

def main():
    url = "https://www.bbc.com/news"
    headlines = scrape_news_headlines(url)
    if headlines:
        print("BBC News Headlines:")
        for headline in headlines:
            print("-", headline)

if __name__ == "__main__":
    main()
