import sys
import webbrowser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Data class to be passed to db
class salesData():
    def __init__(self, player_name, type_of_play, series_name, buyer, price, serial_number, set_number, date_time):
        self.buyer = buyer
        self.price = price
        self.serial_number = serial_number
        self.set_number = set_number
        self.date_time = date_time
    
    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)


def get_sales_data_from_table(link_to_moment):
    # set headless browser
    options = Options()
    options.headless = True

    # start chrome driver and open link
    driver = webdriver.Chrome("C:/bin/chromedriver", chrome_options=options)
    print("Opening link: %s" % link_to_moment)
    driver.get(link_to_moment)

    # grab details from moment header
    player_name = driver.find_element_by_xpath('/html/body/div[1]/div[2]/main/div[3]/div/div[2]/h1')
    type_of_play = driver.find_element_by_xpath('/html/body/div[1]/div[2]/main/div[3]/div/div[2]/h2')
    series_name = driver.find_element_by_xpath('/html/body/div[1]/div[2]/main/div[3]/div/div[2]/a/div')

    print('Player Name: ', player_name.text)
    print('Type of Play: ', type_of_play.text)
    print('Series Name: ', series_name.text)

    past_sales_table = driver.find_element_by_xpath('/html/body/div[1]/div[2]/main/div[4]/details[4]/div/div/div/table')
    # loop through the table of recent sales history starting at the 4th transaction (first 3 are always top 3 sales)

    for row in past_sales_table.find_elements_by_css_selector('tr')[4:]:
        data = row.find_elements_by_tag_name('td')
        obj = salesData(player_name, type_of_play, series_name, data[1].text,data[2].text,data[3].text,data[4].text,data[5].text)
        print(obj)
    # store this data obj to our db ----------- TO-DO

# get_sales_data_from_table(sys.argv[1])


def grab_data_from_marketplace(link_to_marketplace):
    # set headless browser
    # options = Options()
    # options.headless = True

    # start chrome driver and open link
    # driver = webdriver.Chrome("C:/bin/chromedriver", chrome_options=options)
    driver = webdriver.Chrome("C:/bin/chromedriver")
    print("Opening link: %s" % link_to_marketplace)
    driver.get(link_to_marketplace)
    list_of_hrefs = []

    moments_div = driver.find_elements_by_xpath('/html/body/div[1]/div[2]/main/div[3]/div/div/div[3]/div/div[1]/div')
    for moments in moments_div:
        # moment_link = moments.find
        # link = moments.getAttribute("href")
        elements = moments.find_elements_by_tag_name("a")
        for el in elements:
            list_of_hrefs.append(el.get_attribute("href"))
    
    print(list_of_hrefs)


grab_data_from_marketplace("https://www.nbatopshot.com/search")