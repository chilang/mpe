stocks = ['NASDAQ:AAPL',
  'NASDAQ:GOOG',
  'NASDAQ:MSFT',
  'NASDAQ:FB',
  'NASDAQ:AMZN',
  'NASDAQ:EBAY',
  'NYSE:LNKD',
  'NASDAQ:ZNGA']

def fetch(url):
  import urllib
  from bs4 import BeautifulSoup
  html = urllib.urlopen(url).read()
  return BeautifulSoup(html)

def market_cap(soup):
	return soup.find('td', attrs={'data-snapfield': 'market_cap'}).find_next_sibling().text.strip('\n')

def employees(soup):
  return soup.find_all('td', text='Employees\n')[0].next_sibling.text.strip('\n')

if __name__ == '__main__':
	print '\t'.join(['stock', 'mkt cap', 'emp', '$m per emp'])
	for s in stocks:
		page = fetch('http://www.google.com/finance?q=%s' % s)
		cap = market_cap(page)
		emp = employees(page)
		mil_per_emp = float(cap.strip('B')) * 1000 / int(emp.replace(',', ''))
		print '\t'.join([s.split(':')[1], cap, emp, '%.2f' % mil_per_emp])