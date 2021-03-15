
# problem 1
# input_list = [0,5,6,4,-2,-3,6,7,10]
# largest = input_list[0]
# second_largest = largest
# for element in input_list:
#     if element > largest:
#         second_largest = largest
#         largest = element
# print(second_largest)

input_string = input('Enter:')

empty_stack = []
top = -1
is_valid = True

for element in input_string:
    if element == '{' or element == '(':
        empty_stack.append(element)
        top += 1
    elif element == ')':
        if top == -1 or empty_stack[top] != '(':
            is_valid = False
            break
        else:
            empty_stack.pop()
            top -= 1
    else:
        if top == -1 or empty_stack[top] != '{':
            is_valid = False
            break
        else:
            empty_stack.pop()
            top -= 1


if is_valid:
    print('valid')
else:
    print('invalid')






