import requests
import time

base_url = 'https://api.mojang.com/users/profiles/minecraft/'
nameString = ""

offset1 = 97
offset2 = 97
offset3 = 97
offset4 = 97

with open('namesFile.txt', 'r') as f:
    lines = f.read().splitlines()
    if lines:
        last_line = lines[-1]
        nameString = last_line[:4]
        
if nameString != "":
    offset1 = ord(nameString[0]) + 1
    offset2 = ord(nameString[1])
    offset3 = ord(nameString[2])
    offset4 = ord(nameString[3])

for four in range(offset4, 123):
    print(four)
    for three in range(offset3, 123):
        for two in range(offset2, 123):
            for one in range(offset1, 123):
                name = chr(one)+chr(two)+chr(three)+chr(four)
                print(name)
                url = ''.join([base_url, name])
                x = requests.get(url)
                time.sleep(1)
                if x.status_code == 429:
                    print("waiting")
                    time.sleep(62)
                    print("done waiting")
                elif x.status_code != 200:
                    message = name + " is available\n"
                    print(message)
                    f = open("namesFile.txt", "a")
                    f.write(message)
                    f.close()
                else:
                    print("not available")
