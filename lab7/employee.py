employee_dict = {}

num_emp = int(input("Enter number of employees: "))
for i in range(num_emp):
    name = str(input("Enter name of employee {}: ".format(i+1)))
    salary = int(input("Enter salary of employee{}: ".format(i+1)))
    employee_dict[name] = salary