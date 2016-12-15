#! python3
# pw.py - An insecure password locker program.
# Extend program to take in dictionary from custom input File check
# Extend program to take the most commonly used Passwords,
# & write to to a file so we can grab whichever number we want in popularity
# Extend program to keep pasting and trying password into a text box (possible)?

import sys, pyperclip, urllib2
from itertools import izip

passwordPage = "http://www.passwordrandom.com/most-popular-passwords"
page = urllib2.urlopen(passwordPage)

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

def main(account, filename):
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

    dicA = passwordUpdate(filename)

    print "Would you like to use the default list of passwords or your own?"
    print "(type default or own)"
    string = raw_input('Enter your input: ')
    if (string == "default"):
        passwordFind(account, d)
    elif (string == "own"):
        passwordFind(account, dicA)

if __name__ == '__main__':

    if len(sys.argv) < 3:
        print('Usage: py pw.py [account] [filename] - copy account password')
        quit(1)
    main(sys.argv[1],sys.argv[2])
