from bs4 import BeautifulSoup
import requests
import time

html_text = requests.get('https://uk.indeed.com/jobs?q=software%20engineer&l=United%20Kingdom&vjk=eb24cd41c665bae4').text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find('ul', class_ = 'jobsearch-ResultsList css-0').find_all('li')
time.sleep(1)

for job in jobs:
    company = job.find('a', {'data-tn-element': 'companyName'})
    snippet = job.find('div', class_ = 'attribute_snippet')
    pay = snippet.find_all(text=True, recursive=False)[0] if snippet else ''
    location = job.find('div', class_ = 'companyLocation')
    link = job.find('a', href=True)['href'] if job.find('a', href=True) else ''

    if company:# and snippet and location and location.span:
        print(f'Company Name: {company.text}')
        print(f'Pay: {pay}')
        location_text = location.span.text if location and location.span else ''
        print(f'Location: {location_text}')
        print(f'Link: {link}')
        print('')