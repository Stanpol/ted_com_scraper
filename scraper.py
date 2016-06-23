from bs4 import BeautifulSoup
import scraperwiki

print("Scraping the latest page")
html = scraperwiki.scrape("http://www.ted.com/talks/quick-list?page=1")
soup = BeautifulSoup(html, 'lxml')

talks = soup.find_all("div", attrs={"class": "col xs-12 quick-list__container-row"})
for t in talks:
	talk = t.find_all('a')
	talk_url = talk[0]['href']
	talk_name = talk[0].text
	event_url = talk[1]['href']
	event_name = talk[1].text
	try:
		link_low = talk[2]['href']
		link_medium = talk[3]['href']
		link_high = talk[4]['href']
	except:
		print("! No links available")
		link_low = "no link"
		link_medium = "no link"
		link_high = "no link"
	talk = t.find_all("div", attrs={"class": "col-xs-1"})
	date = talk[0].text
	time = talk[1].text
	print(talk_name.encode('utf-8'))

	scraperwiki.sqlite.save(unique_keys=['talk_name'], data={"talk_name": talk_name, "talk_url": talk_url, "event_url": event_url, "event_name": event_name, "link_low": link_low, "link_medium": link_medium, "link_high": link_high, "date": date, "time": time})


# # Old talks:
# # for i in xrange(2,64):
# # 	print("=============================Page: "+str(i))
# # 	html = scraperwiki.scrape("http://www.ted.com/talks/quick-list?page="+str(i))
# # 	soup = BeautifulSoup(html, 'lxml')
# # 
# # 	talks = soup.find_all("div", attrs={"class": "col xs-12 quick-list__container-row"})
# # 	for t in talks:
# # 		talk = t.find_all('a')
# # 		talk_url = talk[0]['href']
# # 		talk_name = talk[0].text
# # 		event_url = talk[1]['href']
# # 		event_name = talk[1].text
# # 		try:
# # 			link_low = talk[2]['href']
# # 			link_medium = talk[3]['href']
# # 			link_high = talk[4]['href']
# # 		except:
# # 			print("! No links available")
# # 			link_low = "no link"
# # 			link_medium = "no link"
# # 			link_high = "no link"
# # 		talk = t.find_all("div", attrs={"class": "col-xs-1"})
# # 		date = talk[0].text
# # 		time = talk[1].text
# # 		print(talk_name.encode('utf-8'))
# # 
# # 		scraperwiki.sqlite.save(unique_keys=['talk_name'], data={"talk_name": talk_name, "talk_url": talk_url, "event_url": event_url, "event_name": event_name, "link_low": link_low, "link_medium": link_medium, "link_high": link_high, "date": date, "time": time})