#! python3
# pw.py - An insecure password locker program.
# Extend program to take in dictionary from custom input File check
# Extend program to take the most commonly used Passwords,
# & write to to a file so we can grab whichever number we want in popularity
# Extend program to keep pasting and trying password into a text box (possible)?
# Notes to run this program you need to install pyperclip, BeautifulSoup, Twill, lxml, cssselect, requests

import sys, pyperclip, urllib2
from itertools import izip
import re
import time
from bs4 import BeautifulSoup
from pprint import pprint
from twill.commands import *

# Here we can try some login attempts :)
# After experimenting in Twill-sh if we attempt to login to FB with a wrong password
# We will get current page: https://www.facebook.com/login.php?login_attempt=1&lwv=110
# If we login with a correct attempt we just get https://www.facebook.com

def loginToSite(passwords):
    go('https://facebook.com/')
    print "What email would you like to use?"
    emailString = raw_input()
    fv("1", "email", emailString)
    fv("1", "pass", passwords)
    submit()
    info()

def passwordFind(account, Passwords):
    if account in Passwords:
        pyperclip.copy(Passwords[account])
        print('Password key value number/name ' + account + ' copied to clipboard.')
    else:
        print('There is no account named ' + account)
    return Passwords[account]

def yummySoup(account, page):
    soup = BeautifulSoup(page, "html.parser")
    all_tables=soup.find_all('table')
    right_table=soup.find('table', class_='table')
    d = {}
    for row in right_table.findAll("tr"):
        AccountLines = row.findAll('td')
        if len(AccountLines)==8: #Only extract table body not heading
            AccNum = AccountLines[0].getText()
            CommonPasswords = AccountLines[1].getText()
            d[AccNum] = CommonPasswords
    return passwordFind(account, d)

def passwordUpdate(filename):
    d = {}
    with open(filename) as f:
        for line in f:
           (key, val) = line.split()
           d[key] = val
    return d
#Code for own document
#Expand to take in almost any formant?
def main2(account, filename):
    start=time.clock()
    dicA = passwordUpdate(filename)
    passwordAttempt = passwordFind(account, dicA)

    print "Password copied successfully! Would you like to try to run it against a Facebook login? (yes or no)"
    yesOrNo = raw_input()
    if yesOrNo == "yes":
        loginToSite(passwordAttempt)
    elif yesOrNo == "no":
        print "OK!"
        quit(1)


    end=time.clock()
    main2time=end-start
    print("Personal textfile timing: "+str(main2time)) + " seconds."

#Code for common passwords
def main(account):
    start=time.clock()
    #Finds the page that we want to webscrape
    passwordPage = "http://www.passwordrandom.com/most-popular-passwords"
    nextPage = "/page/" #NEEDED for all pages after the first one

    if (int(account) > 100):
        if (int(account) % 100 == 0):
            relatedPage = int(account) / 100
        else:
            relatedPage = int(account) / 100 + 1
        passwordPage = passwordPage + nextPage + str(relatedPage)

    page = urllib2.urlopen(passwordPage)

    passwordString = yummySoup(account, page)
    print "Would you like to try to run it against a Facebook login? (yes or no)"
    yesOrNo = raw_input()
    if yesOrNo == "yes":
        loginToSite(passwordString)
    elif yesOrNo == "no":
        print "OK!"
        quit(1)

    end=time.clock()
    maintime=end-start
    print("Common passwords timing: "+str(maintime)) + " seconds."

if __name__ == '__main__':
    print "Would you like to use the default list of passwords or your own?"
    print "(type default or own)"
    string = raw_input('Enter your input: ')
    if (string == "default"):
        main(sys.argv[1])
    elif (string == "own"):
        main2(sys.argv[1],sys.argv[2])
