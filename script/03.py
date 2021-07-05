from bs4 import BeautifulSoup
from selenium import webdriver
import requests

# DEBUG=True
DEBUG=False

if DEBUG:
	heroku_login_url='http://127.0.0.1:8000/accounts/login/'
	heroku_bd_url="http://127.0.0.1:8000/dballdata/"
else:
	heroku_login_url='https://camera-shop-alert.herokuapp.com/accounts/login/'
	heroku_bd_url="https://camera-shop-alert.herokuapp.com/dballdata/"

heroku_id="qMCm1rZDDb"
heroku_pass="cWixDU3Kvv"

# ------------------------------
# HerokuサイトからDB内容を取得する
# ------------------------------
# Herokuサイト用のselenium
def boot_selenium_heroku():
	chrome_options=webdriver.ChromeOptions()
	chrome_options.add_experimental_option("excludeSwitches",['enable-automation',
																														'enable-logging'])
	chrome_options.add_argument('--headless')  #ヘッドレスモード
	chrome_options.add_argument('--incognito')  #シークレットモード
	chrome_options.add_argument('--no-sandbox')
	chrome_options.add_argument('--single-process')
	chrome_options.add_argument('--disable-gpu')
	chrome_options.add_argument('--disable-dev-shm-usage')
	chrome_options.add_argument('--disable-desktop-notifications')
	chrome_options.add_argument("--disable-extensions")
	chrome_options.add_argument('--ignore-certificate-errors')
	chrome_options.add_argument('--ignore-ssl-errors')
	driver=webdriver.Chrome(options=chrome_options)
	return driver
# HerokuサイトからDBの内容を取得
def get_heroku_db_all_data():
	driver_heroku=boot_selenium_heroku()
	try:
		# サーバがスリープしていると起動に10秒程度必要なので追加
		driver_heroku.set_page_load_timeout(60)
		# ログインページを開いてログイン
		driver_heroku.get(heroku_login_url)
		driver_heroku.execute_script('document.getElementById("id_username").value="%s";'%heroku_id)
		driver_heroku.execute_script('document.getElementById("id_password").value="%s";'%heroku_pass)
		driver_heroku.find_element_by_xpath("//button[@type='submit']").click()
		# DBページからスクレイピング
		driver_heroku.get(heroku_bd_url)
		bs4obj=BeautifulSoup(driver_heroku.page_source,'html.parser')
		try:
			search_query=eval(bs4obj.select_one('span[id="db_all_data_dict"]').text)
		except:
			search_query=''
		line_token=bs4obj.select_one('span[id="line_token"]').text
	finally:
		driver_heroku.quit()
	return line_token,search_query
# HerokuサイトからDBの内容を取得 requests
def get_heroku_db_all_data_requests():
	# https://own-search-and-study.xyz/2017/04/09/djangoで作ったサイトにスクリプトでログインする方/
	session=requests.session()
	session.get(heroku_login_url)
	csrf=session.cookies['csrftoken']
	login_info={"csrfmiddlewaretoken":csrf,
							"username":heroku_id,
							"password":heroku_pass,
							"next":heroku_bd_url}
	response=session.post(heroku_login_url,data=login_info,headers=dict(Referer=heroku_login_url))
	bs4obj=BeautifulSoup(response.text,'html.parser')
	try:
		search_query=eval(bs4obj.select_one('span[id="db_all_data_dict"]').text)
	except:
		search_query=''
	line_token=bs4obj.select_one('span[id="line_token"]').text
	return line_token,search_query

line_token,search_query=get_heroku_db_all_data_requests()
print(line_token)
print(search_query)