import re
url=input("enter a url: ")

def domain_name(url):
    print(url.split("www.")[-1].split("//")[-1].split("/")[0])
domain_name(url)
