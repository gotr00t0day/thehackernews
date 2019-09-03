#!/usr/bin/python3

from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from colorama import Fore, Back, Style
import requests, re, string

banner = """

╔╦╗┬ ┬┌─┐  ╦ ╦┌─┐┌─┐┬┌─┌─┐┬─┐  ╔╗╔┌─┐┬ ┬┌─┐
 ║ ├─┤├┤   ╠═╣├─┤│  ├┴┐├┤ ├┬┘  ║║║├┤ │││└─┐
 ╩ ┴ ┴└─┘  ╩ ╩┴ ┴└─┘┴ ┴└─┘┴└─  ╝╚╝└─┘└┴┘└─┘

Author: c0d3Ninja
"""

print (banner)

ua = UserAgent()
header = {'User-Agent':str(ua.chrome)}
link = "https://thehackernews.com/"
response = requests.get(link, timeout=5, headers=header)
if response.status_code == 200:
    print ("-" * 70)
    print("Webite: " + Fore.GREEN + link)
    print(Fore.WHITE + "Status: " + Fore.GREEN + "UP")
else:
    exit()

soup = BeautifulSoup(response.content, "html.parser")
menu = soup.find_all('li',attrs={"class":"show-menu"})

title = soup.title

for titletext in title:
    print(Fore.WHITE + "Title: " + Fore.GREEN + titletext)
    print (Fore.WHITE + "-" * 75)

for links in soup.find_all('a',attrs={"class":"story-link"}):
    seperator = Fore.CYAN + "-" * 75
    print(Fore.WHITE)
    print (''.join(x for x in links.text if x in string.printable).strip() + "\n\n" + Fore.GREEN + links.get('href') + "\n" + seperator + "\n")
