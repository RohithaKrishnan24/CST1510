"""
RECORD CHECK  -  my version
===========================

Name  : ROHITHA BIJU KRISHNAN
Lane  : IT      
Date  : 10/4/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""
over_limit_count = 0 

while True:                                                    # repeats the program till break (if typed quit)
    label = input("Enter the server name: ")

    if label.lower() == "quit":                                # if user types quit it stops the program
        print("End")
        break                                                  # exit loop

    value = float(input("Enter used space: "))                 # stores used space
    limit = float(input("Enter total space: "))                # stores total space 

    difference = limit - value
    percent = (value / limit) * 100                            # percentage

    if percent >= 100:
        status = "OVER LIMIT"
        over_limit_count += 1
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"

    print()
    print("=" * 40)
    print(f"      Record Check -  {label}")
    print("=" * 40)
    print(f"Total space:     {limit:>14.2f} GB")
    print(f"Used space:      {value:>14.2f} GB")
    print(f"Free space:      {difference:>14.2f} GB")
    print(f"Used percentage: {percent:14.2f} %")
    print("=" * 40)
    print(f"      Status:          {status}")
    print("=" * 40)