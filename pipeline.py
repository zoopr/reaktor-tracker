import json

log = "".join([(chr(int(msg, base=2))) for msg in open("D:/GitHub/ppb.bin.log", "r").readline().split(" ")])
contaminants = dict()
j = json.loads(log)
for day in j:
    for reading in day["readings"]:
        sum = 0
        for x in reading["contaminants"]:
            sum += reading["contaminants"][x]
        if (sum < 900000) or (sum > 1100000): #ugly as sin, but I had scanned the set earlier.
            print(day["date"])
            print(reading["time"])
            print(reading["id"])
            print(sum)

#KUNGRAD

