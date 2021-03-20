import requests
import os
import urllib
import math

CHUNK_SIZE = 1024

def Get_Size(url):
    req = urllib.request.Request(url, method='HEAD')
    f = urllib.request.urlopen(req)
    file_size = int(f.headers['Content-Length'])/CHUNK_SIZE
    return math.ceil(file_size)

def download_file(path, title, url):
    local_filename = path + title
    r = requests.get(url, stream=True)
    sz = Get_Size(url)
    i=0
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=CHUNK_SIZE): 
            if chunk:
                f.write(chunk)
                i+=1
                print("%.2f" % (i/sz * 100), '%')
    return local_filename

file_name = "VideoURLs_1.txt"

lines=[]
text_file_r = open(file_name, "r", encoding='utf-8')
for x in text_file_r:
    lines.append(x.strip('\n'))
text_file_r.close()

path = "Disk:/path/to/folder/"
n = 1
N = len(lines)
for line in lines:
    a, b = line.split(' : ')
    title = a + ".mp4" # Here you can change the file name, removing non Winodws chars with a.replace('(','') etc
    url   = b # You can also change the url if you want to
    print("Starting Download", "%i/%i" % (n, N))
    if os.path.isfile(path + title):
        print(title + " already exists")
    else:
        print(title + ' || ' + url)
        download_file(path, title, url)
        print("Finished Download")
    n += 1 

print("Finished all downloads !!!")