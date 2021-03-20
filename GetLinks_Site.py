import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import collections
import os

print("Starting...")
print("Opening Window...")
driver = webdriver.Chrome()

url_dict = {"VideoLinks_1":"https://site.com/page/with/video/links"}

key = "VideoLinks_1"
url = url_dict[key]

driver.get(url)

print("Scrolling down...")
ht=driver.execute_script("return document.documentElement.scrollHeight;")
while True:
    prev_ht=driver.execute_script("return document.documentElement.scrollHeight;")
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    time.sleep(2)
    ht=driver.execute_script("return document.documentElement.scrollHeight;")
    if prev_ht==ht:
        break

print("Finding the urls...")
# Change class="video-link" with whatever your site has
links = driver.find_elements_by_xpath('//*[@class="video-link"]')

print("Writing the urls...")

already = []
file_name = key + ".txt"

# Check if a text file already exists and add urls to it
if os.path.isfile(file_name):
    text_file_r = open(file_name, "r")
    
    for x in text_file_r:
        already.append(x.strip('\n'))
    
    text_file_r.close()
    
    text_file = open(file_name, "a")
    n=0
    for link in links:
        # You might have to change "href" (for example to "src")
        url = link.get_attribute("href")
        if url not in already:
            text_file.write("%s\n" % url)
            n+=1
    
    text_file.close()
    
    print("---------------------------------------------------")
    print("There are %d videos in total" % len(links))
    print("There are", n, "new urls")
    print("---------------------------------------------------")

# Create a new  text file to add the urls
else:
    print('Creating file:', file_name)
    text_file = open(file_name, "w")
    
    n=0
    for link in links:
        # You might have to change "href" (for example to "src")
        url = link.get_attribute("href")
        if url not in already:
            text_file.write("%s\n" % url)
            n+=1
    
    text_file.close()
    
    print("---------------------------------------------------")
    print("There are %d videos in total" % len(links))
    print("There are", n, "written")
    print("---------------------------------------------------")

driver.quit()

print("Finished !!!")
