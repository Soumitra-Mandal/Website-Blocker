import time 
from datetime import datetime as dt 
redir = "127.0.0.1" #LOCALHOST
hosts = "C:\Windows\System32\drivers\etc\hosts"
  
# websites That you want to block 
sites = ['facebook.com'] 
  
while True:  
    if dt(dt.now().year, dt.now().month, dt.now().day,10)< dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,17): #Time restrcition is from 10 A.M. to 5 P.M.
        with open(hosts, 'r+') as f: 
            data = f.read() 
            for site in sites: 
                if site in data: 
                    pass
                else: 
                    f.write(redir + " " + site + "\n") 
    else: 
        with open(hosts, 'r+') as f: 
            data=f.readlines() 
            f.seek(0) 
            for line in data: 
                if not any(site in line for site in sites): 
                    f.write(line) 
            f.truncate() 
    time.sleep(10) 