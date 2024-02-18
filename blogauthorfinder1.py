import requests
import csv
from bs4 import BeautifulSoup

# URL of the website to scrape
url = 'https://www.pythonforbeginners.com/ '

# Send an HTTP request to the website
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Extract the relevant data from the blog posts
blog_posts = soup.find_all('article', class_='post')

# Open a CSV file for writing
csv_file = open('blog_authors.csv', 'a', newline='')
csv_writer = csv.writer(csv_file)

# Write the header row to the CSV file
csv_writer.writerow(['Author Name', 'Author Email', 'Author Profile Link', 'Author Image', 'Blog Logo', 'Blog Name'])

for post in blog_posts:
    # Author name
    author_name = post.find('span', class_='author-name').text

    # Author email
    author_email = post.find('span', class_='author-email').text

    # Author profile link
    author_profile_link = post.find('a', class_='author-profile')['href']

    # Author image
    author_image = post.find('img', class_='author-image')['src']

    # Blog logo
    blog_logo = soup.find('img', class_='blog-logo')['src']

    # Blog name
    blog_name = soup.find('a', class_='blog-name').text

    # Write the extracted data to the CSV file
    csv_writer.writerow([author_name, author_email, author_profile_link, author_image, blog_logo, blog_name])

    # Output the extracted data
    print('Author Name:', author_name)
    print('Author Email:', author_email)
    print('Author Profile Link:', author_profile_link)
    print('Author Image:', author_image)
    print('Blog Logo:', blog_logo)
    print('Blog Name:', blog_name)

# Close the CSV file
csv_file.close()
