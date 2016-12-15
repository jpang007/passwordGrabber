#! python3
# pw.py - An insecure password locker program.
# Extend program to take in dictionary from custom input File check
#

import sys, pyperclip
from itertools import izip

def passwordFind(account, Passwords):
    print Passwords
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


def main(filename, account):
    dicA = passwordUpdate(filename)
    passwordFind(account, dicA)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: py pw.py [filename] [account] - copy account password')
        quit(1)
    if len(sys.argv[1]) < 2:
        print('Usage: py pw.py [filename] [account] - copy account password')
        quit(1)
    main(sys.argv[2],sys.argv[1])
