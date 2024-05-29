import requests
from bs4 import BeautifulSoup # html kodlarını kendi içinde aramamıza yarıyor

url = "https://stackoverflow.com/questions/tagged/python-requests"

sayac = 0
for i in range(1,11):
	url2 = "https://stackoverflow.com/questions/tagged/python-requests?tab=newest&page="+str(i)+"&pagesize=50"

	response = requests.get(url2)

	parser = BeautifulSoup(response.text,'html.parser') # beautifulsoup kütüphanesine html kodlarını tanıtıyoruz

	questions = parser.find_all("div",{"class":"s-post-summary"}) # html kodununda süslü parentezin içindeki classa sahip divleri getir 

	for q in questions:
		#print(q)
		title = q.find('h3',{"class":"s-post-summary--content-title"})
		print(title.text.strip())
		content = q.find('div',{"class":"s-post-summary--content-excerpt"})
		print(content.text.strip())
		time = q.find('span',{"class":"relativetime"})
		print(time['title'])
		
		sayac = sayac+1
		print("content count =",str(sayac))
		print("----------------------")
	
