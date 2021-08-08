# Project on Web Scraping
This project consists of 3 different web scraping techniques.

## Requirements and Installation
The project has been implemented and run on Windows 10 machine with Python 3.8.8. The requirements can be installed by:

```bash
pip install -r requirements.txt
```

## Beautiful Soup
`WebScraping-BeautifulSoup` contains web scraping using BeautifulSoup. Articles on Algorithms present on GeeksForGeeks have been scraped.

Run the program using:

```bash
python main.py
```

## Scrapy
`WebScraping-Scrapy` contains web scraping using Scrapy. There are 2 different scraping projects in this.

### Video Games on Flipkart
Run the program using:

```bash
spider crawl flipkart_games
```

### Watches on Amazon
Run the program using:

```bash
spider crawl amazon_watches
```

**For scraping through Amazon, User-Agents and Proxy methods have also been used**

## Selenium
`WebScraping-Selenium` contains web scraping using Selenium. Videos present on a Gaming Channel (Insym) have been scraped.

Run the program using:

```bash
python main.py
```