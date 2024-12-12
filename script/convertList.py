file = open("onlyuserid.txt", "w")
predList = open("Predator.txt", "r")
predListLines = predList.readlines()

for i in range(3, len(predListLines)):
    getUserID1 = predListLines[i].split("/profile")[0]
    getUserID2 = getUserID1.split("https://www.roblox.com/users/")[-1:]
    finalGetuserID = getUserID2[0]
    file.write(finalGetuserID + "\n")
raise RuntimeError("Proccess is finished.")
