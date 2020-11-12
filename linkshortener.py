#!/usr/bin/env python3
#https://github.com/AngelSecurityTeam/GenTiny
import requests,os,sys
cyan= '\033[33m'
bold= '\033[1m'
end= '\033[0m'

def GenTiny():
	 
    print("""{1}{2}{1}
░▒▓█ 𝓛𝓲𝓷𝓴 𝓢𝓱𝓸𝓻𝓽𝓮𝓷𝓮𝓻 █▓▒░
  {0}{1}Emre Koybasi{2} 
""".format(end,bold,cyan))
GenTiny()
url = input("\033[0m\033[1m\033[36m~/URL# \033[0m\033[1m")
tiny = 'http://tinyurl.com/api-create.php?url='+url
info = requests.get(tiny)
print("\033[0m\033[1m\033[36m~/Link# \033[0m\033[1m"+info.text)

