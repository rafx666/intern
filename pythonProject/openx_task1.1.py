import json
from urllib.request import urlopen

url_main = urlopen("https://openx.com/sellers.json")
j_url_main = json.load(url_main)

url_asc = urlopen("https://ascendeum.com/sellers.json")
j_url_asc = json.load(url_asc)

print(j_url_main["contact_address"])
print("\n")
print("contact sellers: ")
print("\n")

asc_name = j_url_asc["contact_address"][0:12]+"."

i = 0
while i < len(j_url_main["sellers"]):
    warunek = asc_name == j_url_main["sellers"][i]["name"]
    if warunek == True:
        index = i
        break
    else:
        pass
    i+=1

j_url_main["sellers"][index]["sellers"] = j_url_asc["sellers"]

i = 0
while i < len(j_url_main["sellers"]):
    print("seller: {}, seller type: {}".format(j_url_main["sellers"][i]["name"], j_url_main["sellers"][i]["seller_type"]))
    if i == index:
        d = 0
        while d < len(j_url_asc["sellers"]):
            print("\t seller: {}, seller type: {}".format(j_url_main["sellers"][index]["sellers"][d]["name"], j_url_main["sellers"][index]["sellers"][d]["seller_type"]))
            d += 1
    else:
        pass
    i += 1
