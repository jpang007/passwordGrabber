# passwordLocker & AutoLogger
Goals for this project: 
* Demonstrate my interest in cybersecurity
* Develop a potential AutoLogger 

DISCLAIMER: I realize that this project (if finished) could be used to break into peoples' accounts. I just want to demonstrate my knowledge and develop skills in this area NOT for illegal purposes. This should only be for testing purposes and can only be used where strict consent has been given.

<h1> Features </h1>
<hr>
Personal project I am working on, started off by modifying a short existing code to just retrieve the password in a dictionary and copy it to clipboard (https://automatetheboringstuff.com/chapter5/). Using BeautifulSoup to webscrape html data, added in functionality that webscrapes the top 100 most common passwords allows you to grab which one you want based on popularity. The user can choose between using the most common list of passwords or their own. Then using Pyperclip, the desired password is copied to the users' clipboard.

Then I further modified the code to accept any popularity number (e.g #456), my code then calculated what page this would be on and webscraped the according page. I originally wanted to just store a database of all the passwords, then find which one, however it would take way too long (Almost 10 seconds to webscrape just the top 1000!). 

Currently using Twill to attempt to log onto https://www.facebook.com, want to expand by allowing code to read lxml to quickly grab the set of passwords from http://www.passwordrandom.com/most-popular-passwords/. Currently having issues since using BeautifulSoup takes too much time. 
<hr>

<h1> Tasklist </h1>
<hr>
- [x] Extend program to take in dictionary from custom input file
- [x] Webscraped http://www.passwordrandom.com/most-popular-passwords top 100 passwords
- [x] Webscrap all 10000 passwords for same functionality (realistically took too long to make a large database)
- [ ] Implement ability to attempt to login with all passwords stored in database (possible?) 
