# Topic: Functions on Python
# It's a block of code that can be called many times

def my_function():
    print("¡¡Function One by Viko!!")


my_function()

# Giving arguments or parameters to a function
# Parameters: Variables
# Arguments: Values

print('='*35)


# =========================================================== #
def my_second_func(name, lastName):
    print(f'{name} {lastName} is here')


my_second_func("Victor", "Luna")

print('='*35)


# =========================================================== #
def sum(a, b):
    return a + b


result = sum(45, 23)
print(f'Result: {result}')
print(f'Second Result: {sum(34, 36)}')

print('='*35)


# =========================================================== #
# Adding default values
def other_sum(a=0, b=0):
    return a + b


print('='*35)


# =========================================================== #
def name_list(*names):  # For unknown elements we add an *
    for name in names:
        print(name)


name_list('Jose', 'Charles', 'Edward')
print(type(name_list('Jose', 'Charles', 'Edward')))

print('='*35)


# =========================================================== #
def mult_values(*values):
    a = 1
    for val in values:
        a *= val
    return a


print(mult_values(1, 2, 3, 5))

print('='*35)


# =========================================================== #
def list_terms(**terms):  # kwargs: keyword arguments, it's used for dictionaries
    for key, value in terms.items():
        print(f'{key}: {value}')


list_terms(IDGAF='I Dont Give a Fuck', PK='Primary Key')
list_terms(DBMS='Data Base Management System')


print('='*35)


# =========================================================== #
def deploy_names(names):
    for name in names:
        print(name)


names = ['Joe', 'Charles', 'Mark']
deploy_names(names)
deploy_names('Chuck')
deploy_names((10, 11))
deploy_names([10, 11])

print('='*35)


# =========================================================== #
# Recursive functions
def factorial(number):
    if number == 1 or number == 0:
        return 1
    else:
        return number*factorial(number-1)


print('Type a number: ')
aNumber = int(input())
answer = factorial(aNumber)
print(f'{aNumber}! = {answer}')

print('='*35)

# =========================================================== #
