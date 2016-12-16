What is this?

Personal project I worked on, started off by modifying a short existing code to just retrieve the password in a dictionary and copy it to clipboard (https://automatetheboringstuff.com/chapter5/). Using BeautifulSoup to webscrape html data, added in functionality that webscrapes the top 100 most common passwords allows you to grab which one you want based on popularity. The user can choose between using the most common list of passwords or their own. Then using Pyperclip, the desired password is copied to the users' clipboard.

Then I further modified the code to accept any popularity number (e.g #456), my code then calculated what page this would be on and webscraped the according page. I originally wanted to just store a database of all the passwords, then find which one, however it would take way too long (Almost 10 seconds to webscrape just the top 1000!).

This program can also check if the password you want to use (either from the most common or a personal list), is someones' password at https://www.facebook.com. Of course, you should only be using this to try and get into your own account. As of right now the program will return the info gathered, if the site url is just https://www.facebook.com you know the email/password combination is valid. Otherwise you will see https://www.facebook.com/login.php?login_attempt=1&lwv=110.

Why is this useful?

This program is able to retreive a certain password from a long list, for example if you have a million passwords and you want the 6,700 one but they are not numbered, this program can do that for you. The option to try to login to Facebook is also avaliable, I mostly included this as groundwork for the next
