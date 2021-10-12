# employee who has worked the most hours; employee of the month
work_hours = [('Arko', 200), ('Mithi', 300), ('Gampu', 800), ('Golu', 50),('Molu', 2000)]

def employee_of_month(hours_worked):
    current_max = 0
    emp_name = ''
    for name,hours in hours_worked :
        if hours > current_max :
            emp_name = name
            current_max = hours
        else :
            pass
    return (emp_name, current_max)
empOfMonth, maxHrs = employee_of_month(work_hours)

print(f'{empOfMonth} is the employee of the month havin worked {maxHrs} hours')
