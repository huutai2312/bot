import os
import datetime

def fileing(i):
    with open("Readme.md", "w") as file:
        file.write("abc {}".format(i))
        file.close()
        
def load():
    start_date = datetime.date(2021, 1, 1)
    end_date = datetime.date(2019, 12, 31)
    delta = datetime.timedelta(days=1)
    while (start_date <= end_date):
        start_date += delta
        mydate = start_date.strftime('%a %d %b %Y')
        print(mydate)
        fileing(mydate)
        os.system("git add .")
        os.system("git commit --date=\"{} 12:00 2021 +0500\" -m committt".format(mydate))
        
for i in range(1):
    load()
    
os.system("git push -f origin main")