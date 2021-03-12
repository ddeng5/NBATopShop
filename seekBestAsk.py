import sys
import webbrowser

from selenium import webdriver


def removeHighestPrice(dictValues):
    highestPrice = 0
    for value, serial in dictValues.items():
        if float(value) > float(highestPrice):
            highestPrice = value
    if (highestPrice != 0):
        dictValues.pop(highestPrice)

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
    serialNumber = serialNumber[1:]

    #cleanup price data to remove dollar sign
    price = details[2]
    price = price[1:]
    price = price.replace(",", "")

    if len(cheapestListOrdered) < int(numberOfPricesToShow):
        if (len(cheapestListOrdered) == 0):
            cheapestListOrdered[price] = serialNumber
        else:
            for value, serial in cheapestListOrdered.items():
                if (float(price) == float(value)):
                    if (int(serialNumber) < int(serial)):
                        cheapestListOrdered[price] = serialNumber
                        break
                else:
                    cheapestListOrdered[price] = serialNumber
                    break
    elif len(cheapestListOrdered) == int(numberOfPricesToShow):
        print("Trying serial number: ", serialNumber)
        for value, serial in cheapestListOrdered.items():
            if (float(price) < float(value)):
                cheapestListOrdered[price] = serialNumber
                removeHighestPrice(cheapestListOrdered)
                break
            elif (float(price) == float(value)):
                if (int(serialNumber) < int(serial)):
                    cheapestListOrdered[price] = serialNumber
                    break



    # if len(cheapestListOrdered) < int(numberOfPricesToShow):
    #     if (len(cheapestListOrdered) == 0):
    #         cheapestListOrdered[serialNumber] = float(price)
    #         print("added price: ", price)
    #     else:
    #         for num, value in cheapestListOrdered.items():
    #             print(cheapestListOrdered)
    #             if (float(price) < float(value)):
    #                 print("num: %", num)
    #                 print("priceeee: %", price)
    #                 cheapestListOrdered[serialNumber] = float(price)
    #                 print(cheapestListOrdered)
    #                 break
    # elif len(cheapestListOrdered) == int(numberOfPricesToShow):
    #     print("Trying serial number: ", serialNumber)
    #     for num, value in cheapestListOrdered.items():
    #         if (float(price) < float(value)):
    #             removeHighestPrice(cheapestListOrdered)
    #             cheapestListOrdered[serialNumber] = float(price)
    #             break

for value, serial in sorted(cheapestListOrdered.items()):
    print("Price: {} --- Serial Number: {}".format(value, serial))
            



