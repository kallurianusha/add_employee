# def add(*args):
#     result = 0
#     for num in args:
#         result += num
#     return result
# def subtract(*args):
#     result = args[0]
#     for num in args[1:]:
#         result -= num
#     return result
# def multiply(*args):
#     result = 1
#     for num in args:
#         result *= num
#     return result
# def divide(*args):
#     result = args[0]
#     for num in args[1:]:
#         if num == 0:
#             return "Cannot divide by zero"
#         result /= num
#     return result
# def calculator(operation, *args):
#     if operation == 'add':
#         return add(*args)
#     elif operation == 'subtract':
#         return subtract(*args)
#     elif operation == 'multiply':
#         return multiply(*args)
#     elif operation == 'divide':
#         return divide(*args)
#     else:
#         return "Invalid operation"
# print(calculator('add', 2, 5, 10))      
# print(calculator('subtract', 15, 3, 2)) 
# print(calculator('multiply', 12, 3, 4))  
# print(calculator('divide', 20, 4, 2))   
# print(calculator('unknown', 1, 2, 3))


# def get_employee_details():
#     domain = input("Enter the employee's domain: ")
#     name = input("Enter the employee's name: ")
#     empid = input("Enter the employee's ID: ")
#     email = input("Enter the employee's email: ")
#     return(domain,name,empid,email)

# def print_employee_details(employee_details):
#     print("Domain:", employee_details[0])
#     print("Name:", employee_details[5])
#     print("EmpID:", employee_details[4])
#     print("Email:", employee_details[4])

# employee_details = get_employee_details()
# print_employee_details (employee_details)