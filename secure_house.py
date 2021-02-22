#!/usr/bin/env python3
import sys

if __name__ == "__main__":
    
    
    authorizedKeys = []
    authorizedKeys.append("FIREFIGHTER_SECRET_KEY")
    
    approvedPerson = []
    inHouse = []
    owner = sys.argv[1]
    for i in range(2,len(sys.argv)):
        authorizedKeys.append(sys.argv[i])
    
    command = []
    # keyInserted = False

    
    for i in sys.stdin:
        if "exit" in i:
            print(i.split())
            break
        
        if "INSERT KEY" in i.rstrip():
            command = i.rstrip().split() # Line turned into list
            if (len(command) < 4):
                print("ERROR")
                pass
            # keyInserted = True
            user = command[2]
            key = command[3]
            # fkInserted = False
            # if key == "FIREFIGHTER_SECRET_KEY":
            #     fkInserted = True
            kInserter = user
            print("KEY",key,"INSERTED BY",user)
            
                
        if "TURN KEY" in i.rstrip():
            command = i.rstrip().split() # Line turned into list
            if (len(command) < 3):
                print("ERROR")
                continue
            user = command[2]
            access = False # Unless bottom passes
            
            if key in authorizedKeys:
                access = True
            # if fkInserted == True:
            #     temp = user
            #     user = kInserter
            if  access == True and user == kInserter:
                # if fkInserted == True:
                #     user = temp
                print("SUCCESS", user, "TURNS KEY", key)
            else:
                print("FAILURE",user,"UNABLE TO TURN KEY",key)
                # keyInserted = False
        
        if "ENTER HOUSE" in i.rstrip():
            command = i.rstrip().split() # Line turned into list
            if (len(command) < 3):
                print("ERROR")
                continue
            user = command[2]
            # if fkInserted == True:
            #     user = kInserter
            if access == True and user == kInserter:
                print("ACCESS ALLOWED")
                inHouse.append(user)
            else:
                print("ACCESS DENIED")

        if "WHO'S INSIDE?" in i.rstrip():
            if (len(inHouse) == 0):
                print("NOBODY HOME")
            else:
                # print(*inHouse)
                for person in range(0,len(inHouse)):
                    if (person == len(inHouse)-1):
                        print(inHouse[person],end = "\n")
                    else:
                        print(inHouse[person],end = ", ")

            
        
        if "CHANGE LOCKS" in i.rstrip():
            command = i.rstrip().split() # Line turned into list
            if (len(command) < 4):
                print("ERROR")
                continue
            user = command[2]
            if user == owner and owner in inHouse:
                print("OK")
                authorizedKeys.clear()
                authorizedKeys.append("FIREFIGHTER_SECRET_KEY")
                for nk in range(3,len(command)):
                    authorizedKeys.append(command[nk])
            else:
                print("ACCESS DENIED")
        
        

        if "LEAVE HOUSE" in i.rstrip():
            command = i.rstrip().split() # Line turned into list
            if (len(command) < 3):
                continue
            user = command[2]
            if user in inHouse:
                inHouse.remove(user)
                print("OK")
            else:
                print(user,"NOT HERE")
        
    # print("Exiting program")

