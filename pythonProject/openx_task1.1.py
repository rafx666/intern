import json
from urllib.request import urlopen
#importing libraries and modules

url_main = urlopen("https://openx.com/sellers.json")
j_url_main = json.load(url_main)

url_asc = urlopen("https://ascendeum.com/sellers.json")
j_url_asc = json.load(url_asc)
#opening both .json files

print("Contact address: {}".format(j_url_main["contact_address"]))
print("\n")
print("Contact sellers: ")
print("\n")

asc_name = j_url_asc["contact_address"][0:12]+"."
#adjusting the name string so that it matches in both files

i = 0
while i < len(j_url_main["sellers"]):   #while i is smaller than the lenght of the list of sellers
    condition = asc_name == j_url_main["sellers"][i]["name"] #asc_name has to be equal with name of seller from the list
    if condition == True: #if this condition is fulfilled it reads the index of the seller on the list and writes it to variable index
        index = i
        break
    else:   #if the condition isnt fulfilled it passes and iterates again
        pass
    i+=1

j_url_main["sellers"][index]["sellers"] = j_url_asc["sellers"]
#assigning list of sellers under Ascendum to the main list so its all in one file and can be printed out easier
i = 0
while i < len(j_url_main["sellers"]):   #while i is smaller than lenght of list of sellers in main list
    print("seller:  {},    seller type:  {}".format(j_url_main["sellers"][i]["name"], j_url_main["sellers"][i]["seller_type"])) #it prints out sellers names and types
    if i == index: #if number of seller matches the index of Ascendum seller which has sellers under him
        d = 0
        while d < len(j_url_asc["sellers"]):    #while d is smaller than lenght of list of sellers under Ascendum
            print("\t seller:  {},    seller type:  {}".format(j_url_main["sellers"][index]["sellers"][d]["name"], j_url_main["sellers"][index]["sellers"][d]["seller_type"]))
            d += 1  #it prints out sellers names and types, but the data is tabbed so its more visible
    else:
        pass
    i += 1
