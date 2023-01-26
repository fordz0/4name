import requests
import time

base_url = 'https://api.mojang.com/users/profiles/minecraft/'
nameString = ""

offset1 = 0
offset2 = 0
offset3 = 0
offset4 = 0

with open('namesFile.txt', 'r') as f:
    lines = f.read().splitlines()
    if lines:
        last_line = lines[-1]
        nameString = last_line[:4]
        
if nameString != "":
    offset1 = ord(nameString[0]) + 1 - 97
    offset2 = ord(nameString[1]) - 97
    offset3 = ord(nameString[2]) - 97
    offset4 = ord(nameString[3]) - 97

for four in range(97 + offset4, 123):
    offset4 = 0
    for three in range(97 + offset3, 123):
        offset3 = 0
        for two in range(97 + offset2, 123):
	    offset2 = 0
            for one in range(97 + offset1, 123):
		offset1 = 0
                name = chr(one)+chr(two)+chr(three)+chr(four)
                url = ''.join([base_url, name])
                x = requests.get(url)
                time.sleep(1)
                if x.status_code == 429:
                    print("waiting")
                    time.sleep(62)
                    print("done waiting")
                elif x.status_code != 200:
                    message = name + " is available\n"
                    print(name + " is available")
                    f = open("namesFile.txt", "a")
                    f.write(message)
                    f.close()
                else:
                    print("not available")
