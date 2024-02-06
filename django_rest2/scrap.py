import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    # Send an HTTP request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page using Beautiful Soup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract data based on the HTML structure of the webpage
        # Modify the following lines based on the structure of the target webpage
        # For example, if you want to extract all the links on the page:
        links = soup.find_all('a')
        for link in links:
            print(link.get('href'))

        # If you want to extract text from paragraphs:
        paragraphs = soup.find_all('p')
        for paragraph in paragraphs:
            print(paragraph.text)

    else:
        print(f"Failed to retrieve the webpage. Status Code: {response.status_code}")

# Example usage
url_to_scrape = 'https://banglarkobita.com/topic/view/b/5'
scrape_website(url_to_scrape)
