import datetime as dt
today = dt.date.today()
birthdate = dt.date(2004, 7, 1)
delta_age = (today - birthdate)
print(delta_age)
days_old = delta_age.days
print(days_old, "days")
years_old = days_old // 365
print(years_old, "years old")
print(f"You are {years_old} years old ")
print("You are", (years_old),"years old")
months = (days_old % 365) //30
print(f"You are {years_old} years old and {months} months old")
