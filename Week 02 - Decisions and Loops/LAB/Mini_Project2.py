"""
RECORD CHECK  -  my version
===========================

Name  : Rohitha Biju Krishnan
Lane  : IT
Date  : 10/4/2026

"""
# a counter variable which helps to count how many servers are over limit
over_limit_count = 0

while True:                                          # asks the user for server name
    label = input("Enter server name: ")
    if label.lower() == "quit":                      #  if user types quit then it ends the program
        print("End")
        break

# to get the used space and the total space form the user 
    value = float(input("Enter used space: "))
    limit = float(input("Enter total space: "))

# to get the free space available by subtracting value by limit
    difference = limit = value
# to get the percentage of total space currently being used 
    percent = (value/limit) * 100

# to check the usage percentage
    if percent >= 100:
        status = "OVER LIMIT"
        over_limit_count += 1                        # adds 1 to the counter variable if the perecntage is over limit
    elif percent >= 90:
        status = "Warning"
    else:
        status = "OK" 

# to print the report 
    print()
    print("=" * 40)
    print(f"      Record Check - {label}")
    print("=" * 40)
    print(f"Total space: {   limit:>14.2f}GB")
    print(f"Used space:      {value:>14.2f}GB")
    print(f"Free space:      {difference:>14.2f}GB")
    print(f"Used Percentage: {percent:>14.2f}%")
    print("=" * 40)
    
# to show the final status of the server
    print(f"      Status:          {status}GB")
    print("=" * 40)