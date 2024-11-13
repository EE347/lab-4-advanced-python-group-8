import csv
with open("task5.csv", 'w', newline = '') as f:
    writer = csv.writer(f)
    while(True):
        name = input("type your name here!")
        if (name == "quit"):
           break
        writer.writerow([name])
with open ('task5.csv', 'r', newline = '') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(', '.join(row))
        print("add sonmething ")
    
           
    
