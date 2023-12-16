from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
import re, json
app = Flask(__name__)

def scrapeSavant():
    url = "https://baseballsavant.mlb.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    i = 0
    headlines =[]
    descriptions = []
    links = []
    images = []
    for news in soup.find_all(class_="article"):
        headline = news.find(class_="cms-headline").text
        summary = news.find(class_="cms-summary").text
        link = news.find("a")['href']
        image = news.find('img')
        image = image.attrs['src']   
        headlines.append(headline)
        descriptions.append(summary)
        links.append(link)
        images.append(image)
        i += 1
    savantDict = {"headlines": headlines, "descriptions": descriptions, "links":links, "images":images}
        #print(url_ext)
    #print(headlines)
    #print(i)
    return savantDict
def scrapeRoto():
    url = "https://www.rotoballer.com/mlb"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    rotoHeadlines = []
    #rotoHeadlines = soup.prettify()
    #print(rotoHeadlines)
    i = 0
# for news in soup.find_all(class_=["itemContent", "title", "lazyload"])[:5]:
#     headline = news.find("span")
#     link = news.find('a')
#     print(news.prettify())
#     print(headline)
#     image = news.find('img')
#     #url_ext = image.attrs['src']
#     # with open(f"./images/headline{i}.png", "wb") as file:
#     #     image = httpx.get(url_ext)
#     #     # Save the image binary data into the file
#     #     file.write(image.content)
#     i += 1
#     #rotoHeadlines.append(headline.text)
#     rotoHeadlines.append([image,link,headline])
#     print(rotoHeadlines)
def scrapeFantasyPros():
    url = "https://www.fantasypros.com/mlb/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    fantasyprosHeadlines = []
    f = soup.find_all(["script","var news"])[30:]
    s = []
    # for text in f:
    #     t = str(text)
    #     if "var news = " in t:
    #         #print()
    #         found = t.find("var news = ")
    #         sub = t[found :found+10000]
    #         print(sub)
    #         res = json.loads(sub)
    #         print(res)
        #m = re.search(r'var news = ({.*})', text)
        # if m:
        #     break;
    i = 0
    for headline in soup.find_all(class_="article"):
        image = headline.find('img')
        url_ext = image.attrs['src']

        with open(f"./images/headline{i}.png", "wb") as file:
            image = httpx.get(url_ext)
            # Save the image binary data into the file
            file.write(image.content)
        i += 1
        headlinfantasyprosHeadlineses.append(headline.text)
    return fantasyprosHeadlines

def scrapeFanGraphs():
    url = "https://www.fangraphs.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    fangraphsDict = {}
    i = 0
    descriptionLinks = soup.find_all(class_="blog-headline_blog-headline__excerpt___99oD")
    images = soup.find_all("img")
    titles = []
    imageLinks = []
    descriptions = []
    for image in images:
        if image.has_attr("title"):
            descriptions.append(descriptionLinks[i].text)
            titles.append(image['title'])
            imageLinks.append(image['src'])
            i += 1
    #{"headline": titles, "summary": descriptions, "link":link, "images":imageLinks}
    # print(descriptions[:3])
    # print(titles[:3])
    # print(imageLinks[:3])

    return None

def scrapeAthletic():
    url = "https://theathletic.com/mlb/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    athleticHeadlines = []
    i = 0
    # print(soup.prettify())
    headlines = soup.find_all(class_="sc-b636adb0-0 bGJrNO")
    descriptions = soup.find_all(class_="sc-6ba2ebb1-0 joBzxk")
    # for headline in soup.find_all(class_="sc-84353c08-0 bdUdHw container"):
    #     # image = headline.find('img')
    #     # url_ext = image.attrs['src']
    #     print(headline.prettify())
    #     # with open(f"./images/headline{i}.png", "wb") as file:
    #     #     image = httpx.get(url_ext)
    #     #     # Save the image binary data into the file
    #     #     file.write(image.content)
    #     i += 1
    #     athleticHeadlines.append(headline.text)
    # return athleticHeadlines
@app.route("/")
def home():
    savantDict = scrapeSavant()
    # athleticHeadlines = scrapeAthletic()
    # fangraphsHeadlines = scrapeFanGraphs()
    # fantasyprosHeadlines = scrapeFantasyPros()
    # rotoHeadlines = scrapeRoto()
    #images = savantDict['image']
    #print(images)
    return render_template("index.html", d = savantDict)
if __name__ == "__main__":
    app.run(debug=True, port = 8000)
