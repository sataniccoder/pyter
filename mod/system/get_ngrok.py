import requests
import os

def get():
    r = requests.get("http://localhost:4040/api/tunnels")
    r = r.text
    print(r)
    r = r.split(",")
    for i in range(len(r)):
        if "public_url" in r[i] and "https" not in r[i]:
            url = r[i]
            url = url.split(":")
            url = url[2]
            url = url.replace('"',"")
            print("[+] ngrok: http:"+url+"/")
            input("[+] hit enter to continiue ")
        else:
            pass
def start(path):
    c = path+"/./ngrok http 5000 > .dev.null &"
    os.system(c)