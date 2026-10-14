"""
RECORD CHECK  -  my version
===========================

Name  : Rohitha Biju Krishnan
Lane  :  IT      (delete two)
Date  : 10/4/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

over_limit_count = 0

while True:
    label = input("Enter server name: ")
    if label.lower() == "quit":
        print("End")
        break

    value = float(input("Enter used space: "))
    limit = float(input("Enter total space: "))

    difference = limit = value
    percent = (value/limit) * 100

    if percent >= 100:
        status = "OVER LIMIT"
        over_limit_count += 1
    elif percent >= 90:
        status = "Warning"
    else:
        status = "OK" 

    print()
    print("=" * 40)
    print(f"      Record Check - {label}")
    print("=" * 40)
    print(f"Total space: {   limit:>14.2f}GB")
    print(f"Used space:      {value:>14.2f}GB")
    print(f"Free space:      {difference:>14.2f}GB")
    print(f"Used Percentage: {percent:>14.2f}%")
    print("=" * 40)
    print(f"      Status:          {status}GB")
    print("=" * 40)