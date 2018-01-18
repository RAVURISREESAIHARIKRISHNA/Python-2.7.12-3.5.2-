import schedule,time
from tqdm import tqdm
import requests

def download():
    chunk_size = 1024

    urlarr = [
        "https://r5---sn-5hne6n7z.googlevideo.com/videoplayback?ip=37.58.82.168&id=o-AEQVpYtdeKKyZQTD2rGgct2g1sbxBrc0ZHx-g1-PbXFw&clen=24454268&mv=m&dur=521.148&mt=1516251582&ms=au&mn=sn-5hne6n7z&ipbits=0&mm=31&gir=yes&initcwndbps=880000&sparams=clen%2Cdur%2Cei%2Cgir%2Cid%2Cinitcwndbps%2Cip%2Cipbits%2Citag%2Clmt%2Cmime%2Cmm%2Cmn%2Cms%2Cmv%2Cpl%2Cratebypass%2Crequiressl%2Csource%2Cexpire&itag=18&ei=_SlgWsL1IoGZ1gKA2avAAw&signature=C8262E55801D23D94D17ECF3602D2752D3ED2C7E.DC15F819F66D721852AE183F512EF222A1DAE92F&ratebypass=yes&expire=1516273245&pl=22&mime=video%2Fmp4&source=youtube&key=yt6&requiressl=yes&lmt=1497766466820877&title=Question+on+Recursion+-+8",
        "https://r3---sn-5hnedn7z.googlevideo.com/videoplayback?expire=1516273283&ratebypass=yes&dur=872.489&ipbits=0&initcwndbps=880000&itag=18&clen=40567039&key=yt6&mime=video%2Fmp4&gir=yes&ei=IypgWrqqEo_O1wKFmZ2IBQ&signature=DE2E34D151D210DE86F500C48948FD6A365BD5EF.934A880A586D08C36F7AE897D62B0FDE4F773F18&source=youtube&lmt=1497772434803538&pl=22&id=o-ANaqB8089xs7HP-VE-cQOsIeh-IZ1KoaKPm_pxmi1Wf2&mn=sn-5hnedn7z&mm=31&ms=au&sparams=clen%2Cdur%2Cei%2Cgir%2Cid%2Cinitcwndbps%2Cip%2Cipbits%2Citag%2Clmt%2Cmime%2Cmm%2Cmn%2Cms%2Cmv%2Cpl%2Cratebypass%2Crequiressl%2Csource%2Cexpire&mv=m&mt=1516251582&requiressl=yes&ip=37.58.82.168&title=Question+on+Recursion+-+9"
    ]
    for url in urlarr:
        r = requests.get(url , stream = True)
        total_size = int(r.headers['content-length'])
        dest = "G:\\MY MATERIALS\\Algorithms\\Recursion\\"+url[url.index("&title=")+7:].replace("+"," ")+".mp4"
        print("Downloading "+dest+" ...")
        with open(dest,'wb') as f:
            for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = total_size/chunk_size,unit='KB'):
                f.write(data)

    print("Download Complete")

schedule.every().day.at("11:10").do(download)

while True:
    schedule.run_pending()
