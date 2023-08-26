import requests
import re

def img_downloader(imgurl):
   pattern1 = r'/(\d+-\w+\.jpg)$'
   pattern2= r'/([^/]+\.jpg)$'

   response=requests.get(imgurl)
   if(response.status_code==200):
    imgname=''
    if (re.search(pattern2,imgurl)!=None):
        imgname=re.search(pattern2,imgurl).group(1)
    else:
        imgname=re.search(pattern1,imgurl).group(1)

    print(imgname)
    fp=open('img/'+imgname,'wb')
    fp.write(response.content)
    fp.close

def imgid(url):
	r=requests.get(url).text
	test=re.findall(r"src='([^']+)'",r)
	for i in test:
		fullURL="https://www.karavalimunjavu.com/"+i
		img_downloader(fullURL)