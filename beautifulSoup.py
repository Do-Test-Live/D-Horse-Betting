import requests
import time

j=1

while j<10:
    url = "https://bet.hkjc.com/racing/getJSON.aspx?type=winplaodds&date=2023-06-28&venue=HV&start="+str(j)+"&end="+str(j)

    response = requests.get(url)

    if response.status_code == 200:
        time.sleep(1)

        json_data = response.json()
        print(json_data)

    else:
        print("Failed to retrieve JSON data. Status code:", response.status_code)

    j = j + 1
    print('\n')
