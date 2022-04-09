import requests
import sys
import traceback



prefix = "https://mta-sts."
ending = "/.well-known/mta-sts.txt"
domains = ["google.com", "facebook.com", "bing.com", "microsoft.com", "alexander.dk"]


original_stdout = sys.stdout 

for x in domains:
    try:
        url = prefix + x + ending
        r = requests.get(url).status_code
        if r == 200:
            print(url + " has MTA-STS")
            f = open("all.txt", "a")
            f.write(url + " has MTA-STS" "\n")
            f.close()
            f = open("pass.txt", "a")
            f.write(url + " has MTA-STS" "\n")
            f.close()
        if r == 404:
            f = open("all.txt", "a")
            f.write(url + " does not MTA-STS" "\n")
            f.close()
            f = open("failed.txt", "a")
            f.write(url + " does not MTA-STS" "\n")
            f.close()
    except Exception:
        print (Exception)
        print(url + " failed")
        f = open("all.txt", "a")
        f.write(url + " does not MTA-STS" + "\n")
        f.close()
        f = open("failed.txt", "a")
        f.write(url + " does not MTA-STS" + "\n")
        f.close()
     




