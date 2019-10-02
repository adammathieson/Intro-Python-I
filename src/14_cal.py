"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

# print(calendar.weekheader(3))
# print(calendar.firstweekday())
# print(calendar.month(2019, 10))
# print(calendar.calendar(2018))

def printCalendar(file='12_cal.py', month=10, year=2019):
  user_data = input('14_cal.py month [year]')
  separate_fields = user_data.split()
  print(separate_fields)
  input_file = separate_fields[0]
  input_month = separate_fields[1]
  input_year = separate_fields[2]
  user_calendar = calendar.month(int(input_year), int(input_month))
  print(user_calendar)


  # userCalendar = calendar.month(year, month)
  # print(userCalendar)
printCalendar()