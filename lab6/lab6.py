from calc import *

def exec_program(lst):
    if is_program(lst):
        statements = program_statements(lst)
        for statement in statements:
            if is_output(statement):
                print_statement(statement)
            if is_selection(statement):
                if_statement(statement)
            if is_binaryexpr(statement):
                binary_statement(statement)
            if is_constant(statement):
                return statement

def exec_statement(lst):
    print(lst)
    if isinstance(lst[0],list) and isinstance(lst,list):
        for statement in lst:
            if is_output(statement):
                print_statement(statement)
            if is_selection(statement):
                if_statement(statement)
            if is_binaryexpr(statement):
                binary_statement(statement)
            if is_constant(statement):
                return statement
    else:
        if is_output(lst):
            print_statement(lst)
        if is_selection(lst):
            if_statement(lst)
        if is_binaryexpr(lst):
            binary_statement(lst)
        if is_constant(lst):
            return lst
    

def print_statement(print_list):
        print(output_expression(print_list))

calc1 = ['calc', [4]]
# print_list = ['print', 2 + 4]

[3, "+", 5]

def binary_statement(lst):
    result = None
    if binaryexpr_operator(lst) == "+":
        result = binaryexpr_left(lst) + binaryexpr_right(lst)
    elif binaryexpr_operator(lst) == "-":
        result = binaryexpr_left(lst) - binaryexpr_right(lst)
    elif binaryexpr_operator(lst) == "/":
        result = binaryexpr_left(lst) / binaryexpr_right(lst)
    elif binaryexpr_operator(lst) == "*":
        result = binaryexpr_left(lst) * binaryexpr_right(lst)
    return result

def if_statement(if_list):
    if is_condition(if_list[1]):
        new = if_list[1] 
        if condition_operator(new) == '>':
            if exec_statement(condition_left(new)) > exec_statement(condition_right(new)):
                exec_statement(if_list[2:])
            else:
                exec_statement(if_list[3])
        if condition_operator(new) == '<':
            if condition_left(new) < condition_right(new):
                exec_statement(if_list[2:])
            else:
                exec_statement(if_list[3])
        if condition_operator(new) == '=':
            if condition_left(new) == condition_right(new):
                exec_statement(if_list[2:])
            else:
                exec_statement(if_list[3])


    
calc2 = ['calc', ['if', [[3, "+", 5], '>', 5], ['print', 2], ['print', 4]]]
calc3 = ['calc', ['if', [3, '=', 5], ['print', 2], ['print', 4]]]
['if', [[3, "+", 5], '>', 5], ['print', 2]]

exec_program(calc2)