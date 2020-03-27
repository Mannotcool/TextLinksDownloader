import urllib
from urllib.request import urlretrieve
from urllib.error import URLError, HTTPError

# Imported http libarays

x = 1
for g in range(0,31):
    with open('urls.txt') as f:
        while True:
            try:
                for i, line in enumerate(f, 1):
                    urllib.request.urlretrieve(line, "File - " + str(i) + ".pdf")
                    print(str(i) + " Completed!")
            except HTTPError:
                print("Skiped Url due to 404")
                continue
            print("Downloaded All Avalable Files from TXT")
            f.close()

