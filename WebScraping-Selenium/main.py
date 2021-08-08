from selenium import webdriver
import time
import csv

# Initialize csv file
csv_file = open('insym_videos.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Title', 'Link', 'Views', 'Posted On'])

# Define webdriver
driver = webdriver.Edge(executable_path = 'webdriver/msedgedriver.exe')

# Get URL
url = 'https://www.youtube.com/c/Insym/videos'
driver.get(url)

# Recover all the content and then load it
scrollHeight = driver.execute_script("return document.documentElement.scrollHeight")
zero_count = 0
# While scrollHeight variable is not changing
while True:
    # Zero Count is 2 at the start and at the end
    if zero_count == 2:
        break

    prev_scrollHeight = scrollHeight
    driver.execute_script(f"window.scrollTo(0, document.documentElement.scrollHeight);")
    scrollHeight = driver.execute_script("return document.documentElement.scrollHeight")

    # Check change of variable
    if prev_scrollHeight - scrollHeight == 0:
        zero_count += 1

    # Wait to load any lazy loaded images
    time.sleep(1)

# Get video elements
videos = driver.find_elements_by_class_name("style-scope ytd-grid-video-renderer")

# Loop and get all the videos
for video in videos:
    title = video.find_element_by_xpath('.//*[@id="video-title"]').text
    link = video.find_element_by_xpath('.//*[@id="video-title"]').get_attribute('href')
    views = video.find_element_by_xpath('.//*[@id="metadata-line"]/span[1]').text
    posted = video.find_element_by_xpath('.//*[@id="metadata-line"]/span[2]').text

    print(title)
    print('---')
    print(f'{link}\t{views}\t{posted}')
    print()

    csv_writer.writerow([str(title), str(link), str(views), str(posted)])