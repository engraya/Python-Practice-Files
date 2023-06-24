import datetime
from logging.handlers import TimedRotatingFileHandler



# user_name_surname = input("Please enter your name and surname here: ")
# user_country = input(" Please enter your country of residence here: ")

# user_input_date = input("Enter your preparation date seperated by a colon:\n")
# input_list = user_input_date.split(":")

# preparation = input_list[0]
# deadline = input_list[1]

# updated_deadline = datetime.datetime.strptime(deadline, "%d.%m.%Y")


# todays_date = datetime.datetime.today()
# time_till_last_date = updated_deadline - todays_date
# print(time_till_last_date)
# calculated_days = time_till_last_date.days


# time_till_last_date_in_years = int(calculated_days / 365)
# time_till_last_date_in_months = int(calculated_days / 12)
# time_till_last_date_in_weeks = int(calculated_days / 7)
# time_till_last_date_in_days = calculated_days
# time_till_last_date_in_hours = int(time_till_last_date.total_seconds()/60/60)
# time_till_last_date_in_minutes = int(time_till_last_date.total_seconds()/60) 
# time_till_last_date_in_seconds = int(time_till_last_date.total_seconds())


# print(f"User Profile:")
# print(user_name_surname)
# print(f"{user_country}\n")
# print(f"Dear {user_name_surname}, the time remaining from today to the dealine of the date entered is:\n")
# print(f"preparation: {preparation}\n")
# print(f"Todays Date: {datetime.datetime.today()}\n")
# print(f"Expected Deadline : {deadline}\n")
# print(f"Days to Deadline in Years : {time_till_last_date_in_years} years\n")
# print(f"Days to Deadline in Months : {time_till_last_date_in_months} months\n")
# print(f"Days to Deadline in Weeks : {time_till_last_date_in_weeks} weeks\n")
# print(f"Days to Deadline in Days : {time_till_last_date_in_days} days\n")
# print(f"Days to Deadline in Hours : {time_till_last_date_in_hours} hours\n")
# print(f"Days to Dealine in Minutes : {time_till_last_date_in_minutes} minutes\n")
# print(f"Days to Deadline in Seconds : {time_till_last_date_in_seconds} seconds\n")


user_name_surname = input("Please enter your name and surname here: ")
user_country = input(" Please enter your country of residence here: ")

user_input_date = input("Enter your preparation expected Date below:\n")

preparation =input("Enter your goal or preparation here: ")
deadline = input("Enter the expected date here: ")

updated_deadline = datetime.datetime.strptime(deadline, "%d.%m.%Y")


todays_date = datetime.datetime.today()
time_till_last_date = updated_deadline - todays_date
print(time_till_last_date)
calculated_days = time_till_last_date.days


time_till_last_date_in_years = int(calculated_days / 365)
time_till_last_date_in_months = int(calculated_days / 12)
time_till_last_date_in_weeks = int(calculated_days / 7)
time_till_last_date_in_days = calculated_days
time_till_last_date_in_hours = int(time_till_last_date.total_seconds()/60/60)
time_till_last_date_in_minutes = int(time_till_last_date.total_seconds()/60) 
time_till_last_date_in_seconds = int(time_till_last_date.total_seconds())


print(f"User Profile:")
print(user_name_surname)
print(f"{user_country}\n")
print(f"Dear {user_name_surname}, the time remaining from today to the dealine of the date entered is:\n")


print("GOAL NUMBER 1")
print(f"preparation: {preparation}\n")
print(f"Todays Date: {datetime.datetime.today()}\n")
print(f"Expected Deadline : {deadline}\n")
print(f"Days to Deadline in Years : {time_till_last_date_in_years} years\n")
print(f"Days to Deadline in Months : {time_till_last_date_in_months} months\n")
print(f"Days to Deadline in Weeks : {time_till_last_date_in_weeks} weeks\n")
print(f"Days to Deadline in Days : {time_till_last_date_in_days} days\n")
print(f"Days to Deadline in Hours : {time_till_last_date_in_hours} hours\n")
print(f"Days to Dealine in Minutes : {time_till_last_date_in_minutes} minutes\n")
print(f"Days to Deadline in Seconds : {time_till_last_date_in_seconds} seconds\n")


print("GOAL NUMBER 1")
print(f"preparation: {preparation}\n")
print(f"Todays Date: {datetime.datetime.today()}\n")
print(f"Expected Deadline : {deadline}\n")
print(f"Days to Deadline in Years : {time_till_last_date_in_years} years\n")
print(f"Days to Deadline in Months : {time_till_last_date_in_months} months\n")
print(f"Days to Deadline in Weeks : {time_till_last_date_in_weeks} weeks\n")
print(f"Days to Deadline in Days : {time_till_last_date_in_days} days\n")
print(f"Days to Deadline in Hours : {time_till_last_date_in_hours} hours\n")
print(f"Days to Dealine in Minutes : {time_till_last_date_in_minutes} minutes\n")
print(f"Days to Deadline in Seconds : {time_till_last_date_in_seconds} seconds\n")

print("GOAL NUMBER 1")
print(f"preparation: {preparation}\n")
print(f"Todays Date: {datetime.datetime.today()}\n")
print(f"Expected Deadline : {deadline}\n")
print(f"Days to Deadline in Years : {time_till_last_date_in_years} years\n")
print(f"Days to Deadline in Months : {time_till_last_date_in_months} months\n")
print(f"Days to Deadline in Weeks : {time_till_last_date_in_weeks} weeks\n")
print(f"Days to Deadline in Days : {time_till_last_date_in_days} days\n")
print(f"Days to Deadline in Hours : {time_till_last_date_in_hours} hours\n")
print(f"Days to Dealine in Minutes : {time_till_last_date_in_minutes} minutes\n")
print(f"Days to Deadline in Seconds : {time_till_last_date_in_seconds} seconds\n")

