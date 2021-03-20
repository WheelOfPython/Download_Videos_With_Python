import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import collections
import os

def Clear_Empty_Lines(text):
    # Read lines as a list
    fh = open(text, "r")
    lines = fh.readlines()
    fh.close()
    
    # Clear empty lines
    lines = filter(lambda x: not x.isspace(), lines)
    
    # Rewrite the file
    fh = open(text, "w")
    fh.write("".join(lines))
    fh.close()

def Get_Video_URL(url):
    print("Starting...")
    print("Opening Window...")
    driver = webdriver.Chrome()
    
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
    
    title = driver.title
    # You might have to change id="mp4" to whatever the site uses
    link  = driver.find_elements_by_xpath('//*[@id="mp4"]')[0].get_attribute("src")
    
    driver.quit()
    return str(title), str(link)
    


url_dict = {'VideoURLs_1':'VideoLinks_1.txt'}

key = 'VideoURLs_1'
text = url_dict[key]

Clear_Empty_Lines(text)

sz = []
text_file_re = open(text, "r", encoding='utf-8')
for x in text_file_re:
    sz.append(x.strip('\n'))
text_file_re.close()

video_file_name = key+".txt"
if os.path.isfile(video_file_name):
    
    already = []
    video_text_file_r = open(video_file_name, "r", encoding='utf-8')
    for x in video_text_file_r:
        already.append(x.strip('\n').split(" : ")[1])
    video_text_file_r.close()

    print("Adding the URLs...")
    text_file_r = open(text, "r", encoding='utf-8')
    n = 0
    for url in text_file_r:
        if url.strip('\n') not in already:
            title, link = Get_Video_URL(url)
            video_file = open(video_file_name, "a", encoding='utf-8')
            video_file.write("%s : %s" % (title, link))
            video_file.close()
            n += 1
    text_file_r.close()

    print("---------------------------------------------------")
    print("There are %d videos in total" % len(sz))
    print("There are", n, "new URLs added")
    print("---------------------------------------------------")

else:
    print('Creating file:', video_file_name)
    video_file = open(video_file_name, "w", encoding='utf-8')
    video_file.close()
    
    print("Writing the URLs...")
    text_file_r = open(text, "r", encoding='utf-8')
    n = 0
    for url in text_file_r:
        title, link = Get_Video_URL(url)
        video_file = open(video_file_name, "a", encoding='utf-8')
        video_file.write("%s : %s\n" % (title, link))
        video_file.close()
        n += 1
    text_file_r.close()
    
    print("---------------------------------------------------")
    print("There are %d videos in total" % len(sz))
    print("There are", n, "written")
    print("---------------------------------------------------")

print("Finished!!!")

