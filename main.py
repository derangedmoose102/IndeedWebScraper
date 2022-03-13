import requests
from bs4 import BeautifulSoup

# search for an attribute
# a=soup.findAll(class_="companyName")
position, location = 'help desk', '32256'
y = requests.get('https://www.indeed.com/jobs?q={}&l={}&sort=date='.format(position, location))
soup = BeautifulSoup(y.text, 'html.parser')

beacons = soup.find_all('div', {"class": "job_seen_beacon"})

for ii in beacons:

    jobpage = "https://www.indeed.com" + ii.parent.parent.parent.parent.attrs.get("href")

    j = ii.find('tbody')  # calling the table body to go inside of
    a = j.find('tr')  # going inside the table
    # job title
    for n in a.find_all('h2', {'class': 'jobTitle jobTitle-color-purple jobTitle-newJob'}):
        job_title = n.find_all('span')[1].get_text()

    # company name
    other = a.find('div', {'class': 'heading6 company_location tapItem-gutter companyInfo'})
    pr = other.find('span')
    company = pr.get_text()
    # salary
    if a.find('div', {'class': 'metadata salary-snippet-container'}):

        salary = (a.find('div', {'class': 'metadata salary-snippet-container'}).get_text())
    else:
        salary = 0
    # location
    location = (a.find('div', {'class': 'companyLocation'}).get_text())
    # rating
    rating = a.find('span', {'class': 'ratingNumber'})
    # print all results
    if salary != 0 and rating:
        print(" ")
        print(jobpage)
        print(job_title)
        print(company)
        print(rating)
        print(salary)
        print(location)