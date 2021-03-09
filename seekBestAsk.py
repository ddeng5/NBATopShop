import sys
import webbrowser

from selenium import webdriver


def removeHighestPrice(dictValues):
    highestPrice = 0
    dictKey = 0
    for key, value in dictValues.items():
        if value > highestPrice:
            highestPrice = value
            dictKey = key
    if (highestPrice != 0):
        dictValues.pop(dictKey)

numberOfPricesToShow = sys.argv[1]
cheapestListOrdered = {}

driver = webdriver.Chrome("C:/bin/chromedriver")
content = driver.page_source

print("Opening link: %s" % sys.argv[2])
driver.get(sys.argv[2])

priceList = driver.find_element_by_id("moment-detailed-serialNumber")

options = [x for x in priceList.find_elements_by_tag_name("option")]

for element in options[1:]:
    element = element.text
    details = element.split( )
    serialNumber = details[0]

    #cleanup price data to remove dollar sign
    price = details[2]
    price = price[1:]
    price = price.replace(",", "")

    if len(cheapestListOrdered) < int(numberOfPricesToShow):
        if (len(cheapestListOrdered) == 0):
            cheapestListOrdered[serialNumber] = float(price)
            print("added price: ", price)
        else:
            for num, value in cheapestListOrdered.items():
                print(cheapestListOrdered)
                if (float(price) < float(value)):
                    print("num: %", num)
                    print("priceeee: %", price)
                    cheapestListOrdered[serialNumber] = float(price)
                    print(cheapestListOrdered)
                    break
    elif len(cheapestListOrdered) == int(numberOfPricesToShow):
        print("Trying serial number: ", serialNumber)
        for num, value in cheapestListOrdered.items():
            if (float(price) < float(value)):
                removeHighestPrice(cheapestListOrdered)
                cheapestListOrdered[serialNumber] = float(price)
                break
print(cheapestListOrdered)
            



