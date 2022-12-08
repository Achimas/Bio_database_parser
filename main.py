import requests
from openpyxl import Workbook
from bs4 import BeautifulSoup as bs

def open_excel(excel_name):
	wb = Workbook(excel_name)
	ws = wb.active
	all_names = []
	for row in ws.iter_rows(values_only=True):  
		all_names.append(row['1'])  # to do
	new_filename = f'v2_{excel_name}'
	wb.save(filename = new_filename)
	return all_names

def search_object(all_names):
	site_url = "..."  # to do
	r = request.get(site_url)  # to do
	with open(r) as r:
		soup = BeautifulSoup(r, 'html.parser')  # to do
	for name in all_names:
		link = soup.find(name)  # to do
		all_parents = get_parents(name, link)

def get_parents(name, link):
	all_parents_list = {}
	parent_name_now = {}
	parent_name_now[name] = link
	while 'pathways' not in parent_name_now:
		if parent_name_now < 2:
			r = request.get(link)  # to do
			soup = BeautifulSoup(r, 'html.parser')  # to do
			links_name = soup.find_all("a", class_='...') #class = '' как-то там называющийся класс-родитель
			links = soup.find_all("a", class_='...') # .get (href) # class = '' как-то там называющийся класс-родитель
			for link in links_name:
				parent_name_now.append(link.text()) # to do
			all_parents_list.append(', '.join(parent_name_now) if len(parent_name_now)>1 else parent_name_now)
			
		else:
			
			
