

import time

from bs4 import BeautifulSoup
import requests

print("Enter an unfamiliar skill")
unfamiliar_skill = input('>')
print(f'Filtering out {unfamiliar_skill}')

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    posts = soup.find_all('li', class_= 'clearfix job-bx wht-shd-bx')
    for index,post in enumerate(posts):
        time_posted = post.find('span',class_='sim-posted').span.text
        if('few'in time_posted):

            comp_name=post.find('h3',class_='joblist-comp-name').text.replace(' ','')
            skills = post.find('span',class_='srp-skills').text.replace(' ','')
            link = post.header.h2.a['href']
            #link= post.find('header',class_='clearfix').h2.a['href']
            if(unfamiliar_skill not in skills):

                with open(f'posts/{index}.txt', 'w') as f:

                    f.write(f"Company Name: {comp_name.strip()}\n")
                    f.write(f"Required skills: {skills.strip()}\n")
                    f.write(f"Link: {link}\n")
                    print(f'file {index} saved')

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)

