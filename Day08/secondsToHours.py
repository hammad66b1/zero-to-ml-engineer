#1hr=3600s
#1s=1/3600hrs
#1hr=60min
#1min=1/60hr
#1min=60s
#1s=1/60min

sec=float(input("Enter number of seconds: "))
#sec to hr: 
hrs=sec//3600
#remaining time
min=(sec-(hrs*3600))//60
#remaining sec
sec=sec-((hrs*3600)+(min*60))
print(f"Time is: {int(hrs)} hours, {int(min)} minutes, {int(sec)} seconds")