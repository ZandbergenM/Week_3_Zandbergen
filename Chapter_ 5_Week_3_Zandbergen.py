#Week 3 Module_Zandbergen
#5.1

import time
epoch = time.time()
#Need to convert to the time of day in hours, minutes, and seconds
#Need to determine days since epoch
#epoch is in SECONDS
def current_time(x):
	total_hours = x // 60 // 60 #takes dividing by 60 twice to get minutes then hours to get TOTAL number of hours
	current_hour = total_hours - (total_hours // 24) * 24 #converts total hours to the hour of the day rounded down
	total_minutes = x // 60 #diving by 60 to get total minutes
	current_minutes = total_minutes - (total_minutes // 60) * 60 #converts total minutes to current minute rounded down
	total_seconds = x // 1 #this will take the seconds divided by itself and rounded down
	current_seconds = total_seconds - (total_seconds // 60) * 60 #converts total seconds to current second rounded down
	return current_hour, current_minutes, current_seconds #returns the three values needed

print(current_time(epoch))

def days_since_epoch(x):
    total_hours = x // 60 // 60 #takes epoch, divides by 60 twice to get total hours
    days = total_hours// 24 #total hours divided by hours in a day
    return days

print(days_since_epoch(epoch))

#5.2
def check_fermat(a, b, c, n):
    if n > 2 and a**n + b**n == c**n:
        print ('Holy smokes, Fermat was wrong!')
    else:
        print ("No, that doesn't work")

def user_prompt():
    a = input('Type the value of A and press enter ')
    b = input('Type the value of B and press enter ')
    c = input('Type the value of C and press enter ')
    n = input('Type the value of N and press enter ')
    check_fermat(int (a), int (b), int (c), int (n))

user_prompt()







