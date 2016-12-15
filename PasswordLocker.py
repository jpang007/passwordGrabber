#! python3
# pw.py - An insecure password locker program.
# Extend program to take in dictionary from custom input File check
# Extend program to take the most commonly used Passwords,
# & write to to a file so we can grab whichever number we want in popularity
# Extend program to keep pasting and trying password into a text box (possible)?

import sys, pyperclip, urllib2
from itertools import izip

from bs4 import BeautifulSoup
from pprint import pprint

def passwordFind(account, Passwords):
    if account in Passwords:
        pyperclip.copy(Passwords[account])
        print('Password for ' + account + ' copied to clipboard.')
    else:
        print('There is no account named ' + account)

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
    dicA = passwordUpdate(filename)
    passwordFind(account, dicA)

#Code for common passwords
def main(account):
    #Finds the page that we want to webscrape
    passwordPage = "http://www.passwordrandom.com/most-popular-passwords"

    #We know the next X pages are just /page/31
    #We could do it in a for loop for O(n) time but is there a faster way?

    page = urllib2.urlopen(passwordPage)

    #The acutal BS code
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
    passwordFind(account, d)

if __name__ == '__main__':
    print "Would you like to use the default list of passwords or your own?"
    print "(type default or own)"
    string = raw_input('Enter your input: ')
    if (string == "default"):
        main(sys.argv[1])
    elif (string == "own"):
        main2(sys.argv[1],sys.argv[2])
