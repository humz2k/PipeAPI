import requests

class PipeAPI:
    def __init__(self,url="http://127.0.0.1:5000"):
        self.url = url

    def alive(self):
        try:
            send = {"command":"ping"}
            response = requests.get(self.url,params=send)
            return response.json()['alive'] == '1'
        except:
            return False

    def image_math(self,date,user,exposures,filters,limit=0):
        expo = ",".join([str(i) for i in exposures])
        filt = ",".join(filters)
        lim = str(limit)
        send = {"command":"image_math","date": date,"user": user,"exposures": expo,"filters": filt,"limit":lim}
        response = requests.get(self.url,params=send)
        return response.json()['job']

'''
todo = {"name": "bob"}
response = requests.get(api_url,params=todo)
print(response.json())
'''
pipe = PipeAPI()
if pipe.alive():
    print(pipe.image_math("2022-02-18","hqureshi",[128],["g-band","r-band"]))
