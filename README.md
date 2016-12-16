# passwordGrabber & LoginChecker
Goals for this project:
* Demonstrate my interest in cybersecurity
* Develop a potential LoginChecker

DISCLAIMER: I realize that this project can be used to break into peoples' accounts. I just want to demonstrate my knowledge and develop skills in this area NOT for illegal purposes. This should only be for testing purposes and can only be used where strict consent has been given.

For a more in-depth explanation why I made this, go to documentation.md. 

<h1> Features </h1>
<hr>
* Ability to use ones' own password list or http://www.passwordrandom.com/most-popular-passwords/ (default)
* Select a password based off a dictionary key or popularity (if using the default), then copies said password to clipboard
* If interested, can run obtained password against a Facebook login

<h1> Need to install to run </h1>
<hr>
1. Pyperclip
2. BeautifulSoup
3. Twill
4. lxml (for Twill)

<h1> How to run </h1>
<hr>
default most common passwords: python passwordLocker.py [int of popularity number]

own textfie: python passwordLocker.py [account number] [textfile]

<h1> Tasklist </h1>
<hr>
- [x] Extend program to take in dictionary from custom input file
- [x] Webscraped http://www.passwordrandom.com/most-popular-passwords top 100 passwords
- [x] Webscrap all 10000 passwords for same functionality (realistically took too long to make a large database)
- [x] Implement ability to attempt to login with a password stored in database
- [x] Expand program to convert a list of passwords to dictionary format (so user can feed it just a text file of just passwords)

