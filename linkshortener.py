#!/usr/bin/env python3
import requests,os,sys
cyan= '\033[36m'
bold= '\033[1m'
end= '\033[0m'

def GenTiny():
	 
    print("""{1}{2}{1}

                  __        __   __  ___  ___       ___  __  
|    | |\ | |__/ /__` |__| /  \ |__)  |  |__  |\ | |__  |__) 
|___ | | \| |  \ .__/ |  | \__/ |  \  |  |___ | \| |___ |  \ 
                                                             

  {0}{1}EmreKybs{2} 
""".format(end,bold,cyan))
GenTiny()
url = input("\033[0m\033[1m\033[36m~/URL: \033[0m\033[1m")
tiny = 'http://tinyurl.com/api-create.php?url='+url
info = requests.get(tiny)
print("\033[0m\033[1m\033[36m~/Link: \033[0m\033[1m"+info.text)
