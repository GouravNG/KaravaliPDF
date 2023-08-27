import requests
import re
import os
import img2pdf
from configs import *

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
                
def pdfMaker():
	dirname = "img"
	imgs = []
	for fname in os.listdir(dirname):
		if not fname.endswith(".jpg"):
			continue
		path = os.path.join(dirname, fname)
		print(path)
		# if os.path.isdir(path):
		# 	continue
		imgs.append(path)

	with open("pdf/name.pdf","wb") as f:
		f.write(img2pdf.convert(imgs))
		
def botsend():
	bot_token = api_key
	chat_id = '758744186' 
	file_path = 'pdf/name.pdf'

	with open(file_path, 'rb') as pdf_file:
		pdf_content = pdf_file.read()

	url = f'https://api.telegram.org/bot{bot_token}/sendDocument'

	data = {
		'chat_id': chat_id,
	}

	files = {
		'document': ('document.pdf', pdf_content)
	}

	response = requests.post(url, data=data, files=files)

	if response.status_code == 200:
		print('PDF sent successfully!')
	else:
		print('Failed to send PDF.')
		print(response.text)