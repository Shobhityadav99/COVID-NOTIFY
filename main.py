from plyer import notification
import requests
from bs4 import BeautifulSoup

def notifyMe(title,message):
    notification.notify(
        title=title,
        message =message,
        app_icon="F:\PythonProjects\COVID NOTIFY\icon.ico",
        timeout=10
    )

def getData(url):
    return requests.get(url).text

if __name__ == '__main__':
    notifyMe("Shobhit","What is this")
    myHtml= getData("https://www.mohfw.gov.in/")
    soup = BeautifulSoup(myHtml, 'html.parser')
    print(soup.prettify())