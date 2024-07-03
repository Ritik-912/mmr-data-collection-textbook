import requests
from bs4 import BeautifulSoup
from pandas import read_csv, DataFrame
import re
urls = read_csv("scrapped_url.csv").values.tolist()
viewer_links = "http://ndl.iitkgp.ac.in/module-viewer/viewer.php?id="
df = []
error_links = []
for url in urls:
    link = "/".join(url[0].split("/")[4:]).split('?')[0]
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/532.36',
        'Referer':url[0]}
    response = requests.get(viewer_links+link+"&domain=se", headers=headers)
    soup = BeautifulSoup(response.content, features="html.parser")
    scripts = soup.find_all("script", {'type': 'text/javascript'})
    try:
        for script in scripts:
            match = re.search(r'"url":"(.*?)"', script.string)
            df.append("http://ndl.iitkgp.ac.in"+match.group(1))
            break
    except:
        try:
            tag_link = soup.find("a", {"class": "btn btn-success"})['href']
            df.append(tag_link)
        except:
            error_links.append(url[0])
print("Number of pdf links = ", len(df))
DataFrame(df, columns=["url"]).to_csv("download_url.csv", index=False)
DataFrame(error_links, columns=["url"]).to_csv("error_download_links.csv", index=False)