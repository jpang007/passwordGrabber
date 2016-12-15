# passwordLocker & LoginChecker
Goals for this project: 
* Demonstrate my interest in cybersecurity
* Develop a potential LoginChecker 

DISCLAIMER: I realize that this project (if finished) could be used to break into peoples' accounts. I just want to demonstrate my knowledge and develop skills in this area NOT for illegal purposes. This should only be for testing purposes and can only be used where strict consent has been given.

<h1> Features </h1>
<hr>
* Ability to use ones' own password list or http://www.passwordrandom.com/most-popular-passwords/ (default)
* Select a password based off a dictionary key or popularity (if using the default) 
* If interested, can run obtained password against a Facebook login
<hr>

<h1> Documentation </h1>
<hr>
Personal project I worked on, started off by modifying a short existing code to just retrieve the password in a dictionary and copy it to clipboard (https://automatetheboringstuff.com/chapter5/). Using BeautifulSoup to webscrape html data, added in functionality that webscrapes the top 100 most common passwords allows you to grab which one you want based on popularity. The user can choose between using the most common list of passwords or their own. Then using Pyperclip, the desired password is copied to the users' clipboard.

Then I further modified the code to accept any popularity number (e.g #456), my code then calculated what page this would be on and webscraped the according page. I originally wanted to just store a database of all the passwords, then find which one, however it would take way too long (Almost 10 seconds to webscrape just the top 1000!). 

This program can also check if the password you want to use (either from the most common or a personal list), is someones' password at https://www.facebook.com. Of course, you should only be using this to try and get into your own account. As of right now the program will return the info gathered, if the site url is just https://www.facebook.com you know the email/password combination is valid. Otherwise you will see https://www.facebook.com/login.php?login_attempt=1&lwv=110. 
<hr>

<h1> Needed For Installation </h1> 
<hr>
1. Pyperclip
2. BeautifulSoup
3. Twill
4. lxml (for Twill)
<hr>

<h1> Tasklist </h1>
<hr>
- [x] Extend program to take in dictionary from custom input file
- [x] Webscraped http://www.passwordrandom.com/most-popular-passwords top 100 passwords
- [x] Webscrap all 10000 passwords for same functionality (realistically took too long to make a large database)
- [x] Implement ability to attempt to login with a password stored in database 
