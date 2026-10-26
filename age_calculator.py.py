
from datetime import date
import calendar

def age_calculator(bday, today):
    if bday > today:
        raise ValueError("Date of birth cannot be in the future.")
    years = today.year - bday.year
    months = today.month - bday.month
    days = today.day - bday.day
    if days < 0:
        months -= 1
        if today.month == 1:
            previous_month = 12
            previous_year = today.year - 1
        else:
            previous_month = today.month - 1
            previous_year = today.year

        days += calendar.monthrange(previous_year, previous_month)[1]
    if months < 0:
        years -= 1
        months += 12

    return years, months, days

def main():
    print("====- AGE CALCULATOR -====")
    dob = input("Enter your date of birth (YYYY-MM-DD): ")
    try:
        bday = date.fromisoformat(dob)
        today = date.today()
        years, months, days = age_calculator(bday, today)
        print(f"\nYou are {years} years, {months} months and {days} days old")

    except ValueError as error:
        print(f"\nInvalid input: {error}")


if __name__ == "__main__":
    main()
