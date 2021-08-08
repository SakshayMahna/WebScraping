from bs4 import BeautifulSoup
import requests
import csv

# Initialize beautiful soup
source = requests.get('https://www.geeksforgeeks.org/fundamentals-of-algorithms/').text
soup = BeautifulSoup(source, 'lxml')

# Initialize csv file
csv_file = open('gfg_algorithms.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Heading', 'Title', 'Link'])

# Retreive headings and links
heading_tags = soup.find_all('p', style='text-align:center')
link_tags = soup.find_all('ol')

for link in link_tags:
    link_list = link.find_all('li')
    subheading = link.find_previous('p').text
    
    if subheading[-1] == ':':
        subheading = subheading[:-1]

    print(subheading)
    print('-' * 10)

    for li in link_list:
        print(li.a.text)
        csv_writer.writerow([subheading, li.a.text, li.a['href']])

    print()

# for heading in heading_tags:
#     heading_text = heading.strong.text

#     if heading_text[-1] == ":":
#         heading_text = heading_text[:-1]
    
#     print(heading_text)