print("Calculator\n")
print("Available options: +, -, *, /\n")

first_num = int(input("Enter first number: "))
action = input("Choose action for calculation: ")
second_num = int(input("Enter second number: "))


def sum(first_num, second_num):
    return first_num + second_num


def subt(first_num, second_num):
    return first_num - second_num


def mult(first_num, second_num):
    return first_num * second_num


def div(first_num, second_num):
    return first_num / second_num


def execution(action):
    if action == "+":
        print(str(sum(first_num, second_num)))
    elif action == "-":
        print(str(subt(first_num, second_num)))
    elif action == "*":
        print(str(mult(first_num, second_num)))
    elif action == "/":
        print(str(div(first_num, second_num)))
    else:
        print("There is no such action\n")


if __name__ == "__main__":
    execution(action)
