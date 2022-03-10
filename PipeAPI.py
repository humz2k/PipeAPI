import requests
import time
import random

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

    def status_update(self,job_no):
        send = {"command":"check","job":str(job_no)}
        response = requests.get(self.url,params=send)
        return response.json()['finished'] == '1'

    def download(self,file):
        send = {"command":"download","file":file}
        response = requests.get(self.url,params=send)
        open(file, 'wb').write(response.content)

    def image_math(self,date,user,exposures,filters,limit=0):
        expo = ",".join([str(i) for i in exposures])
        filt = ",".join(filters)
        lim = str(limit)
        send = {"command":"image_math","date": date,"user": user,"exposures": expo,"filters": filt,"limit":lim}
        response = requests.get(self.url,params=send)
        files = response.json()['files'].split(",")
        job_no = response.json()['job']
        print("Job Number:",job_no)
        while True:
            print("Waiting for job to be finished" + "."*random.randint(0,4))
            if self.status_update(job_no):
                break
            time.sleep(10)
        for file in files:
            self.download(file)
        return job_no,files

'''
todo = {"name": "bob"}
response = requests.get(api_url,params=todo)
print(response.json())
'''
pipe = PipeAPI()

if pipe.alive():
    pipe.image_math("2022-02-18","hqureshi",[128],["r-band"],limit=3)
    #pipe.image_math("2022-02-18","hqureshi",[128],["h-alpha"],limit=3)
print(pipe.alive())
'''
'm51_i-band_128.0s_bin1H_220218_080941_hqureshi_seo_0_RAW.fits', 'm51_i-band_128.0s_bin1H_220218_081259_hqureshi_seo_0_RAW.fits', 'm51_i-band_128.0s_bin1H_220218_081529_hqureshi_seo_1_RAW.fits', 'm51_i-band_128.0s_bin1H_220218_081759_hqureshi_seo_2_RAW.fits', 'm51_i-band_128.0s_bin1H_220218_082030_hqureshi_seo_3_RAW.fits', 'm51_i-band_128.0s_bin1H_220218_082300_hqureshi_seo_4_RAW.fits', 'm51_i-band_128.0s_bin1H_220218_082530_hqureshi_seo_5_RAW.fits', 'm51_i-band_128.0s_bin1H_220218_082800_hqureshi_seo_6_RAW.fits', 'm51_i-band_128.0s_bin1H_220218_083030_hqureshi_seo_7_RAW.fits', 'm51_i-band_128.0s_bin1H_220218_083300_hqureshi_seo_8_RAW.fits'
'''
