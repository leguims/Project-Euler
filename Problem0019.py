Enonce = """
Counting Sundays

Problem 19
You are given the following information, but you may prefer to do some research for yourself.

 - Thirty days has September,
 - April, June and November.
   All the rest have thirty-one,
   Saving February alone,
   Which has twenty-eight, rain or shine.
   And on leap years, twenty-nine.
 - A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

# Iterator style
class dayByMonth:
    def __init__(self, start_year=1900, start_month='January', end_year=1900, end_month='December'):
        self.nameDay = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        self.day_a_week = len(self.nameDay)
        self.nameMonth = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        self.month_a_year = len(self.nameMonth)
        self.days_a_month = {'January': 31,
                           'February': 28,
                           'March': 31,
                           'April': 30,
                           'May': 31,
                           'June': 30,
                           'July': 31,
                           'August': 31,
                           'September': 30,
                           'October': 31,
                           'November': 30,
                           'December': 31
                           }
        self.first_day = {1900: 'Monday', 1901: 'Tuesday'}
        
        self.current_year = start_year
        self.current_month = start_month
        self.current_month_index = self.nameMonth.index(self.current_month)
        
        self.max_year = end_year
        self.max_month = end_month
        self.max_month_index = self.nameMonth.index(self.max_month)

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_year > self.max_year or ((self.current_year == self.max_year) and (self.current_month_index > self.max_month_index)) :
            raise StopIteration
        
        days_this_month = self.days_a_month[self.current_month]
        if self.current_month is 'February':
            leap = (self.current_year % 4 == 0) and (self.current_year % 100 != 0) or (self.current_year % 400 == 0)
            if leap:
                days_this_month = days_this_month + 1
                
        year, month = self.current_year, self.current_month
        self.nextMonth()
        return (year, month, days_this_month)

    def nextMonth(self):
        self.current_month_index = self.current_month_index + 1 if self.current_month_index < (self.month_a_year-1) else 0
        self.current_month = self.nameMonth[self.current_month_index]
        if self.current_month_index == 0:
            self.current_year = self.current_year + 1

def main():
    print(40*"=")
    print(Enonce)
    print(40*"-")

    Solution = 0
    start, end = 1901, 2000
    dayOfWeek = 2 # 1901 starts a Tuesday
    nameDay = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    for year, month, days in dayByMonth(start_year=start, end_year=end):
        #print(f"Month {month} of {year},  starts a {nameDay[dayOfWeek-1]}")
        if dayOfWeek == 0:
            Solution = Solution + 1
            print(f"Month {month} of {year}, starts a {nameDay[dayOfWeek-1]} !!!")
        #print(f"{year}, {month} : {days}")
        dayOfWeek = (dayOfWeek + days)%7

    print(f"{Solution} Sunday the first day of month from {start} to {end}.")
    
    print(40*"-")
    print("Solution = {}".format(Solution))
    print(40*"=")

if __name__ == "__main__":
    # execute only if run as a script
    main()
