from selenium import webdriver
from PIL import Image
#from selenium.webdriver.common.by import By
browser = webdriver.Chrome()
browser.get('https://www.alexa.com/topsites')
the_links = browser.find_elements_by_tag_name("a")
browser.set_page_load_timeout(30)
formatted_links= []
count = 1
for link in the_links:
    if "siteinfo/" in link.get_attribute("href"):
        topsite = link.get_attribute("href")
        topsite = topsite.replace("https://www.alexa.com/siteinfo/", "")
        formatted_links.append(topsite)
for element in formatted_links:
    try:
        browser.get("http://www." + element)
    except:
        print(element + ' took to long')
    else:
        #title = browser.title
        image = '{}.png'.format('rank' + str(count))
        browser.save_screenshot(image)
    count +=1
browser.close()
browser.quit()

