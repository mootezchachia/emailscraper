import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Set the URL you want to scrape
url = 'http://www.example.com/'

# Use requests to get the contents of the website
r = requests.get(url)

# Get the text of the contents
html_content = r.text

# Use BeautifulSoup to parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Find all 'a' elements that have an 'href' attribute
links = soup.find_all('a', {'href': True})

# Iterate over the found links and extract the email addresses
emails = []
for link in links:
    email = link['href'].split(':')[1]
    emails.append(email)

# Open a file for writing in 'w' mode
file = open('emails.txt', 'w')

# Write the email addresses to the file, one per line
for email in emails:
    file.write(email + '\n')

# Close the file
file.close()

# Set your email address and password
fromaddr = 'your_email@example.com'
password = 'your_password'

# Set the recipient and email subject
toaddr = 'recipient@example.com'
subject = 'Scraped Email Addresses'

# Create a MIMEMultipart object
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = subject

# Open the text file and attach its content to the email
with open('emails.txt', 'r') as file:
    email_text = file.read()

msg.attach(MIMEText(email_text, 'plain'))

# Connect to the email server and send the email
server = smtplib.SMTP('smtp.example.com', 587)
server.starttls()
server.login(fromaddr, password)
server.send_message(msg)
server.quit()
