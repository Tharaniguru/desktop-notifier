from win10toast import ToastNotifier
import time
import subprocess
import requests
from bs4 import BeautifulSoup

def get_headline():
    source = requests.get('https://www.technewsworld.com/section/tech-blog').text
    soup = BeautifulSoup(source, 'lxml')
    div = soup.find('div',class_='catogory-pic')
    headline = div.find('h2', class_='heading-title').text
    url=div.find('a')['href']
    return headline,url

def notify(title, message, duration, url):
    
    toaster = ToastNotifier()
    toaster.show_toast(

        title,
        message,
        duration=duration,  # duration in seconds
        threaded=True
    )
    subprocess.Popen(['explorer', url], shell=True)

if __name__ == "__main__": 
    while True:
        headline,url = get_headline()
        # print(headline)
        notify("Tech News", headline, 10,url)
        time.sleep(1800)  # notify every 30 minutes
