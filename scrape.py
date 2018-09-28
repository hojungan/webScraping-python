from bs4 import BeautifulSoup
import requests
from csv import writer

# GET request to the URL
response = requests.get('https://hojungan.blogspot.com/')

# Parse the html of the response
soup = BeautifulSoup(response.text, 'html.parser')

# Get all the posts
posts = soup.select('div.post-outer')

with open('posts.csv', 'w') as csv_file:
    csv_writer = writer(csv_file, lineterminator='\n')
    headers = ['Title', 'Link', 'Date']
    csv_writer.writerow(headers)

    for post in posts:
        postTitle = post.find(class_='post-title').find('a').get_text().replace('\n', '')
        postLink = post.find(class_='post-title').find('a')['href'].replace('\n', '')
        postDate = post.find(class_='published').get_text().replace('\n', '').replace(',', ' ')
        csv_writer.writerow([postTitle, postLink, postDate])
