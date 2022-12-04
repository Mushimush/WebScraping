from bs4 import BeautifulSoup
import requests

html_text = requests.get(
    'https://www.linkedin.com/jobs/search?keywords=software%2Bengineer&location=Singapore&geoId=102454443&trk=public_jobs_jobs-search-bar_search-submit&currentJobId=3385798079&position=21&pageNum=0').text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all(
    'div', class_='base-search-card__info')
for job in jobs:
    job_desc = job.find('h3', class_='base-search-card__title').text.strip()
    company_name = job.find(
        'h4', class_='base-search-card__subtitle').text.strip()
    date_posted = job.find(
        'time', class_='job-search-card__listdate').text.strip()
    print(f'''
Company Name: {company_name}
Job: {job_desc}
Date Posted: {date_posted}
''')
