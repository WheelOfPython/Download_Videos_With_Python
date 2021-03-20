# Download Videos With Python
It makes a text file with the URL addresses of the videos of a given page and downloads them !!!

It works by opening a browser instance, scrolling down to catch everything and searches the HTML file for the video URLs. Then it closes the instance.

Unfortunately, you'll have to tweek the code to fit to your needs. So some basic knowlege of HTML is necessary.<br /> 
The scripts here are general and would work with any site that includes direct links to the video files (or any other type of file .jpg, .png, .mp3 etc).

It's based on a previous repository I made for getting YouTube videos' urls.

# Dependencies
!!! This code works only with the Chrome/Chromium browser !!!

• selenium (Python library)

• chromedriver (Executable)

You can download the chromedriver executable for your Chromium version from here: https://chromedriver.chromium.org/downloads

# Setup
Make a directory, in which you will put the python scripts and the chromedriver.exe (on Windows).

The text files will be saved in the same directory.

# Workflow
<ins>**1st Step (Not always needed)**</ins>

If you have a page, where you click on links to go to a page containing the video, use GetLinks_Site.py to get the URLs of the those video pages.

Using Chrome, right-click -> inspect element.<br /> 
With the help of the visual guide, you'll be able to find a line containing a link. They'll all have the same syntax.<br /> 
Put the flag in .find_elements_by_xpath().

After the text file is created, you'll have to manually check it, because some URLs might not contain videos and you'll have to delete them. 
They usually appear in the first few lines and are easy to find.

<ins>**2nd Step**</ins>

Use GetLinks_Video.py to get the URLs of the videos from their pages.<br /> 
Do the same thing as before to find the link format and put it in .find_elements_by_xpath() of this script.

<ins>**3rd Step**</ins>

Use Download_Videos.py to download the videos.
Here, you can specify the location and the name of the video files.
