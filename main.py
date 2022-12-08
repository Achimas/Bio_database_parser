import requests
from openpyxl import Workbook
from bs4 import BeautifulSoup as bs

def open_excel(excel_name):
	wb = Workbook(excel_name)
	ws = wb.active
	all_names = []
	for row in ws.iter_rows(values_only=True):  
		??? all_names.append(row['1'])
	new_filename = f'v2_{excel_name}'
	wb.save(filename = new_filename)
	return all_names

def search_object(all_names):
	site_url = "..."
	r = request.get(site_url)
	with open(r) as r:
		soup = BeautifulSoup(r, 'html.parser')
	for name in all_names:
		link = soup.find(name)

def get_parents(link):
	parents_list = []
	parent_now = ''
	while parent_now == 'r = request.get(link)
	
