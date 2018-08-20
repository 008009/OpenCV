import requests
import urllib.request as ur
from bs4 import BeautifulSoup
import os

# crawl image from douban.com
# url = "https://movie.douban.com/celebrity/1001373/photos/"
# r = requests.get(url)
# html_content = r.text

# soup = BeautifulSoup(html_content,"html.parser")

# div = soup.find_all('div', class_ = 'cover')
# divs = BeautifulSoup(str(div), "html.parser")

# images = divs.find_all('img')

# imagelist = []
# for image in images:
# 	imagelist.append(image['src'])

# crawl image from http://www.happyjuzi.com/star-ku-4-0-0-0-0-0-0/
#initUrl = "http://www.happyjuzi.com/star-picture-45/"  # TaylorSwift
#initUrl = "http://www.happyjuzi.com/star-picture-84/"  # EmmaWatson
#initUrl = "http://www.happyjuzi.com/star-picture-1435/" #SatomiIshihara
#initUrl = "http://www.happyjuzi.com/star-picture-21/" #JenniferLawrence
#initUrl = "http://www.happyjuzi.com/star-picture-1306/" #JasonStatham
initUrl = "http://www.happyjuzi.com/star-picture-7795/" #DwayneJohnson
urlList = []
imagelist = []
count = 1
totalPage = BeautifulSoup(requests.get(initUrl).text, "html.parser")
MaxPageNumber = totalPage.find_all('a', class_= 'num')
MPN = 1 + (len(MaxPageNumber))

while(count <= MPN):
	url = initUrl + "p"+ str(count) + ".html"
	count+= 1 
	urlList.append(url)

for url in urlList:
	r = requests.get(url)
	html_content = r.text
	soup = BeautifulSoup(html_content, "html.parser")
	divs = soup.find_all('div', class_= 'star-pic load-img')
	for image in divs:
		#print(image['data-src'])
		imagelist.append(image['data-src'])

num = 0
position = '/Users/carl0809/OpenCV/facedetection/src/DwayneJohnson/'
for img in imagelist:
    img = requests.get(img)
    if not os.path.exists(position):
        os.makedirs(position)
        print('path created')
    with open(position + str(num) + '.png', 'wb') as f:
    	f.write(img.content)
    	f.close()
    num = num + 1