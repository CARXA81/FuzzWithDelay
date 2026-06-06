import requests
import optparse
import time 
parser = optparse.OptionParser()
parser.add_option("-u", "--url", help="Base target uri (ex. http://10.10.10.100/cms)")

options, args = parser.parse_args()
if not options.url:
        print("\n [+] Need a url to execute script")
        exit()

print(f'\n url = { options.url }')

dic = "./wordlist.txt"

with open(dic, 'r', encoding="utf-8") as file:
    for linea in file:

        time.sleep(1)
        directorio = linea.strip()
        urlF = f"{options.url}/{linea}"
        print(f"Target :{urlF}")
