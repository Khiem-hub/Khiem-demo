try:
    hours = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))
except ValueError:
    print("Error, please enter numeric input")
    raise SystemExit

if hours > 40:
    regular_pay = 40 * rate
    overtime_hours = hours - 40
    overtime_pay = overtime_hours * rate * 1.5
    pay = regular_pay + overtime_pay
else:
    pay = hours * rate

print("Pay:", pay)