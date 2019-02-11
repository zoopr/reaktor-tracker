import json

def pool(arr, start, end):
    side = min(arr[start], arr[end])
    #If it's a straight downhill or uphill edge, return 0
    if end == start+1:
        return 0
    total = 0
    for i in range(start+1, end):
        total += side - arr[i]
    return total


def main():
    j = json.load(open("D:/Github/flood.txt", "r"))
    for region in j["regions"]:
        lastReading = 0
        for ent in region["readings"]:
            #print(ent["readingID"])
            arr = ent["reading"]
            pools = sorted(range(len(arr)), key=lambda k: arr[k], reverse=True)
            flooded_high = max(pools[0], pools[1])
            flooded_low = min(pools[0], pools[1])
            floodedVol = pool(arr, flooded_low, flooded_high)
            for index in pools:
                if index < flooded_low:
                    floodedVol += pool(arr, index, flooded_low)
                    flooded_low = index
                if index > flooded_high:
                    floodedVol += pool(arr, flooded_high, index)
                    flooded_high = index
            if ent["readingID"] != "A":
                if abs(lastReading - floodedVol) > 1000:
                    #print(region["regionID"])
                    print(ent["readingID"])
                    break
            lastReading = floodedVol

main()

#FERIMED
