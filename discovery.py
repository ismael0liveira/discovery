import requests
import urllib3
import pyfiglet

banner = pyfiglet.figlet_format("D1SCOV3RY")
print(banner)

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


site = input('Site: ')
wordlist = input('Wordlist: ')

arquivo = open(wordlist)

for d in arquivo.readlines():
	requisicao = requests.get(site+"/"+d.replace('\n',''),verify = False)
	print(requisicao.url+"\033[31;1m[=>]\033[m"+"\033[32;1m"+str(requisicao.status_code)+"\033[m")
